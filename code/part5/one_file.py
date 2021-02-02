from discord.ext import commands

bot = commands.Bot(command_prefix="!")


class SomeCommands(commands.Cog):
    """A couple of simple commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        """Get the bot's current websocket latency"""
        await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")


bot.add_cog(SomeCommands(bot))

bot.run("your_token_here")
