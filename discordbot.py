import asyncio
import discord
import sys

token = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

loop = asyncio.get_event_loop()

def handler(signum,frame):
    print("SIGTERM received")
    client.close()
    
loop.add_signal_handler(signal.SIGTERM,handler)
loop.run_until_complete(client.start(TOKEN))
