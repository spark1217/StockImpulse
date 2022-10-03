import config
import discord
from discord.ext import commands
import finnhub
import time

# tokens
DISCORD_TOKEN = config.tokens['discord_token']
FINNHUB_TOKEN = config.tokens['finnhub_token']

client = commands.Bot(command_prefix='!', intents=discord.Intents.all()) #discord.Client(intents=discord.Intents.all())

# setup finnhub
finnhub_client = finnhub.Client(api_key=FINNHUB_TOKEN)

# print message when ready
@client.event
async def on_ready_test():
    print('Logged in {0.user}'.format(client))

client.run(DISCORD_TOKEN)
time.sleep(10)
client.close()
