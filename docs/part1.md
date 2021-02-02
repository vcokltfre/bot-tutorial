# Part 1 - Creating a Bot User

The first step of creating your own bot is creating the user itself. To do this you first have to go to the [Discord Developer Portal](https://discord.com/developers) where you'll be asked to login to your Discord account. Once logged in you should see a screen like this:

![Discord Developer Portal](https://github.com/vcokltfre/bot-tutorial/raw/master/images/dev_portal_1.png "Discord Developer Portal")

Now that you're here you can create an application. To do this you just need to click the `New Application` button in the top right hand corner of the screen - note that you will need to have verified your email address to create an application. After doing that You'll see a screen like this:

![Create an Application"](https://github.com/vcokltfre/bot-tutorial/raw/master/images/dev_portal_2.png "Create an Application")

Be sure to enter a suitable name for your bot - make sure to follow the Discord terms of service, so no slurs or harassment. To be clear, this applies throughout this tutorial also, and you should make sure to follow the [Terms of Service](https://dis.gd/terms) and [Developer Terms](https://discord.com/developers/docs/legal) when creating your bot. Notably that means things like:

- Not abusing the API.
- Not harassing users.
  - This means don't DM users randomly, or spam them.
- Not spamming Discord.
  - Generally, actions performed by your bot should be a result of a user action, be this running a command, deleting a message, etc.
- Not posting NSFW content in channels not marked as NSFW.
  - This may seem obvious but a lot of bots allow NSFW content to be posted outside of NSFW channels. This is not allowed.

For this tutorial, the bot will be called `WumpusBot`, and that's what it will be referred to as for the duration of the tutorial.

Now that you've created your application, you'll see a screen like this:

![General Information](https://github.com/vcokltfre/bot-tutorial/raw/master/images/dev_portal_3.png "General Information")

Although there is quite a lot on this screen, it's out of scope for the beginning of this tutorial, so for now we'll ignore it and move to the `Bot` tab on the left hand side, marked by a jigsaw piece. If you click this tab you'll see a screen asking you to create a new bot. When you click this you'll be prompted if you want to continue because you wont be able to delete the bot after (because bots are too cool to destroy, of course!). Click yes and you'll be taken to a screen that looks like this:

![Bot](https://github.com/vcokltfre/bot-tutorial/raw/master/images/dev_portal_4.png "Bot")

Now you'll see a button that says `Copy` just under the username box. This button copies your bot's token to your clipboard, make sure to keep this safe, you'll need it to connect with Discord later in the tutorial.

Finally for this part, you need to add your bot to your server. To do this you first require the Manage Server permission in whatever server you plan on adding it to. You'll want to head over to the OAuth2 tab on the left of the developer portal, marked by a wrench, where you'll be able to choose the scopes you want for your bot. For now, just select the bot scope, as it's all that will be needed for this tutorial - at least at the beginning.

Now you'll want to choose permissions for your bot based on what you want it to do. For WumpusBot, I'll start by giving it Send Messages, Embed Links, Attach Files, Manage Messages, and Add Reactions, although we may need more permissions later, but that will be handled within Discord itself. It is **highly recommended that you never give bots the `Administrator` permission, even if it feels easier than giving the bot just what's needed. Please do not give your bots administrator.** In the end your permissions should look something like this:

![Bot Permissions](https://github.com/vcokltfre/bot-tutorial/raw/master/images/dev_portal_5.png "Bot Permissions")

Finally, you can copy the URL that the box above gives you and paste it into your browser, then follow the steps to add the bot to your server of choice.

That's it! You've created your very own bot user on Discord. Now you just have to do the fun bit - creating functionality, after all, what's a bot without commands or functionality?

Please read the note below, and then you can move onto [Part 2 - An Overview of Discord.](./part2.md)

### A quick note on tokens:

You should make an effort to keep your token safe at all times. This means not sharing it with anyone or accidentally uploading it in code samples. If someone gains access to your bot's token they then have full control of the bot, and can perform actions with it that you may not want. If you believe that your bot's token was leaked, be sure to go to it's developer portal page and click the `Regenerate` button to regenerate the token so that nobody can use the old one.