import discord
from discord.utils import get
from discord.ext import commands
from bs4 import BeautifulSoup as soup
from .utils import Pyson, checks

all_emojis = Pyson("./cogs/data/emojis", [])
saved_notifications = Pyson("./cogs/data/saved_notifications", [])
server_emojis = Pyson("./cogs/data/emoji_roles")


class Check_Emoji(commands.Converter):
    async def convert(self, ctx, emoji):
        if emoji in all_emojis.data:
            return emoji
        try:
            emoji = await commands.EmojiConverter().convert(ctx, emoji)
        except:
            emoji = None
        return emoji


def check_guild(guild):
    if str(guild.id) not in server_emojis.data:
        server_emojis.data[str(guild.id)] = {}


class Emoji_Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            check_guild(guild)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        check_guild(guild)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id in saved_notifications.data:
            user, role = self.parse_reaction(payload)
            if role:
                await user.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id in saved_notifications.data:
            user, role = self.parse_reaction(payload)
            if role:
                await user.remove_roles(role)

    @commands.Cog.listener()
    async def on_raw_message_delete(self, payload):
        if payload.message_id in saved_notifications.data:
            saved_notifications.data.remove(payload.message_id)
            saved_notifications.save

    def parse_reaction(self, payload):
        guild = self.bot.get_guild(payload.guild_id)
        user = guild.get_member(payload.user_id)
        role = None
        if not user.bot:
            role_name = (
                server_emojis.data.get(str(guild.id))
                .get(payload.emoji.name)
                .get("role")
            )
            role = get(guild.roles, name=role_name)
        return user, role

    @checks.is_admin()
    @commands.command()
    async def categories(self, ctx):
        ": Check what categories are available"
        embed = discord.Embed(
            title="Categories",
            description="\n".join(item for item in self._categories(ctx.guild)),
            color=discord.Color.green(),
        )
        await ctx.send(embed=embed)

    @checks.is_admin()
    @commands.command()
    async def update_emojis(self, ctx):
        """
        : Update the bots list of supported emojis
        """
        r = await self.bot.aiohttp.get("https://getemoji.com/")
        if r.status == 200:
            html = await r.text("utf-8")
            page = soup(html, "html.parser")
            tags = page.findAll(
                "p", {"style": "font-family: Segoe UI Emoji; font-size: 3.5em"}
            )
            all_emojis.data = []
            for emojis in tags:
                all_emojis.data += emojis.text.split()
            all_emojis.save()
            await ctx.send("Emojis have been updated!")
        else:
            await ctx.send("There was an error fetching emojis!")

    @checks.is_admin()
    @commands.command(no_pm=True, aliases=["aer", "add"])
    async def add_emoji_role(
        self,
        ctx,
        category: str,
        emoji: Check_Emoji,
        role: discord.Role,
        *,
        description: str = " ",
    ):
        ": Assign emojis to a specific role. Emojis with common categories will be posted together on the next notificaiton message."
        category = category.lower()
        d = {"type": category, "role": role.name, "description": description}
        if isinstance(emoji, str):
            server_emojis.data[str(ctx.guild.id)][emoji] = d
        else:
            server_emojis.data[str(ctx.guild.id)][emoji.name] = d
        server_emojis.save
        await ctx.send(
            f"{emoji} will assign {role.mention} in newly created **{category}** notifications."
        )
        await ctx.message.delete()

    @checks.is_admin()
    @commands.command(no_pm=True, aliases=["der", "delete"])
    async def delete_emoji_role(self, ctx, emoji: Check_Emoji):
        ": Enter the emoji you would like to remove"
        if isinstance(emoji, str):
            del server_emojis.data[str(ctx.guild.id)][emoji]
        else:
            del server_emojis.data[str(ctx.guild.id)][emoji.name]
        server_emojis.save
        await ctx.send(
            f"{emoji} will no longer assign roles. Please create a new message to assign roles."
        )

    @checks.is_admin()
    @commands.command(no_pm=True)
    async def create(self, ctx, category: str):
        ": Create a role assigning message from the categories you have created."
        category = category.lower()
        if category in self._categories(ctx.guild):
            config = []
            for key, value in server_emojis.data[str(ctx.guild.id)].items():
                if value.get("type") == category:
                    em = [
                        await Check_Emoji().convert(ctx, key),
                        get(ctx.guild.roles, name=value.get("role")).mention,
                        value.get("description"),
                    ]
                    config.append(em)
            description = "\n".join(
                f"{item[0]} {item[1]} - {item[2]}" for item in config
            )
            embed = discord.Embed(
                title=f"{category} Notifications".title(),
                description=description,
                color=discord.Color.blue(),
            )
            message = await ctx.send(embed=embed)
            for emoji in config:
                await message.add_reaction(emoji[0])
            saved_notifications.data.append(message.id)
            saved_notifications.save
        else:
            await ctx.send(f"*{category}* in not a valid category.")

    def _categories(self, guild):
        return set(
            list(v.get("type") for v in server_emojis.data[str(guild.id)].values())
        )


def setup(bot):
    bot.add_cog(Emoji_Roles(bot))
