Purpur adds a few new permission nodes for some of it’s added features.

By default **all** of these permissions are for OP users only. Any other users will need to be granted the permissions using a permissions plugin.

## allow.ride.<mob_id&gt;
Requires [`<mob_id>.ridable`](../Configuration#mobs) to be enabled in purpur.yml

- This permission gives the ability to ride a certain mob by shift
right-clicking it. Once mounted you can use WASD to move around, and spacebar to jump or fly. Just replace "<mob_id&gt;" with the mob's Entity ID.

- **examples**:
    - `allow.ride.cow`
    - `allow.ride.zombie_pigman`
    - `allow.ride.snow_golem`

## allow.special.<mob_id&gt;
Requires [`<mob_id>.ridable`](../Configuration#mobs) to be enabled in purpur.yml

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
Requires [`creeper.ridable`](../Configuration#creeper) to be enabled in purpur.yml

- This permission gives the ability to toggle a creeper's powered state while riding.
Hold spacebar while not moving to charge the toggle. Instead of blowing up the powered
state will toggle on or off.

## bukkit.command.demo
- Allows the use of the [`/demo`](../Commands#demo) command.

## bukkit.command.credits
- Allows the use of the [`/credits`](../Commands#credits) command.

## bukkit.command.ping
- Allows the use of the [`/ping`](../Commands#ping) command.

## bukkit.command.tpsbar
- Allows the use of the [`/tpsbar`](../Commands#tpsbar) command.

## minecraft.command.gamemode.<gamemode&gt;
Requires [`gamemode.requires-specific-permission`](../Configuration#command) to be enabled in purpur.yml

- Allows the user to set their own gamemode to <gamemode&gt;
- Available gamemodes
    - adventure, creative, spectator, survival

## minecraft.command.gamemode.<gamemode&gt;.other;
Requires [`gamemode.requires-specific-permission`](../Configuration#command) to be enabled in purpur.yml

- Allows the user to set their own and other players' gamemode to <gamemode&gt;
- Available gamemodes
    - adventure, creative, spectator, survival

## purpur.debug.f3n
- Allows the use of the F3+N debug hotkey to swap gamemodes.
Player must have this perm _and_ the gamemode perm for it to work.

## purpur.drop.spawners
Requires [`gameplay-mechanics.silk-touch`](../Configuration#silk-touch) to be enabled in purpur.yml

- Players with this permission can use a configured tool with silk
touch enchantment to mine up any spawner cage instead of disappearing.

## purpur.joinfullserver
- Allows players to join when server is full
  
## purpur.place.spawners
Requires [`gameplay-mechanics.silk-touch`](../Configuration#silk-touch) to be enabled in purpur.yml

- Players with this permission can place down a spawner cage and
have the mob type restored to what it was when it was mined using silk touch.

## purpur.sign.edit
Requires [`sign.right-click-edit`](../Configuration#sign) to be enabled in purpur.yml

- Allows players to open the sign editor when right clicking a sign while holding a sign.

## purpur.sign.color
Requires [`sign.allow-colors`](../Configuration#sign) to be enabled in purpur.yml

- Allows players to use color codes on signs

## purpur.sign.style
Requires [`sign.allow-colors`](../Configuration#sign) to be enabled in purpur.yml

- Allows players to use style codes on signs (except the magic/obfuscated code)

## purpur.sign.magic
Requires [`sign.allow-colors`](../Configuration#sign) to be enabled in purpur.yml

- Allows players to use the magic/obfuscated style code on signs

## purpur.book.color.edit

- Allows players to use legacy color codes in books while it's being edited

## purpur.book.color.sign
Hex colors only register once a book has been signed

- Allows players to use the legacy and hex color codes in books which update after the book is signed

## purpur.anvil.color
Requires [`anvil.allow-colors`](../Configuration#anvil) to be enabled in purpur.yml

- Allows players to use color codes in anvils

## purpur.anvil.remove_italics
Requires [`anvil.allow-colors`](../Configuration#anvil) to be enabled in purpur.yml

- Allows players to remove the italics from items renamed in the anvil by starting the text with '&r'

## purpur.enderchest.rows.<number&gt;
Requires [`ender_chest.six-rows`](../Configuration#ender_chest) and [`ender_chest.use-permissions-for-rows`](../Configuration#ender_chest) to be enabled in purpur.yml

- Controls how many rows a player's enderchest has
- Available sizes
    - one, two, three, four, five, six
