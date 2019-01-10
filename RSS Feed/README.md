# Assign role with an emoji reaction

This should work with all custom and standard emojis.

# Getting Started
## This is built for my [Basic-Cog-Bot](https://github.com/stroupbslayen/Basic-Cog-Bot)
- Install the requirements with `pip install -r requirements.txt`
- Put the script and 'utils' folder in the 'cogs' folder of the Cog Bot and that's it!

# Commands
## rssSubscribe
- Aliases - N/A
- Usage - `<prefix>rssSubscribe <rss_link> <channel>`
- Example - `!rssSubscribe rss.feed RSS_Channel`
- Description - Subscribe to an RSS feed. Updates to the feed will be posted in the mentioned channel

## rssUnSubscribe
- Aliases - N/A
- Usage - `<prefix>rssUnSubscribe <rss_link>`
- Example - `!rssUnSubscribe rss.feed`
- Description - Unsubscribe from an RSS feed.

## rssFeeds
- Aliases - N/A
- Usage - `<prefix>rssFeeds`
- Example - `!rssFeeds`
- Description - See what RSS feeds you are currently subscribed to

# Notes
- Python 3.6 is required
- `feedparser` is required
- Anyone can add an RSS feed