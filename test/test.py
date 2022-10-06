import discord
from discord.ext import commands
import finnhub
import time 
import config
import asyncio
import requests


# tokens
DISCORD_TOKEN = config.tokens['testing_token']
FINNHUB_TOKEN = config.tokens['finnhub_token']
SERVER_TOKEN = config.tokens['channel-token']

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# setup finnhub
finnhub_client = finnhub.Client(api_key=FINNHUB_TOKEN)

# print message when ready
@client.event
async def on_ready_test():
    print('Logged in {0.user}'.format(client))
    time.sleep(10)
    client.close()

@client.event
async def on_ready():
    fails = 0
    fails += await test_price()
    fails += await test_invalid_price()
    fails += await test_stock()
    fails += await test_invalid_stock()
    fails += await test_crypto()
    fails += await test_invalid_crypto()
    assert fails == 0
    await client.close()

async def test_price():
    channel = discord.utils.get(client.get_all_channels(), name='bot-testing')
    await channel.send("!price AAPL")
    stock_info = finnhub_client.quote("AAPL")
    content = f'```AAPL is currently ${stock_info["c"]}```'
    try:
        await client.wait_for('message', timeout=2, check=lambda x: x.guild.id == channel.guild.id and x.author.name == 'StockImpulse' and str(content) in x.content)
        return 0
    except asyncio.TimeoutError:
        return 1

async def test_invalid_price():
    channel = discord.utils.get(client.get_all_channels(), name='bot-testing')
    await channel.send("!price abcdefg")
    content = "Stock abcdefg does not exist or has no value."
    try:
        await client.wait_for('message', timeout=10, check=lambda x: x.guild.id == channel.guild.id and x.author.name == 'StockImpulse' and str(content) in x.content)
        return 0
    except asyncio.TimeoutError:
        return 1

async def test_stock():
    channel = discord.utils.get(client.get_all_channels(), name='bot-testing')
    await channel.send("!stock AAPL")
    stock_info = finnhub_client.quote("AAPL")
    if stock_info["d"] >= 0:
        content = f"""```AAPL Information
Current Price:    ${stock_info["c"]}
Change:           ${stock_info["d"]}
Percent Change:   {stock_info["dp"]}%
Daily High:       ${stock_info["h"]}
Daily Low:        ${stock_info["l"]}
Open Price:       ${stock_info["o"]}
Last Close Price: ${stock_info["pc"]}```"""
    else:
        content = f"""```AAPL Information
Current Price:    ${stock_info["c"]}
Change:          -${abs(stock_info["d"])}
Percent Change:   {stock_info["dp"]}%
Daily High:       ${stock_info["h"]}
Daily Low:        ${stock_info["l"]}
Open Price:       ${stock_info["o"]}
Last Close Price: ${stock_info["pc"]}```"""
    try:
        await client.wait_for('message', timeout=10, check=lambda x: x.guild.id == channel.guild.id and x.author.name == 'StockImpulse' and str(content) in x.content)
        return 0
    except asyncio.TimeoutError:
        return 1

async def test_invalid_stock():
    channel = discord.utils.get(client.get_all_channels(), name='bot-testing')
    await channel.send("!stock abcdefg")
    content = "Stock abcdefg does not exist or has no value."
    try:
        await client.wait_for('message', timeout=10, check=lambda x: x.guild.id == channel.guild.id and x.author.name == 'StockImpulse' and str(content) in x.content)
        return 0
    except asyncio.TimeoutError:
        return 1

async def test_crypto():
    channel = discord.utils.get(client.get_all_channels(), name='bot-testing')
    await channel.send("!crypto ETH")
    key = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"
    data = requests.get(key, timeout=10)
    data = data.json()
    cprice =  round(float(data['price']), 3)
    content = f"```{data['symbol']} price is ${cprice}```"
    try:
        await client.wait_for('message', timeout=10, check=lambda x: x.guild.id == channel.guild.id and x.author.name == 'StockImpulse' and str(content) in x.content)
        return 0
    except asyncio.TimeoutError:
        return 1

async def test_invalid_crypto():
    channel = discord.utils.get(client.get_all_channels(), name='bot-testing')
    await channel.send("!crypto abcdefg")
    content = f"There was an issue getting the information for abcdefg."
    try:
        await client.wait_for('message', timeout=10, check=lambda x: x.guild.id == channel.guild.id and x.author.name == 'StockImpulse' and str(content) in x.content)
        return 0
    except asyncio.TimeoutError:
        return 1
    
if __name__ == '__main__':
    client.run(DISCORD_TOKEN)

