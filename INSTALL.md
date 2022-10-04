# Installation Guide for StockImpulse
These are step by step instructions on how to start developing using our repository.
## Clone the Repository
1) Go to the [repository homepage](https://github.com/spark1217/StockImpulse)
2) Click on the code dropdown and copy the link
3) In Visual Studio Code install the "GitHub Pull Requests and Issues" extension and log into github
4) Press ```Ctrl + Shift + P```, type ```Git: Clone```, and paste the link
5) In the root directory of the project create a ```config.py``` file with the following content. Information on what your tokens are can be found below
```
tokens = {
    'discord_token': "YOUR DISCORD BOT TOKEN HERE",
    'finnhub_token': "YOUR FINNHUB API TOKEN HERE"
}
```

Alternatively for steps 2-4 you can run this code where you want the repository to be cloned ```git clone https://github.com/spark1217/StockImpulse```
  
## Create a Discord Bot
You will need to create your own discord bot in order to run the program.
1) If you do not already have a discord account you must create one [here](https://discord.com/register)
2) Enable developer mode on your discord account. This can be found by going to ```User Settings``` and then ```Advanced```
3) Go to the [discord developers page](https://discord.com/developers/applications). If you are working with a team go to ```Teams``` and create a new team with the discord accounts of all your team members
4) In ```Applications``` press ```New Application```. Name the bot ```StockImpulse``` and select your team if you are working with one. Accept the terms of service and press ```Create```
5) In the application you just created go to ```Bot``` and create a bot
6) The token you are given is what you should enter into the ```config.py``` file for the ```discord_token``` variable. If you are not given a token you can press ```Reset Token``` for a new one.
7) Scroll down and make sure your bot has access to all of the ```Privileged Gateway Intents```
8) Invite the discord bot to the server you want it in

## Get a FinnHub API Key
You will also need an API key for FinnHub to get stock information.
1) Go to the [FinnHub Homepage](https://finnhub.io/)
2) Choose to ```Get free API key```. You will need to create an account for this. You do not need to get the paid version for this bot
3) Put this key in the ```config.py``` file for the ```finnhub_token``` variable

## Install Required Dependencies
The bot relies on certain libraries to run. These can be easily installed by running ```pip install -r requirements.txt``` from inside the root of the project.
