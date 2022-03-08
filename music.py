import nextcord
from nextcord.ext import commands
import youtube_dl


class music(commands.Cog, name="Music"):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def play(self, ctx, url):
        if ctx.author.voice is None:
            await ctx.reply("You're not in a voice channel!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)
        ctx.voice_client.stop()
        ffmpegOptions = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                         'options': '-vn'}
        YDL_OPTIONS = {'format': "bestaudio"}
        vc = ctx.voice_client
        await ctx.reply(f'Now Playing {url}')
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await nextcord.FFmpegOpusAudio.from_probe(url2, **ffmpegOptions)
            vc.play(source)

    @commands.command()
    async def helikopter(self, ctx):
        if ctx.author.voice is None:
            await ctx.reply("You're not in a voice channel!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)
        ctx.voice_client.stop()
        ffmpegOptions = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                         'options': '-vn'}
        YDL_OPTIONS = {'format': "bestaudio"}
        vc = ctx.voice_client
        url = 'https://youtu.be/3ExGuHWdXCE'
        await ctx.reply(f'Now Playing {url}')
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await nextcord.FFmpegOpusAudio.from_probe(url2, **ffmpegOptions)
            vc.play(source)

    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()
        await ctx.send('Bye')

    @commands.command()
    async def stop(self, ctx):
        await ctx.voice_client.stop()
        await ctx.reply('Audio Stopped')

    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_client.pause()
        await ctx.send('Audio Paused')

    @commands.command()
    async def resume(self, ctx):
        await ctx.voice_client.resume()
        await ctx.send('Audio Resumed')


def setup(client):
    client.add_cog(music(client))
