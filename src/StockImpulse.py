import discord 
import random

TOKEN='MTAyMjk0MjMwNjM1MDk0NDM0Ng.G24d9m.roxUvVQaRrQjedKAkjTgTa70T9lznBnxrOsmHk'

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('Logged in {0.user}'.format(client))

client.run(TOKEN)
