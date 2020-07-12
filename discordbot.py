import discord
from discord.ext import commands

import os
import io
import asyncio
improt time

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

#bot.run(token)
