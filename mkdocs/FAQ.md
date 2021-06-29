## Where to download??!1?

We have a downloads page on our website that's almost as majestic as my beard ![Billy's Majestic Beard](https://cdn.discordapp.com/emojis/768978823655063602.png?size=16). It is our user friendly front-end for our downloads api: https://purpur.pl3x.net/downloads/

If you'd rather use the downloads api directly (for automation, scripts, or whatever) you can find the api endpoints listed on [the home page](https://purpur.pl3x.net/docs/#Downloads).

## Can I make a feature request or report a bug?

Of course you can! That's what makes Purpur better and better ^_^

If you need to report a bug, please let us know about it. Remember, we can't fix what we don't know is broke :wink:

Bug Reports: https://github.com/pl3xgaming/Purpur/issues/new

If you have a feature request or suggestion, please keep in mind that we try to stay away from niche features that may only help 1 or 2 servers. Things like that are best suited to plugins or datapacks. If you are unsure, open a ticket anyways and we'll let you know \o/

Feature Request: https://github.com/pl3xgaming/Purpur/discussions/new

## Purpur has permissions? :open_mouth:

Yes.

Purpur adds a few permissions for a few features and commands that have been added. Some permissions for specific features will not work unless that feature is enabled in purpur.yml, too, so keep an eye out for those :wink:

https://purpur.pl3x.net/docs/Permissions

## What does *&lt;insert random config option>* do?

Stuff.

No seriously, we get asked this quite a lot. We built this wiki to answer all these questions so we wouldn't have to repeat them daily.

I promise, this wiki covers every single option in purpur.yml - you wont find any missing entries. (the only exception is when a new option gets added; it might take a day or two before it's updated)

https://purpur.pl3x.net/docs/Configuration

## Does Purpur have a Discord?

Yes! It's where the purpur community resides. Don't be afraid to poke your head in and take a peek! https://purpur.pl3x.net/discord

## What does Purpur add/change from upstream?

Quite a lot, actually. But none of it goes into effect unless **you** enable it in `purpur.yml`. Everything we change is set to the default behaviors. If you don't edit anything in `purpur.yml`, running this jar is no different than running Tuinity.

For the curious, you can view all the code changes on github here: https://github.com/pl3xgaming/Purpur/tree/master/patches

Don't worry if you can't read code. Most people can't. We have this nice wiki that covers every single option in `purpur.yml` and all the new permission nodes added for some new features/commands.

## Does Purpur have feature *X* from Paper/Tuinity?

Yes, Thats how forks work. All features from upstream are inherited by design

`Vanilla -> CraftBukkit -> Spigot -> Paper -> Tuinity -> Purpur`

We have it all ^_^

## Do CraftBukkit/Spigot/Paper plugins work on Purpur?

Yes. The only time there's incompatibilities is due to authors hard-coding support for craftbukkit/spigot, ignoring the existence of Paper and it's forks. If you run into any bugs that you know are because of Purpur, [create a ticket](https://github.com/pl3xgaming/Purpur/issues/new) and/or [join our discord server](https://purpur.pl3x.net/discord) so we can take a look.

## Why isn't Purpur a direct fork of Tuinity? Why are all of Tuinity's patches squashed into 1 patch?

Because Tuinity doesn't merge upstream Paper nearly as often as I would prefer. Doing it this way allows me to upstream merge Paper's patches before Tuinity does. \o/

## Is there a Purpur for MC insert _`random version here`_?
Maybe. Check the downloads page.

https://purpur.pl3x.net/downloads

## My server is lagging and I don't understand my timings report!? Can you read it for me and tell me what to fix?

At the top right of your timings report is a link to a video tutorial that will teach you how to read and understand your timings report. I highly advise giving that a watch before reaching out to others for help. I understand its long (45 minutes?!) but its got a lot of good information in it and it really will help you more in the long run.

For those that are impatient and just want quick fixes, the good people over at [![Birdflop Emote](https://cdn.discordapp.com/emojis/799601349095587840.png?size=16) Birdflop Hosting](https://discord.com/invite/nmgtX5z) have made a nice bot that can analyze your timings report and recommend the most common community recommended optimization changes to boost your performance. Head on over to their Discord Server and paste your timings link in their `#bot` channel to have their bot scan it. Here is the invite: https://discord.com/invite/nmgtX5z

Some people may want to know what all of these options the bot is recommending you change actually do. Well, my friend, you're in luck \o/ There is a nice community written optimization guide that's been compiled with a ton of information over these performance related options, including what they do and what are some good starting points to use for your own server. The Birdflop bot gets most of its information from this guide, too. Just remember, these are starting points, not the golden rule. Be sure you understand what each option does before you change them, or you might end up surprised later with your server doing something you didnt expect or don't want. That guide is here: https://github.com/YouHaveTrouble/minecraft-optimization
