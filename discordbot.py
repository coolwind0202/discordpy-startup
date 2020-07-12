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

def handler(signum, flame):
    print(f"received SIGTERM")
signal.signal(signal.SIGTERM,handler)    

@atexit.register
def goodbye():
    print("exit")
    
print("Hello world")

loop = asyncio.get_event_loop()
loop.create_task(bot.start(token))

#time.sleep(1000)
