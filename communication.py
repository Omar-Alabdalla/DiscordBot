import os
import nextcord
from nextcord.ext import commands

poker = '<@&900387751885680640>'
whitelist = [737859220552286229]


class communication(commands.Cog, name="Communication"):
    def __init__(self, client):
        self.client = client

    #@commands.command(pass_context=True)
    #async def vr(self, ctx):

    @commands.command(pass_context=True)
    async def pingpoker(self, ctx):
        print(ctx.message.guild.id)
        print(type(ctx.message.guild.id))
        if ctx.message.guild.id == 737859220552286229:
            await ctx.reply(poker)
        else:
            await ctx.reply("You're not allowed to use this command on this server")
            print(ctx.message.guild.id)

    @commands.command()
    async def hello(self, ctx):
        await ctx.reply('Hello! :monkey:')

    # @commands.command()
    # async def abhi(self, ctx):
    #    await ctx.reply('<@439614911371411456>')

    @commands.command()
    async def shutup(self, ctx, person: nextcord.Member):
        await ctx.channel.send(f'https://youtu.be/hEqv_tdZpuc {person.mention}')

    @commands.command()
    async def china(self, ctx):
        await ctx.reply('Down with the CCP!')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(ctx.message.guild.default_role)


def setup(client):
    client.add_cog(communication(client))
