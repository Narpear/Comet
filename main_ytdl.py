# main.py
import discord
from discord.ext import commands
import youtube_dl

intents = discord.Intents.all()
client = commands.Bot(command_prefix='.', intents=intents)

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("You're not in a voice channel!")
        else:
            voice_channel = ctx.author.voice.channel
            if ctx.voice_client is None:
                await voice_channel.connect()
            else:
                await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self, ctx, url):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format': "bestaudio"}
        vc = ctx.voice_client

        if not vc.is_connected():
            await ctx.send("I'm not connected to a voice channel.")
            return

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            print(f"Attempting to play: {url}")
            try:
                info = ydl.extract_info(url, download=False)
            except Exception as e:
                print(f"Error extracting info from URL: {e}")
                await ctx.send("An error occurred while trying to play the audio.")
                return

            url2 = info['formats'][0]['url']
            print(f"Extracted audio URL: {url2}")
            try:
                source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            except Exception as e:
                print(f"Error creating audio source: {e}")
                await ctx.send("An error occurred while trying to play the audio.")
                return

            vc.play(source)
            print("Playing audio...")

    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_client.pause()
        await ctx.send("Paused")

    @commands.command()
    async def resume(self, ctx):
        await ctx.voice_client.resume()
        await ctx.send("Resumed")

async def setup(client):
    await client.add_cog(Music(client))

async def main():
    await setup(client)

TOKEN = "MTIzMzM1MTg3OTAwNjYyMTcyNw.GigoWx.ncdpWj2v3r-UKWnRYMC06xS9RSutA4Pni-bSYk"

client.setup_hook = main
client.run(TOKEN)