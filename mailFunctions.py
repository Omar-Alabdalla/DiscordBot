from nextcord.ext import commands
import mail
import basicMail


class mailFunctions(commands.Cog, name="Email Functions"):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def mail(self, ctx, email, *message):
        await ctx.reply(basicMail.sendMail(email, message))
