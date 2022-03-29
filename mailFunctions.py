from nextcord.ext import commands
from nextcord import embeds
import basicMail


class mailFunctions(commands.Cog, name="Email Functions"):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def mail(self, ctx, email, *message):
        await ctx.reply(basicMail.sendMail(email, message))

    # for attachment in ctx.message.attachments:
    # await attachment.save(attachment.filename)

    @commands.command()
    async def mailFile(self, ctx, rmail, a=None):
        # received if else statement from stackoverflow: https://stackoverflow.com/questions/65169339/download-csv-file-sent-by-user-discord-py
        for attachment in ctx.message.attachments:
            await attachment.save(attachment.filename)
            a = attachment.filename
        basicMail.sendFileMail(rmail, a)


def setup(client):
    client.add_cog(mailFunctions(client))
