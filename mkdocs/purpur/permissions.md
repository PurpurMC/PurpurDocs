Purpur adds a few new permission nodes for some of its added features.

By default, Purpur disables **all** of these permissions, no matter if a user has OP. Servers will need a permissions plugin such as [LuckPerms](https://luckperms.net/) to grant permissions to users.

## allow.ride.<mob_id&gt;
Requires enabling [`<mob_id>.ridable`](configuration#mobs) in purpur.yml

- This permission gives the ability to ride a certain mob by shift
right-clicking it. Once mounted you can use WASD to move around, and spacebar to jump or fly. Just replace "<mob_id&gt;" with the mob's Entity ID.

- **examples**:
    - `allow.ride.cow`
    - `allow.ride.zombie_pigman`
    - `allow.ride.snow_golem`

## allow.special.<mob_id&gt;
Requires enabling [`<mob_id>.ridable`](configuration#mobs) in purpur.yml

- This permission gives the ability to activate a ridable mob's
special ability. Not all mobs have a special ability. Just replace "<mob_id&gt;" with
the mob's Entity ID.

- **Currently Available Specials**
    - `allow.special.creeper`
        - Ignites when spacebar is pressed
    - `allow.special.dolphin`
        - Spits when spacebar is pressed
    - `allow.special.phantom`
        - Shoots flames when spacebar is pressed
    - `allow.special.wither`
        - Shoots a wither head on mouse click

## allow.powered.creeper
Requires enabling [`creeper.ridable`](configuration#creeper) in purpur.yml

- This permission gives the ability to toggle a creeper's powered state while riding.
Hold the spacebar while not moving to charge the toggle. Instead of blowing up the powered
state will toggle on or off.

## bukkit.command.uptime
- Allows the use of the [`/uptime`](commands#uptime) command.

## bukkit.command.demo
- Allows the use of the [`/demo`](commands#demo) command.

## bukkit.command.demo.other
- Allows the use of the [`/demo`](commands#demo) command on other players.

## bukkit.command.credits
- Allows the use of the [`/credits`](commands#credits) command.

## bukkit.command.credits.other
- Allows the use of the [`/credits`](commands#credits) command on other players.

## bukkit.command.ping
- Allows the use of the [`/ping`](commands#ping) command.

## bukkit.command.ping.other
- Allows the use of the [`/ping`](commands#ping) command on other players.

## bukkit.command.tpsbar
- Allows the use of the [`/tpsbar`](commands#tpsbar) command.

## bukkit.command.tpsbar.other
- Allows the use of the [`/tpsbar`](commands#tpsbar) command on other players.

## bukkit.command.ram
- Allows the use of the [`/ram`](commands#ram) command.

## bukkit.command.rambar
- Allows the use of the [`/rambar`](commands#rambar) command.

## bukkit.command.rambar.other
- Allows the use of the [`/rambar`](commands#rambar) command on other players.

## bukkit.command.compass
- Allows the use of the [`/compass`](commands#compass) command.

## minecraft.command.gamemode.<gamemode&gt;
Requires enabling [`gamemode.requires-specific-permission`](configuration#command) in purpur.yml

- Allows the user to set their own gamemode to <gamemode&gt;
- Available gamemodes
    - adventure, creative, spectator, survival

## minecraft.command.gamemode.<gamemode&gt;.other;
Requires enabling [`gamemode.requires-specific-permission`](configuration#command) in purpur.yml

- Allows the user to set their own and other players' gamemode to <gamemode&gt;
- Available gamemodes
    - adventure, creative, spectator, survival

## purpur.debug.f3n
- Allows the use of the F3+N debug hotkey to swap gamemodes.
Player must have this perm _and_ the gamemode perm for it to work.

## purpur.drop.spawners
Requires enabling [`gameplay-mechanics.silk-touch`](configuration#silk-touch_1) in purpur.yml

- Players with this permission can use a configured tool with silk
touch enchantment to mine up any spawner cage instead of disappearing.

## purpur.joinfullserver
- Allows players to join when the server is full

## purpur.bypassIdleKick
- Allows players to bypass being kicked while idle

## purpur.portal.instant
- Allows players to instantly teleport through portals when stepping through them
  
## purpur.place.spawners
Requires enabling [`gameplay-mechanics.silk-touch`](configuration#silk-touch_1) in purpur.yml

- Players with this permission can place down a spawner cage and
restore the mob type to what it was when it was mined using silk touch.

## purpur.sign.color
Requires enabling [`sign.allow-colors`](configuration#sign) in purpur.yml

- Allows players to use color codes on signs

## purpur.sign.style
Requires enabling [`sign.allow-colors`](configuration#sign) in purpur.yml

- Allows players to use style codes on signs (except the magic/obfuscated code)

## purpur.sign.magic
Requires enabling [`sign.allow-colors`](configuration#sign) in purpur.yml

- Allows players to use the magic/obfuscated style code on signs

## purpur.book.color.sign
Hex colors only register once a book has been signed

- Allows players to use the legacy and hex color codes in books which update after the book is signed

## purpur.anvil.color
Requires enabling [`anvil.allow-colors`](configuration#allow-colors_1) in purpur.yml

- Allows players to use legacy color codes in anvil. [`There is more information about colour codes on the Minecraft website.`](https://minecraft.wiki/w/Formatting_codes)

## purpur.anvil.minimessage
Requires enabling [`anvil.allow-minimessage`](configuration#use-mini-message) in purpur.yml

- This allows players to use MiniMessage tags in an anvil. [`You can test your minimessage tags here.`](https://webui.advntr.dev/)

## purpur.anvil.remove_italics
Requires enabling [`anvil.allow-colors`](configuration#anvil) in purpur.yml

- Allows players to remove the italics from items renamed in the anvil by starting the text with '&r'

## purpur.anvil.format
Requires enabling [`anvil.allow-colors`](configuration#anvil) in purpur.yml

- Allows players to use legacy formatting codes in an anvil (&l, &m, &n, &o)


## purpur.enderchest.rows.<number&gt;
Requires enabling [`ender_chest.six-rows`](configuration#ender_chest) and [`ender_chest.use-permissions-for-rows`](configuration#ender_chest) in purpur.yml

- Controls how many rows a player's enderchest has
- Available sizes
    - one, two, three, four, five, six

## purpur.inventory_totem
Requires enabling [`totem-of-undying-works-in-inventory`](configuration#totem-of-undying-works-in-inventory) in purpur.yml

- Allows player's totem to work while in their inventory

## purpur.mending_shift_click
Requires setting [`shift-right-click-repairs-mending-points`](configuration#shift-right-click-repairs-mending-points) to a number greater than 0

- Allows a player to shift-right-click to use their stored experience to mend their gear

## purpur.tnt.defuse
Requires enabling [`defuse-tnt-chance`](configuration#defuse-tnt-chance) to a chance greater than 0

- Allows a player to defuse primed TNT when right-clicking with shears
