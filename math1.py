from nextcord.ext import commands


class math1(commands.Cog, name="Math"):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def add(self, ctx, *nums):
        operation = " + ".join(nums)
        await ctx.reply(f"{operation} = {eval(operation)}")

    @commands.command()
    async def subtract(self, ctx, *nums):
        operation = " - ".join(nums)
        await ctx.reply(f"{operation} = {eval(operation)}")

    @commands.command()
    async def multiply(self, ctx, *nums):
        operation = " * ".join(nums)
        await ctx.reply(f"{operation} = {eval(operation)}")

    # @commands.command(hidden = True)
    @commands.command()
    async def divide(self, ctx, *nums):
        try:
            operation = " / ".join(nums)
            await ctx.reply(f"{operation} = {eval(operation)}")
        except SyntaxError:
            await ctx.reply("Your numbers can't start with a zero.")
        except ZeroDivisionError:
            await ctx.reply("Cannot divide by zero.")


def setup(client):
    client.add_cog(math1(client))
