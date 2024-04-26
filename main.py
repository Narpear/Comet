# main.py
import discord
from discord.ext import commands
import music

intents = discord.Intents.all()
client = commands.Bot(command_prefix='.', intents=intents)

cogs = [music]

for i in range(len(cogs)):
    cogs[i].setup(client)


client.run("MTIzMzM1MTg3OTAwNjYyMTcyNw.GigoWx.ncdpWj2v3r-UKWnRYMC06xS9RSutA4Pni-bSYk")