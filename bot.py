import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import os
from feedparser import parse


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

"""Bot that fetches and shares the latest news from an RSS feed.
def get_latest_news():
    feed_url = "https://news.google.com/rss"
    feed = parse(feed_url)
    latest_entries = feed.entries[:5]  # Get the latest 5 news entries
    news_list = []
    for entry in latest_entries:
        news_list.append(f"{entry.title}\n{entry.link}\n")
    return news_list
    """
def get_bbc_cyber_news():
    feed_url = "https://feeds.bbci.co.uk/news/technology/rss.xml"
    feed = parse(feed_url)
    return [
        (entry.title, entry.link) 
        for entry in feed.entries
        if any(k in entry.title.lower() for k in ['cyber', 'security', 'hacker', 'data breach'])

    ][:5]  # Get the latest 5 relevant news entries
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    post_news.start()

@tasks.loop(hours=6)
async def post_news():
    channel_id = 1436438342286835753
    channel = bot.get_channel(channel_id)
    news =  get_bbc_cyber_news()
    if news:
        await channel.send("@everyone")
        await channel.send("DON'T WORRY GUYS! ZOID IS HERE!")
        await channel.send("🔔 **Cybersecurity News Update!** 🔔")
        await channel.send("Here are the latest cybersecurity news articles ( USING BBC AS THE MAIN SOURCE):\n")
        
        for title, link in news:
            await channel.send(f"{title}\n{link}\n")
    else:
        await channel.send("No new cybersecurity news articles found.")

@bot.command()
async def news(ctx):
    news = get_bbc_cyber_news()
    if not news:
        await ctx.send("No new cybersecurity news articles found.")
    else:
        msg = "\n".join([f"• [{t}]({l})" for t, l in news])
        await ctx.send(f"Here are the latest cybersecurity news articles:\n{msg}")

bot.run(TOKEN) 

#Bot that fetches and shares the latest news from an RSS feed.
