import discord
import asyncio
import openpyxl
import os

client = discord.Client()

@client.event
async def on_ready():
    print('온')
    print('------')
    game = discord.Game("!명령어 l 제작중")
    await client.change_presence(status=discord.Status.online , activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("!명령어"):
        await message.channel.send(embed=discord.Embed(title="제작중", description= "\n\n\n차후추가예정", color=0x00ff00))


client.run('NTk3NzI1OTU0MzY1NzE4NTI5.XSMXBA.Q5iVr_ykyrQJvdgoALXh65FgHL4')
