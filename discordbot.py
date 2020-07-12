import asyncio
import discord
import sys
import os
import signal
import time

TOKEN = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

loop = asyncio.get_event_loop()

    
def handler(signum,frame):
    print("SIGTERM received")

    
signal.signal(signal.SIGTERM,handler)

def run():
    future = asyncio.ensure_future(client.start(TOKEN), loop=loop)
    future.add_done_callback(lambda:loop.stop())
    #loop.run_until_complete(client.start(TOKEN))
    loop.run_forever()
    
run()
print("ran")
