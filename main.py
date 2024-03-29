import json
import Token
# from keep_alive import keep_alive
# from pretty_help import DefaultMenu, PrettyHelp  # https://github.com/stroupbslayen/discord-pretty-help

import asyncio

import nextcord
from nextcord.ext import commands

import math1
import music
import weather
import mailFunctions

intents = nextcord.Intents.default()
intents.message_content = True

lst = []
mail = [mailFunctions]
music = [music]
weather = [weather]
math1 = [math1]

bot = commands.Bot(command_prefix=['idk ', 'iDk ', 'idK ', 'Idk ', 'IDk ', 'IdK ', 'IDK ', 'iDK '],
                   case_insensitive=True, intents=intents)

for i in range(len(mail)):
    mail[i].setup(bot)

for i in range(len(music)):
    music[i].setup(bot)

for i in range(len(weather)):
    weather[i].setup(bot)

for i in range(len(math1)):
    math1[i].setup(bot)


@bot.event
async def on_ready():
    print('Client Ready')


@bot.command(hidden=True)
async def spam(ctx):
    f = True
    while f is True:
        await ctx.send("HAHA")
        await asyncio.sleep(86400)


# https://youtu.be/V1bFr2SWP1I
class MyHelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        e = nextcord.Embed(color=nextcord.Color.blue(), description='')
        for page in self.paginator.pages:
            e.description += page
        await destination.send(embed=e)


bot.help_command = MyHelpCommand()
# The color can be whatever you want, including normal color codes,
# I just like the discord green personally.
# keep_alive()
bot.run(Token.discordToken())
