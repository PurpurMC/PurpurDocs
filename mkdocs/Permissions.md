Purpur adds a few new permission nodes for some of its added features.

By default, Purpur disables **all** of these permissions, no matter if a user has OP. Servers will need a permissions plugin such as [LuckPerms](https://luckperms.net/) to grant permissions to users.

## allow.ride.<mob_id&gt;
Requires enabling [`<mob_id>.ridable`](../Configuration#mobs) in purpur.yml

- This permission gives the ability to ride a certain mob by shift
right-clicking it. Once mounted you can use WASD to move around, and spacebar to jump or fly. Just replace "<mob_id&gt;" with the mob's Entity ID.

- **examples**:
    - `allow.ride.cow`
    - `allow.ride.zombie_pigman`
    - `allow.ride.snow_golem`

## allow.special.<mob_id&gt;
Requires enabling [`<mob_id>.ridable`](../Configuration#mobs) in purpur.yml

- This permission gives the ability to activate a ridable mob's
special ability. Not all mobs have a special ability. Just replace "<mob_id&gt;" with
the mob's Entity ID.

- **Currently Available Specials
    - `allow.special.creeper`
        - Ignites when spacebar is pressed
    - `allow.special.dolphin`
        - Spits when spacebar is pressed
    - `allow.special.phantom`
        - Shoots flames when spacebar is pressed
    - `allow.special.wither`
        - Shoots a wither head on mouse click

## allow.powered.creeper
Requires enabling [`creeper.ridable`](../Configuration#creeper) in purpur.yml

- This permission gives the ability to toggle a creeper's powered state while riding.
Hold the spacebar while not moving to charge the toggle. Instead of blowing up the powered
state will toggle on or off.

## bukkit.command.uptime
- Allows the use of the [`/uptime`](../Commands#uptime) command.

## bukkit.command.demo
- Allows the use of the [`/demo`](../Commands#demo) command.

## bukkit.command.credits
- Allows the use of the [`/credits`](../Commands#credits) command.

## bukkit.command.ping
- Allows the use of the [`/ping`](../Commands#ping) command.

## bukkit.command.tpsbar
- Allows the use of the [`/tpsbar`](../Commands#tpsbar) command.

## bukkit.command.compass
- Allows the use of the [`/compass`](../Commands#compass) command.

## minecraft.command.gamemode.<gamemode&gt;
Requires enabling [`gamemode.requires-specific-permission`](../Configuration#command) in purpur.yml

- Allows the user to set their own gamemode to <gamemode&gt;
- Available gamemodes
    - adventure, creative, spectator, survival

## minecraft.command.gamemode.<gamemode&gt;.other;
Requires enabling [`gamemode.requires-specific-permission`](../Configuration#command) in purpur.yml

- Allows the user to set their own and other players' gamemode to <gamemode&gt;
- Available gamemodes
    - adventure, creative, spectator, survival

## purpur.debug.f3n
- Allows the use of the F3+N debug hotkey to swap gamemodes.
Player must have this perm _and_ the gamemode perm for it to work.

## purpur.drop.spawners
Requires enabling [`gameplay-mechanics.silk-touch`](../Configuration#silk-touch_1) in purpur.yml

- Players with this permission can use a configured tool with silk
touch enchantment to mine up any spawner cage instead of disappearing.

## purpur.joinfullserver
- Allows players to join when the server is full

## purpur.bypassIdleKick
- Allows players to bypass being kicked while idle

## purpur.portal.instant
- Allows players to instantly teleport through portals when stepping through them
  
## purpur.place.spawners
Requires enabling [`gameplay-mechanics.silk-touch`](../Configuration#silk-touch_1) in purpur.yml

- Players with this permission can place down a spawner cage and
restore the mob type to what it was when it was mined using silk touch.

## purpur.sign.edit
Requires enabling [`sign.right-click-edit`](../Configuration#sign) in purpur.yml

- Allows players to open the sign editor when right clicking a sign while holding a sign.

## purpur.sign.color
Requires enabling [`sign.allow-colors`](../Configuration#sign) in purpur.yml

- Allows players to use color codes on signs

## purpur.sign.style
Requires enabling [`sign.allow-colors`](../Configuration#sign) in purpur.yml

- Allows players to use style codes on signs (except the magic/obfuscated code)

## purpur.sign.magic
Requires enabling [`sign.allow-colors`](../Configuration#sign) in purpur.yml

- Allows players to use the magic/obfuscated style code on signs

## purpur.book.color.sign
Hex colors only register once a book has been signed

- Allows players to use the legacy and hex color codes in books which update after the book is signed

## purpur.anvil.color
Requires enabling [`anvil.allow-colors`](../Configuration#allow-colors_1) in purpur.yml

- Allows players to use legacy color codes in anvil. [`There is more information about colour codes on the Minecraft website.`](**https://minecraft.fandom.com/wiki/Formatting_codes**)

## purpur.anvil.minimessage
Requires enabling [`anvil.allow-minimessage`](../Configuration#use-mini-message) in purpur.yml

- This allows players to use MiniMessage tags in an anvil. [`You can test your minimessage tags here.`](https://webui.adventure.kyori.net/)

## purpur.anvil.remove_italics
Requires enabling [`anvil.allow-colors`](../Configuration#anvil) in purpur.yml

- Allows players to remove the italics from items renamed in the anvil by starting the text with '&r'

## purpur.anvil.format
Requires enabling [`anvil.allow-colors`](../Configuration#anvil) in purpur.yml

- Allows players to use legacy formatting codes in an anvil (&l, &m, &n, &o)


## purpur.enderchest.rows.<number&gt;
Requires enabling [`ender_chest.six-rows`](../Configuration#ender_chest) and [`ender_chest.use-permissions-for-rows`](../Configuration#ender_chest) in purpur.yml

- Controls how many rows a player's enderchest has
- Available sizes
    - one, two, three, four, five, six

## purpur.inventory_totem
Requires enabling [`totem-of-undying-works-in-inventory`](../Configuration#totem-of-undying-works-in-inventory)

- Allows player's totem to work while in their inventory

## purpur.mending_shift_click
Requires setting [`shift-right-click-repairs-mending-points`](../Configuration#shift-right-click-repairs-mending-points) to a number greater than 0

- Allows a player to shift-right-click to use their stored experience to mend their gear
