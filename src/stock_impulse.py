"""
stock_impulse.py is responsible for setting up the discord bot for use.
Responsibilities include getting the necessary tokens, settings the bot's prefix
and intents, and starting the bot.
"""

import discord
from discord.ext import commands
import config
import stocks
import cryptos



# tokens
DISCORD_TOKEN = config.tokens['discord_token']
"""Discord API Token"""

# setup discord bot
client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

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
    try:
        stock_info = stocks.get_stock_info(stock_name)
    except NameError as exception:
        await ctx.send(str(exception))
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
    The information is gotten through an API call to FinnHub."""
    try:
        stock_info = stocks.get_stock_info(stock_name)
    except NameError as exception:
        await ctx.send(str(exception))
        return
    await ctx.send(f'```{stock_name} is currently ${stock_info["c"]}```')

@client.command(name="crypto")
async def crypto(ctx, crypto_name):
    """Prints the current value of the given crypto currency. This command is run by
    typing !crypto "crypto". The information is gotten from binance."""
    try:
        data = cryptos.get_crypto_info(crypto_name)
    except NameError as exception:
        await ctx.send(str(exception))
        return
    cprice =  round(float(data['price']), 3)
    await ctx.send(f"```{data['symbol']} price is ${cprice}```")
# Example stock output
# https://github.com/Finnhub-Stock-API/finnhub-python
#res = finnhub_client.stock_candles('AAPL', 'D', 1590988249, 1591852249)
#print(res)

@client.command(name="info")
async def info(ctx):
    """Prints the information of how to use different commands."""

    inf = "The following commands can be used to access the bot.\n\n'!price' followed by the stock ticker will give you the current price of that stock. For example '!price META' will return the current stock price of Facebook stock\n\n'!stock' followed by the stock ticker will give you detailed information of that stock. For example '!stock IBM' will return info of IBM stock.\n\n'!crypto' followed by the crypto ticker will return that information. For example '!crypto ETH' will return info of Ethereum.\n\n'!info' is this command. A bit self explanatory :)"

    await ctx.send(f"```Info: {inf}```")

if __name__ == "__main__":
    client.run(DISCORD_TOKEN)

#---------------------------------------------------------#
# Everything below this line is for documentation purposes
# and does not perform any function.
#---------------------------------------------------------#

async def stock_command(ctx, stock_name):
    """Prints information regarding a given stock. This command is run by typing "!stock "stock"".
    The information is gotten through an API call to finnhub."""
    try:
        stock_info = stocks.get_stock_info(stock_name)
    except NameError as exception:
        await ctx.send(str(exception))
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

async def price_command(ctx, stock_name):
    """Prints the price of a given stock. This command is run by typing "!price "stock".
    The information is gotten through an API call to FinnHub."""
    try:
        stock_info = stocks.get_stock_info(stock_name)
    except NameError as exception:
        await ctx.send(str(exception))
        return
    await ctx.send(f'```{stock_name} is currently ${stock_info["c"]}```')

async def crypto_command(ctx, crypto_name):
    """Prints the current value of the given crypto currency. This command is run by
    typing !crypto "crypto". The information is gotten from binance."""
    try:
        data = cryptos.get_crypto_info(crypto_name)
    except NameError as exception:
        await ctx.send(str(exception))
        return
    cprice =  round(float(data['price']), 3)
    await ctx.send(f"```{data['symbol']} price is ${cprice}```")
