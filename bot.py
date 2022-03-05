import json
import os
import discord
from discord.ext import tasks, commands
from checker import CheckTwitch

# Get the config
with open("config.json", "r") as config:
    data = json.load(config)
    token = data["token"]

bot = commands.Bot()

@tasks.loop(seconds=10)
async def check():
    channel = bot.get_channel(948168949323923488)
    name = "Lyubaw"
    result = await CheckTwitch.check_streamer(CheckTwitch, name)
    if result is not None:
        message = f"@everyone {name} est en live ! https://twitch.tv/{name}\n{result[0]} : {result[1]}"
        await channel.send(message)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print(f"Pycord v{discord.__version__}")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="Lyubaw's twitch"))
    check.start()

bot.run(token)

