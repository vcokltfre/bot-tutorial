from discord.ext import commands

bot = commands.Bot(command_prefix="!")

bot.load_extension("somecommands") # Note, we don't need the .py file extension

bot.run("your_token_here")