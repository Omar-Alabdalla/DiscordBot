import nextcord
from nextcord.ext import commands

poker = '<@&900387751885680640>'
whitelist = [737859220552286229]


class communication(commands.Cog, name="Communication"):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def hello(self, ctx):
        await ctx.reply('Hello!')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(ctx.message.guild.default_role)


def setup(client):
    client.add_cog(communication(client))
