# main.py
import discord
from discord.ext import commands
import datetime
import asyncio

intents = discord.Intents.all()
client = commands.Bot(command_prefix='.', intents=intents)

class Stats(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def age(self, ctx):
        guild = ctx.guild
        created_at = guild.created_at
        now = datetime.datetime.now(datetime.timezone.utc)
        days_since_creation = (now - created_at).days
        await ctx.send(f"This server was created {days_since_creation} days ago.")

    @commands.command()
    async def active(self, ctx):
        guild = ctx.guild
        now = datetime.datetime.now(datetime.timezone.utc)
        days_active = (now - guild.me.joined_at).days
        await ctx.send(f"I have been active in this server for {days_active} days.")

    @commands.command()
    async def members(self, ctx):
        guild = ctx.guild
        members = '\n'.join([member.name for member in guild.members])
        await ctx.send(f"Members in this server:\n{members}")

    @commands.command()
    async def bots(self, ctx):
        guild = ctx.guild
        bots = '\n'.join([member.name for member in guild.members if member.bot])
        await ctx.send(f"Bots in this server:\n{bots}")

    @commands.command()
    async def member_stats(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author

        roles = ', '.join([role.name for role in member.roles])
        embed = discord.Embed(title=f"{member.name}'s Stats", color=discord.Color.blue())
        embed.add_field(name="Name", value=member.name, inline=True)
        embed.add_field(name="Username", value=member.display_name, inline=True)
        embed.add_field(name="Roles", value=roles, inline=False)

        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(Stats(client))

async def main():
    await setup(client)
    TOKEN = "your-token-here"
    await client.start(TOKEN)

asyncio.run(main())