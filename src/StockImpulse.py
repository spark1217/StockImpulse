from email import message
import discord 
import random
import requests
import finnhub
import config

# tokens
DISCORD_TOKEN = config.tokens['discord_token']
FINNHUB_TOKEN = config.tokens['finnhub_token']

client = discord.Client(intents=discord.Intents.all())

# setup finnhub
finnhub_client = finnhub.Client(api_key=FINNHUB_TOKEN)

@client.event
async def on_ready():
    print('Logged in {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
    
    if message.channel.name == 'bot-testing':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        if user_message.lower() == 'bye':
            await message.channel.send(f'See you later! {username}!')
            return
        if user_message.lower() == '!random':
            await message.channel.send(f'Thats quite random bro {username}!')
            return

    if user_message.lower() == '!anywhere':
        await message.channel.send(f'This can be used anywhere {username}!')
        return

# Example stock output
# https://github.com/Finnhub-Stock-API/finnhub-python
res = finnhub_client.stock_candles('AAPL', 'D', 1590988249, 1591852249)
print(res)

client.run(DISCORD_TOKEN)

