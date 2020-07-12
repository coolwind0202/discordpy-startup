import asyncio
import discord
import sys
import signal
import time

TOKEN = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

loop = asyncio.get_event_loop()

    
def handler(signum,frame):
    print("SIGTERM received")

    
signal.signal(signal.SIGTERM,handler)
client.run(TOKEN)

while True:
    time.sleep(1)
    print("sleeping...")
