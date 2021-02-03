import discord
from discord.ext import commands


class SomeCommands(commands.Cog):
    """A couple of simple commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.last_msg = None

    @commands.command(name="ping")
    @commands.cooldown(1, 5, commands.BucketType.channel)
    async def ping(self, ctx: commands.Context):
        """Get the bot's current websocket latency"""
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

    @commands.command(name="setstatus")
    async def setstatus(self, ctx: commands.Context, *, text: str):
        """Set the bot's status"""
        await self.bot.change_presence(activity=discord.Game(text))

    @commands.command(name="snipe")
    async def snipe(self, ctx: commands.Context):
        """A command to snipe deleted messages"""
        if self.last_msg is None:
            await ctx.send("There is no message to snipe!")
            return

        desc = self.last_msg.content
        embed = discord.Embed(title=f"Message from {self.last_msg.author}", description=desc)
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel = self.bot.get_channel(799309066202775624)
        await channel.send(f"Welcome, {member}!")

    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        self.last_msg = message

    @ping.error
    async def ping_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"This command is on cooldown, try again after {round(error.retry_after)} seconds.", delete_after=5)
        print(error)


def setup(bot: commands.Bot):
    bot.add_cog(SomeCommands(bot))
