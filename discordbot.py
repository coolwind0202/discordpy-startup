import asyncio
import discord
import sys
import os
import signal

TOKEN = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

loop = asyncio.get_event_loop()

def handler():
    print("SIGTERM received")
    loop.close()
    
loop.add_signal_handler(signal.SIGTERM,handler)
loop.run_until_complete(client.start(TOKEN))
