import discord 
import random

TOKEN='DEFAULT'

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('Logged in {0.user}'.format(client))

client.run(TOKEN)
