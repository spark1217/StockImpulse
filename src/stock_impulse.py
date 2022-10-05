"""
stock_impulse.py is responsible for setting up the discord bot for use.
Responsibilities include getting the necessary tokens, settings the bot's prefix
and intents, and starting the bot.
"""

import discord
from discord.ext import commands
import finnhub
import config
import json
import requests

# tokens
DISCORD_TOKEN = config.tokens['discord_token']
"""Discord API Token"""
FINNHUB_TOKEN = config.tokens['finnhub_token']
"""FinnHub API Token"""

# setup discord bot
client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# setup finnhub
finnhub_client = finnhub.Client(api_key=FINNHUB_TOKEN)

# print message when ready
@client.event
async def on_ready():
    """Prints a message when the bot comes online."""
    print(f'Logged in {client}')

@client.event
async def on_message(message):
    ''' run on message sent to a channel '''
    # allow messages from test bot
    if message.author.bot and message.author.id == 1027018277408477194:
        ctx = await client.get_context(message)
        await client.invoke(ctx)
    await client.process_commands(message)

@client.command(name='stock')
async def stock(ctx, stock_name):
    """Prints information regarding a given stock. This command is run by typing "!stock "stock"".
    The information is gotten through an API call to finnhub."""
    stock_info = finnhub_client.quote(stock_name)
    if all((v == 0) or (v is None) for v in stock_info.values()):
        await ctx.send(f'```Stock {stock_name} does not exist or has no value.```')
        return
    if stock_info["d"] >= 0:
        await ctx.send(f"""```{stock_name} Information
Current Price:    ${stock_info["c"]}
Change:           ${stock_info["d"]}
Percent Change:   {stock_info["dp"]}%
Daily High:       ${stock_info["h"]}
Daily Low:        ${stock_info["l"]}
Open Price:       ${stock_info["o"]}
Last Close Price: ${stock_info["pc"]}```""")
    else:
        await ctx.send(f"""```{stock_name} Information
Current Price:    ${stock_info["c"]}
Change:          -${abs(stock_info["d"])}
Percent Change:   {stock_info["dp"]}%
Daily High:       ${stock_info["h"]}
Daily Low:        ${stock_info["l"]}
Open Price:       ${stock_info["o"]}
Last Close Price: ${stock_info["pc"]}```""")

@client.command(name="price")
async def price(ctx, stock_name):
    """Prints the price of a given stock. This command is run by typing "!price "stock".
    The information is gotten through an API call to finnhub."""
    stock_info = finnhub_client.quote(stock_name)
    if all((v == 0) or (v is None) for v in stock_info.values()):
        await ctx.send(f'```Stock {stock_name} does not exist or has no value.```')
        return
    await ctx.send(f'```{stock_name} is currently ${stock_info["c"]}```')

@client.command(name="crypto")
async def crypto(ctx, crypto_name):
    key = "https://api.binance.com/api/v3/ticker/price?symbol=" + crypto_name + "USDT"
    data = requests.get(key)  
    data = data.json()
    cprice =  round(float(data['price']), 3)
    await ctx.send(f"```{data['symbol']} price is ${cprice}```")
# Example stock output
# https://github.com/Finnhub-Stock-API/finnhub-python
#res = finnhub_client.stock_candles('AAPL', 'D', 1590988249, 1591852249)
#print(res)

if __name__ == "__main__":
    client.run(DISCORD_TOKEN)

#---------------------------------------------------------#
# Everything below this line is for documentation purposes
# and does not perform any function.
#---------------------------------------------------------#
async def price_command(ctx, stock_name):
    """Prints the price of a given stock. This command is run by typing "!price "stock"".
    The information is gotten through an API call to finnhub."""
    stock_info = finnhub_client.quote(stock_name)
    if all((v == 0) or (v is None) for v in stock_info.values()):
        await ctx.send(f'```Stock {stock_name} does not exist or has no value.```')
        return
    await ctx.send(f'```{stock_name} is currently ${stock_info["c"]}```')

async def stock_command(ctx, stock_name):
    """Prints information regarding a given stock. This command is run by typing "!stock "stock"".
     The information is gotten through an API call to finnhub."""
    stock_info = finnhub_client.quote(stock_name)
    if all((v == 0) or (v is None) for v in stock_info.values()):
        await ctx.send(f'```Stock {stock_name} does not exist or has no value.```')
        return
    if stock_info["d"] >= 0:
        await ctx.send(f"""```{stock_name} Information
Current Price:    ${stock_info["c"]}
Change:           ${stock_info["d"]}
Percent Change:   {stock_info["dp"]}%
Daily High:       ${stock_info["h"]}
Daily Low:        ${stock_info["l"]}
Open Price:       ${stock_info["o"]}
Last Close Price: ${stock_info["pc"]}```""")
    else:
        await ctx.send(f"""```{stock_name} Information
Current Price:    ${stock_info["c"]}
Change:          -${abs(stock_info["d"])}
Percent Change:   {stock_info["dp"]}%
Daily High:       ${stock_info["h"]}
Daily Low:        ${stock_info["l"]}
Open Price:       ${stock_info["o"]}
Last Close Price: ${stock_info["pc"]}```""")
