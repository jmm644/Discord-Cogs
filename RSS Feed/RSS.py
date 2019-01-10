from datetime import datetime
import re
from time import mktime
import aiohttp
import asyncio
import feedparser
import discord
from discord.ext import commands
from cogs.utils import Pyson
from cogs.utils.classes.rss_feed import Rss_Feed


class RSS:

    def __init__(self, bot):
        self.bot = bot
        self.rss = Pyson('cogs/data/rss')
        self.bot.loop.create_task(self.feed_update())

    @commands.command()
    async def rssSubscribe(self, ctx, link: str, channel: discord.TextChannel):
        ': Subscribe to an RSS feed'
        try:
            test = await self.get_feed(link)
        except:
            await ctx.channel.send(f'*{link}* is an invalid RSS feed')
            return

        if test.bozo:
            await ctx.channel.send(f'*{link}* is an invalid RSS feed')
        elif not isinstance(channel, discord.TextChannel):
            await ctx.channel.send('Channel must be a text channel')
        elif link not in self.rss.data:
            self.rss.data[link] = {
                'last_post': datetime.utcnow().timestamp(),
                'channel': channel.id
            }
            self.rss.save
            await ctx.channel.send('Link has been added')
        else:
            await ctx.channel.send(f'*{link}* already exists!')

    @commands.command()
    async def rssUnsubscribe(self, ctx, link: str):
        ': Unsubscribe from an RSS feed'
        if self.rss.data.get(link):
            await ctx.channel.send(f'You have unsubscribed from {link}')
            del self.rss.data[link]
            self.rss.save
        else:
            await ctx.channel.send(f'You are not currently subscribed to *{link}*')

    @commands.command()
    async def rssFeeds(self, ctx):
        ': See what RSS feeds you are currently subscribed to'
        links = ''
        channels = ''
        for link, info in self.rss.data.items():
            links += f'{link}\n'
            channels += f'{self.bot.get_channel(info.get("channel")).mention} \n'

        if links:
            embed = discord.Embed(title='Following', color=discord.Colour.green())
            embed.add_field(name='Link', value=links)
            embed.add_field(name='Channel', value=channels)
            return await ctx.channel.send(embed=embed)
        return await ctx.channel.send('You have not added any RSS links!')

    async def get_feed(self, URL):
        async with aiohttp.ClientSession() as session:
            async with session.get(URL) as r:
                if r.status == 200:
                    text = await r.text()
                    parsed = feedparser.parse(text)
                    return Rss_Feed(parsed)

    def latest(self, old, new):
        old = datetime.fromtimestamp(old)
        new = datetime.fromtimestamp(new)
        if (new-old).total_seconds() > 0:
            return True

    async def send_embed(self, entry, channel, image=None):
        embed = discord.Embed(title=f'Post by {entry.author}', description=entry.title, url=entry.link, color=discord.Color.blue())
        if image:
            embed.set_thumbnail(url=image)
        await channel.send(embed=embed)

    async def feed_update(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            for link, info in tuple(self.rss.data.items()):
                new_post = False
                last_post = info.get('last_post')
                channel = self.bot.get_channel(info.get('channel'))
                feed = await self.get_feed(link)
                if feed:
                    published_times = []
                    for entry in feed.entries:
                        published = mktime(entry.published_parsed)
                        published_times.append(published)
                        if self.latest(last_post, published):
                            new_post = True
                            await self.send_embed(entry, channel, image=feed.feed.image.href)
                    if new_post:
                        self.rss.data[link]['last_post'] = sorted(published_times, reverse=True)[0]
                        self.rss.save
            await asyncio.sleep(600)


def setup(bot):
    bot.add_cog(RSS(bot))
