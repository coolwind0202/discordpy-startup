import asyncio
import discord
import sys
import signal

TOKEN = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

loop = asyncio.get_event_loop()

def handler():
    print("SIGTERM received 1")
    #loop.stop()

def handler_2():
    print("SIGTERM received 2")
    
def handler_3(signum,frame):
    print("SIGTERM received 3")

    
loop.add_signal_handler(signal.SIGTERM,handler)
loop.add_signal_handler(signal.SIGTERM,handler_2)
signal.signal(signal.SIGTERM,handler_3)
loop.run_until_complete(client.start(TOKEN))
