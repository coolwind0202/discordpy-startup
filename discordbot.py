import discord
from discord.ext import commands

import os
import io
import asyncio
import time

import signal
import atexit

bot = commands.Bot(command_prefix="$")
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_ready():
    print("ready...")

    
print("Hello world")

def handler(signum, frame):
    print(f"received SIGTERM")
signal.signal(signal.SIGTERM,handler)    

@atexit.register
def goodbye():
    print("exit")

loop = asyncio.get_event_loop()
loop.run_until_complete(bot.start(token))
print("end.")
#time.sleep(1000)
