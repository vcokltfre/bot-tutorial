from discord.ext import commands # This is the part of discord.py that helps us build bots

bot = commands.Bot(command_prefix="!")

@bot.command(name="hello")
async def hello_world(ctx: commands.Context):
    await ctx.send("Hello, world!")

bot.run("your_token_here")