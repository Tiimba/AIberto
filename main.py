import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
        channel = client.get_channel(id=729391516384100437)

        await channel.send("Dedo lingua")

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome {member.mention} to {guild.name}!'
            await guild.system_channel.send(to_send)

client = MyClient(intents=intents)
client.run('OTYzODcyMjg4MjM3ODQ2NTM4.YlcaBQ.N17rBwV65QeQKkkOZBbarfKlNwo')
