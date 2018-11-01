import discord
import json
import os
import youtube_dl
from discord.ext import commands



client = commands.Bot(command_prefix="+")

@client.event
async def  on_ready():
    print("Reddy Freddy.")

@client.event
async def is_nsfw(channel: discord.Channel):
    try:
        _gid = channel.server.id
    except AttributeError:
        return False
    data = await client.http.request(
        discord.http.Route(
            'GET', '/guilds/{guild_id}/channels', guild_id=_gid))
    channeldata = [d for d in data if d['id'] == channel.id][0]
    return channeldata['nsfw']

client.run(os.environ['TOKEN'])
