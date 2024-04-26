import discord
from discord.ext import commands
import music

cogs = [music]
client = commands.Bot(command_prefix='.', intents=discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)

client.run(
    "MTIzMzM1MTg3OTAwNjYyMTcyNw.GigoWx.ncdpWj2v3r-UKWnRYMC06xS9RSutA4Pni-bSYk")
