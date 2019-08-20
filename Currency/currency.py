import dataset
import discord
from discord.ext import commands

db = dataset.connect('sqlite:///cogs/data/banks.db')


def is_owner_or_has_role():
    async def predicate(ctx):
        if await ctx.bot.is_owner(ctx.author) or ctx.author == ctx.guild.owner or any(role.name in Bank(ctx.guild).approved for role in ctx.author.roles):
            return True

    return commands.check(predicate)


def tableName(guild):
    return f'guild_{guild.id}'


def checkGuild(ctx):
    if tableName(ctx.guild) not in db.tables:
        table = db.get_table(tableName(ctx.guild))
        table.insert(dict(currency_name='dollar'))
        table.create_column('member', dataset.types.Integer)
        table.create_column('balance', dataset.types.Integer)
        table.create_column('approved', dataset.types.UnicodeText)
    return True


class Bank:
    def __init__(self, guild):
        self._name = tableName(guild)
        self._table = db.get_table(self._name)

    def changeCurrency(self, currency):
        if currency.lower().endswith('s'):
            currency = currency[:-1]
        self._table.upsert(dict(id=1, currency_name=currency), ['id'])

    def get_account(self, member):
        return Account(member, self._table)

    @property
    def currency(self):
        return list(r.get('currency_name') for r in self._table.find(id=1) if r)[0]

    @property
    def approved(self):
        query = f'SELECT approved FROM {self._name} WHERE approved IS NOT NULL'
        result = db.query(query)
        return list(role.get('approved') for role in result)

    def addApproved(self, *roles):
        inserts = list(dict(approved=role.name) for role in roles)
        self._table.insert_many(inserts)

    def removeApproved(self, *roles):
        for role in roles:
            self._table.delete(approved=role.name)


class Account:

    def __init__(self, member, table):
        self.id = member.id
        self._table = table

    @property
    def _account(self):
        return self._table.find_one(member=self.id)

    @property
    def balance(self):
        if self._account is None:
            return 0
        else:
            return self._account.get('balance')

    def deposit(self, amount):
        self._table.upsert(dict(member=self.id, balance=self.balance+amount), ['member'])

    def withdraw(self, amount):
        self._table.upsert(dict(member=self.id, balance=self.balance-amount), ['member'])



class Currency(commands.Cog):
    '''
    A cog with basic currency commmands
    '''

    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        if not ctx.guild:
            return
        return checkGuild(ctx)

    @commands.command(aliases=['bank', 'stash'])
    async def balance(self, ctx, member: discord.Member = None):
        '''
        : Check the balance of your account or another member
        '''
        if not member:
            member = ctx.author
        bank = Bank(ctx.guild)
        account = bank.get_account(member)
        await ctx.send(f'{member.mention} has **{account.balance}** {bank.currency}s')

    @is_owner_or_has_role()
    @commands.command(aliases=['add', 'give'])
    async def deposit(self, ctx, amount: int = 0,  member: discord.Member = None):
        '''
        : Deposit currency into a members account
        usage:
            deposit <amount> <@member>
        '''
        if not member:
            member = ctx.author
        bank = Bank(ctx.guild)
        account = bank.get_account(member)
        account.deposit(amount)
        await ctx.send(f'**{amount}** {bank.currency}s have been deposited into {member.mention}\'s account!')

    @is_owner_or_has_role()
    @commands.command(aliases=['remove', 'take'])
    async def withdraw(self, ctx, amount: int = 0,  member: discord.Member = None):
        '''
        : Withdraw currency from a members account
        usage:
            withdraw <amount> <@member>
        '''
        if not member:
            member = ctx.author
        bank = Bank(ctx.guild)
        account = bank.get_account(member)
        account.deposit(-amount)
        await ctx.send(f'**{amount}** {bank.currency}s have been withdrawn from {member.mention}\'s account!')

    @is_owner_or_has_role()
    @commands.command(aliases=['currencyname'])
    async def changeCurrency(self, ctx, name: str='dollar'):
        '''
        : Change the currency name that the server is using
        usage:
            changeCurrency <currency_name>
        note:
            default currency is 'dollars'
        '''
        bank = Bank(ctx.guild)
        bank.changeCurrency(name)
        await ctx.send(f'The currency has been changed to **{bank.currency}s**')

    @commands.command()
    async def leaderboard(self, ctx):
        '''
        : Get a leaderboard showing the top 10 members with the largest account
        usage:
            leaderboard
        '''
        table = db.get_table(tableName(ctx.guild))
        embed = discord.Embed(title='Leaderboard', color=discord.Color.gold())
        currency = list(r.get('currency_name') for r in table.find(id=1) if r)[0]+'s'
        members = ''
        points = ''
        for member in table.find(order_by=['-balance'], _limit=10):
            if member.get('balance'):
                m = ctx.guild.get_member(member.get('member'))
                if m:
                    members += f'{m.mention}\n'
                    points += f'{member.get("balance")}\n'
        if members:
            embed.add_field(name='Member', value=members)
            embed.add_field(name=currency.title(), value=points)
        else:
            embed.description = f'Nobody has any {currency}'
        await ctx.send(embed=embed)

    @is_owner_or_has_role()
    @commands.command()
    async def approved(self, ctx):
        '''
        : Get a list of approved roles that can deposit or withdraw from members
        usage:
            approved
        '''
        bank = Bank(ctx.guild)
        description = '\n'.join(discord.utils.get(ctx.guild.roles, name=role).mention for role in bank.approved if discord.utils.get(ctx.guild.roles, name=role))
        embed = discord.Embed(title='Approved Roles', description=description, color=discord.Color.green())
        await ctx.send(embed=embed)

    @commands.is_owner()
    @commands.command(aliases=['addrole'])
    async def addApproved(self, ctx, roles: commands.Greedy[discord.Role]):
        '''
        : Add roles that can deposit or withdraw currency from members
        usage:
            addApproved <@role>
        note:
            multiple roles can be added in one command
        '''
        Bank(ctx.guild).addApproved(*roles)
        await ctx.send('Approved roles have been added!')

    @commands.is_owner()
    @commands.command(aliases=['delrole'])
    async def delApproved(self, ctx, roles: commands.Greedy[discord.Role]):
        '''
        : Remove roles that can deposit or withdraw currency from members
        usage:
            delApproved <@role>
        note:
            multiple roles can be added in one command
        '''
        Bank(ctx.guild).removeApproved(*roles)
        await ctx.send('Approved roles have been removed!')


def setup(bot):
    bot.add_cog(Currency(bot))
