from discord.ext import commands # Again, we need this imported


class SomeCommands(commands.Cog):
    """A couple of simple commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        """Get the bot's current websocket latency"""
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")


# Now, we need to set up this cog somehow, and we do that by making a setup function:
def setup(bot: commands.Bot):
    bot.add_cog(SomeCommands(bot))