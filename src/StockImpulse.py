import discord
from discord.ext import commands
import finnhub
import config

# tokens
DISCORD_TOKEN = config.tokens['discord_token']
FINNHUB_TOKEN = config.tokens['finnhub_token']

client = commands.Bot(command_prefix='!', intents=discord.Intents.all()) #discord.Client(intents=discord.Intents.all())

# setup finnhub
finnhub_client = finnhub.Client(api_key=FINNHUB_TOKEN)

# print message when ready
@client.event
async def on_ready():
    print('Logged in {0.user}'.format(client))

@client.command(name='stock')
async def stock(ctx, stock):
    stockInfo = finnhub_client.quote(stock)
    if all((v == 0) or (v == None) for v in stockInfo.values()):
        await ctx.send(f'```Stock {stock} does not exist or has no value.```')
        return
    if (stockInfo["d"] >= 0):
        await ctx.send(f"""```{stock} Information
Current Price:    ${stockInfo["c"]}
Change:           ${stockInfo["d"]}
Percent Change:   {stockInfo["dp"]}%
Daily High:       ${stockInfo["h"]}
Daily Low:        ${stockInfo["l"]}
Open Price:       ${stockInfo["o"]}
Last Close Price: ${stockInfo["pc"]}```""")
    else:
        await ctx.send(f"""```{stock} Information
Current Price:    ${stockInfo["c"]}
Change:          -${abs(stockInfo["d"])}
Percent Change:   {stockInfo["dp"]}%
Daily High:       ${stockInfo["h"]}
Daily Low:        ${stockInfo["l"]}
Open Price:       ${stockInfo["o"]}
Last Close Price: ${stockInfo["pc"]}```""")

@client.command(name="price")
async def price(ctx, stock):
    stockInfo = finnhub_client.quote(stock)
    if all((v == 0) or (v == None) for v in stockInfo.values()):
        await ctx.send(f'```Stock {stock} does not exist or has no value.```')
        return
    await ctx.send(f'```{stock} is currently ${stockInfo["c"]}```')


@client.event
async def on_message(message):    
    if message.author == client.user:
        return

    await client.process_commands(message) # Process commands first (REQUIRED)
    
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    if not (isinstance(message.channel, discord.DMChannel)):
        channel = str(message.channel.name) # Crashes if message is a DM
    else:
        channel = str('DMChannel')
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if channel == 'bot-testing':
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

