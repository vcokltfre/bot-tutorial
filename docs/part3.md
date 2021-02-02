# Part 3 - Hello, World!

In this part, I'll show you the basics of how to create a super simple bot and get it connected to Discord. From now on it is assume that you have the [discord.py](https://pypi.org/project/discord.py/) library installed, along with a version of Python later than 3.6.

---

The first step to creating a bot is to import the Bot class so that we can create the bot.

```py
from discord.ext import commands # This is the part of discord.py that helps us build bots
```

Epic! Now we can use the discord.ext.commands module, we need to actually create a bot instance that will run our commands:

```py
bot = commands.Bot(command_prefix="!")
```

As you can see, the first thing we need to do is tell the bot which command prefix to use, else how can it respond to commands? This prefix can actually be one of many things, but for the sake of this tutorial I'll just be using the string `"!"` for the prefix. Just know that it is possible to create more complex prefixes, such as a different prefix for each server.

While creating the bot is also where we would specify what are known as gateway intents - essentially telling the gateway which events we want. For now we'll ignore this, however it will be covered later in the tutorial when we need to use events not given with the defaukt intents.

Next, we want to add a command to the bot so that it can do something. The first command we'll add is a !hello command, that responds with "Hello, world!"

```py
@bot.command(name="hello")
async def hello_world(ctx: commands.Context):
    await ctx.send("Hello, world!")
```

That's quite a lot to take in, even if you're quite familiar with Python, so allow me to explain what each piece of it does:

- `@bot.command(name="hello")` is a decorator that converts the function below it into a command that you can run from Discord.
- `async def hello_world(ctx: commands.Context):` defines a hello_world function that takes 1 argument - ctx - which is a Context object that's passed with **every** command. All commands will be passed a Context object as their first argument.
- `await ctx.send("Hello, world!")` makes an API call to Discord to send a message to the channel the command was run in with the content "Hello, world!"

Next, we need to run the bot with ts token that you got from the developer portal in [part 1](./part1.md):

```py
bot.run("your_token_here")
```

This runs the bot with your token, and asbtracts away creating an event loop and running the bot through coroutines.

At this point, your bot should be entirely functional, and if you start it up in your preferred method, you should see it come online and answer commands.

![Hello World](https://github.com/vcokltfre/bot-tutorial/raw/master/images/hello_world.png "Hello World")

Now that you've got the basic bot running, you're ready to move onto [Part 4 - A Ping Command](./part4.md), or you can take a [look at the full code for this part.](../code/part3.py)