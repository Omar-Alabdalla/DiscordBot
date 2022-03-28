from nextcord.ext import commands
from nextcord import embeds
import basicMail


class mailFunctions(commands.Cog, name="Email Functions"):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def mail(self, ctx, email, *message):
        await ctx.reply(basicMail.sendMail(email, message))

    @commands.command()
    async def mailFile(self, ctx, *stuff):
        # received if else statement from stackoverflow: https://stackoverflow.com/questions/65169339/download-csv-file-sent-by-user-discord-py
        if str(ctx.attachments) == "[]":  # This checks if there is an attachment on the message
            return "You didn't include a file"
        else:
            await save("mailFile", False, False)
            basicMail.sendMail()


def setup(client):
    client.add_cog(mailFunctions(client))
