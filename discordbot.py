import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
token = os.environ['DISCORD_BOT_TOKEN']

@bot.command(aliases=["connect","summon"])
async def join(ctx):
    """Botをボイスチャンネルに入室させます。"""
    channel = ctx.author.voice.channel
    if not channel:
        await ctx.send("先にボイスチャンネルに入っている必要があります。")
        return

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

    file = ctx.message.attachments[0]
    buffer = await file.read()
    ffmpeg_audio_source = discord.FFmpegPCMAudio(buffer)
    
    voice_client.play(ffmpeg_audio_source)
bot.run(token)
