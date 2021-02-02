import discord
from discord.ext import commands # Again, we need this imported


class SomeCommands(commands.Cog):
    """A couple of simple commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        """Get the bot's current websocket latency"""
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

    @commands.command(name="setstatus")
    async def setstatus(self, ctx: commands.Context, *, text: str):
        """Set the bot's status"""
        await self.bot.change_presence(activity=discord.Game(text))

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel = self.bot.get_channel(799309066202775624)
        await channel.send(f"Welcome, {member}!")


# Now, we need to set up this cog somehow, and we do that by making a setup function:
def setup(bot: commands.Bot):
    bot.add_cog(SomeCommands(bot))
