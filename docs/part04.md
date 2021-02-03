# Part 4 - A Ping Command

So far we've made a pretty simple bot - it only responds to !hello with a static response. Not particularly interesting, is it? Let's fix that! In this part we'll be creating a ping command that shows the bot's gateway websocket latency when you call it.

As with the previous part we'll want to import and set up the bot like below:

```py
from discord.ext import commands # This is the part of discord.py that helps us build bots

bot = commands.Bot(command_prefix="!")

@bot.command(name="hello")
async def hello_world(ctx: commands.Context):
    await ctx.send("Hello, world!")

bot.run("your_token_here")
```

But now we want to add another command between the hello comamnd and where we run the bot. Note that if you put the command after running the bot it will never be called since running the bot creates an infinite loop.

The command will look like this:

```py
@bot.command(name="ping")
async def ping(ctx: commands.Context):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")
```

This will send a message that says something along the lines of "Pong! 113ms" which is the amount of time between discord&#46;py sending a gateway heartbeat and it receiving an acknowledgement from the gateway. In the response we're using an f-string (Python 3.6 and above) so that we can use inline code within the string, in this case the bot's latency is measured in seconds, but we want it in milliseconds, so we multiply it by 1000 and round it to remove the decimals.

It's that simple, you've added another command, go ahead and run the bot to try it out! If it works it should look like the following:

![Ping Pong](https://github.com/vcokltfre/bot-tutorial/raw/master/images/ping_pong.png "Ping Pong")

Well done! You're 4 parts in already, fortunately there's a lot more to learn! You can now move on to [Part 5 - Cogs](./part05.md), or you can take a [look at the full code for this part.](../code/part4.py)