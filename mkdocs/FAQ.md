## Where to download??!1?

We have a downloads page on our website that's almost as majestic as my beard ![Billy's Majestic Beard](https://cdn.discordapp.com/emojis/768978823655063602.png?size=16). It is our user friendly front-end for our downloads API: {{ project.downloads }}

If you'd rather use the downloads API directly (for automation, scripts, or whatever) you can find the API endpoints listed on [the home page]({{ project.downloads }}).

## What are the best purpur options?

It's hard to summarize Purpur because then it wouldn't be fully representative of everything it can do.

Take a look at the [most liked features](https://www.reddit.com/r/admincraft/comments/pbx5le/what_is_your_favorite_purpur_feature/) poll over on reddit.  
But that list is hardly exhaustive, so do make sure to check out all the available options, there's something for everyone \o/  
{{ site_url }}/Configuration


## Can I make a feature request or report a bug?

Of course you can! That's what makes Purpur better and better ^_^

If you need to report a bug, please let us know about it. Remember, we can't fix what we don't know is broke :wink:

Bug Reports: {{ project.source }}/issues/new

If you have a feature request or suggestion, please keep in mind that we try to stay away from niche features that may only help 1 or 2 servers. Things like that are best suited to plugins or datapacks. If you are unsure, open a ticket anyways and we'll let you know \o/

Feature Request: {{ project.source }}/discussions/new

## Purpur has permissions? :open_mouth:

Yes.

Purpur adds a few permissions for a few features and commands that have been added. Some permissions for specific features will not work unless that feature is enabled in purpur.yml, too, so keep an eye out for those :wink:

{{ site_url }}/Permissions

## What does *&lt;insert random config option>* do?

Stuff.

No seriously, we get asked this quite a lot. We built this wiki to answer all these questions so we wouldn't have to repeat them daily.

I promise, this wiki covers every single option in purpur.yml - you wont find any missing entries. (the only exception is when a new option gets added; it might take a day or two before it's updated)

{{ site_url }}/Configuration

## Does Purpur have a Discord?

Yes! It's where the Purpur community resides. Don't be afraid to poke your head in and take a peek! {{ social[0].link }}

## What does Purpur add/change from upstream?

Quite a lot, actually. But none of it goes into effect unless **you** enable it in `purpur.yml`. Everything we change is set to the default behaviors. If you don't edit anything in `purpur.yml`, running this JAR is no different than running Pufferfish.

For the curious, you can view all the code changes on GitHub here: {{ project.source }}/tree/master/patches

Don't worry if you can't read code. Most people can't. We have this nice wiki that covers every single option in `purpur.yml` and all the new permission nodes added for some new features/commands.

## Does Purpur have feature *X* from Paper?

Yes, Thats how forks work. All features from upstream are inherited by design

`Vanilla -> CraftBukkit -> Spigot -> Paper -> Pufferfish -> Purpur`

We have it all ^_^

## Do CraftBukkit/Spigot/Paper/Pufferfish plugins work on Purpur?

Yes. The only time there's incompatibility is due to authors hard-coding support for CraftBukkit/Spigot, ignoring the existence of Paper and its forks. If you run into any bugs that you know are because of Purpur, [create a ticket]({{ project.source }}/issues/new) and/or [join our Discord server]({{ social[0].link }}) so we can take a look.

## Is there a Purpur for MC insert _`random version here`_?
Maybe. Check the downloads page.

{{ project.downloads }}
