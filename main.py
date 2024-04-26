# main.py
import discord
from discord.ext import commands
import datetime
import asyncio
import time

intents = discord.Intents.all()
client = commands.Bot(command_prefix='.', intents=intents)

start_time = time.time()

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

    @commands.command()
    async def uptime(self, ctx):
        current_time = time.time()
        uptime_seconds = int(current_time - start_time)
        uptime_string = str(datetime.timedelta(seconds=uptime_seconds))
        await ctx.send(f"I have been online for {uptime_string}")

    @commands.command()
    async def ping(self, ctx):
        latency = self.client.latency * 1000
        await ctx.send(f"Pong! Latency is {latency:.2f} ms")

    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        avatar_url = member.avatar_url
        embed = discord.Embed(title=f"{member.name}'s Avatar")
        embed.set_image(url=avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def server_info(self, ctx):
        guild = ctx.guild
        embed = discord.Embed(title=guild.name, color=discord.Color.blue())
        embed.add_field(name="Owner", value=guild.owner.mention, inline=True)
        embed.add_field(name="Members", value=len(guild.members), inline=True)
        embed.add_field(name="Created On", value=guild.created_at.strftime("%Y-%m-%d"), inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        if amount <= 0:
            await ctx.send("The amount of messages to delete must be a positive integer.")
            return
        elif amount > 100:
            await ctx.send("You cannot delete more than 100 messages at once.")
            return

        deleted = await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f"{len(deleted) - 1} messages have been deleted.", delete_after=0.01)

async def setup(client):
    await client.add_cog(Stats(client))

async def main():
    await setup(client)
    TOKEN = "token-here"
    await client.start(TOKEN)

asyncio.run(main())