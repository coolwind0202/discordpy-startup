import asyncio
import discord
import sys
import os
import signal
import time
import atexit

signal.signal(signal.SIGTERM,lambda signum, frame:print("signal"))

@atexit.register
def func():
    print("atexit")

time.sleep(1000)
