import discord
from discord.ext import commands

import os
import io


bot = commands.Bot(command_prefix="$")
token = os.environ['DISCORD_BOT_TOKEN']

if not discord.opus.is_loaded():
    discord.opus.load_opus("heroku-buildpack-libopus")

@bot.command(aliases=["connect","summon"])
async def join(ctx):
    """Botをボイスチャンネルに入室させます。"""
    voice_state = ctx.author.voice
    
    if (not voice_state) or (not voice_state.channel):
        await ctx.send("先にボイスチャンネルに入っている必要があります。")
        return
    
    channel = voice_state.channel
    await channel.connect()
    print("connected to:",channel.name)


@bot.command(aliases=["disconnect","bye"])
async def leave(ctx):
    """Botをボイスチャンネルから切断します。"""
    voice_client = ctx.message.guild.voice_client

    if not voice_client:
        await ctx.send("Botはこのサーバーのボイスチャンネルに参加していません。")
        return

    await voice_client.disconnect()
    await ctx.send("ボイスチャンネルから切断しました。")


@bot.command()
async def play(ctx):
    """指定された音声ファイルを流します。"""
    voice_client = ctx.message.guild.voice_client

    if not voice_client:
        await ctx.send("Botはこのサーバーのボイスチャンネルに参加していません。")
        return

    if not ctx.message.attachments:
        await ctx.send("ファイルが添付されていません。")
        return

    tmp = await ctx.message.attachments[0].read()
    tmp = tmp.decode().replace("\0","").encode()
    
    ffmpeg_audio_source = discord.FFmpegPCMAudio(tmp)
    
    voice_client.play(ffmpeg_audio_source)
    
bot.run(token)
