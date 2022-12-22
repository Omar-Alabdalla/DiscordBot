import os
import Token
import requests
from nextcord.ext import commands


def get_temp(zipp):
    URL = f'http://api.openweathermap.org/data/2.5/weather?'
    params = {
        "zip": zipp,
        "units": "imperial",
        "appid": Token.TokenWeather()
    }
    r = requests.get(URL, params=params)
    print(URL, params)
    res = r.json()
    print(res)
    temp = res['main']['temp']
    return "The Temperature is " + str(temp)


def get_weather(zipp):
    appid = Token.TokenWeather()
    URL = f'http://api.openweathermap.org/data/2.5/weather?'
    params = {
        "zip": zipp,
        "units": "imperial",
        "appid": appid
    }
    r = requests.get(URL, params=params)
    print(URL, params)
    res = r.json()
    print(res)
    temp = res['main']['temp']
    return "The Temperature is " + str(temp)


class weather(commands.Cog, name="Weather"):
    def __init__(self, person):
        self.person = person

    @commands.command()
    async def temp(self, ctx, zipp):
        await ctx.reply(get_weather(zipp))


def setup(person):
    person.add_cog(weather(person))
