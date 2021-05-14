Purpur adds a few new permission nodes for some of it’s added features.

By default **all** of these permissions are for OP users only. Any other users will need to be granted the permissions using a permissions plugin.

* **allow.ride.<mob_id&gt;**
    - This permission gives the ability to ride a certain mob by shift
    right clicking it. Once mounted you can use WASD to move around, and spacebar to jump or fly. Just replace "<mob_id&gt;" with the mob's Entity ID.

    - **examples**:
        - `allow.ride.cow`
        - `allow.ride.zombie_pigman`
        - `allow.ride.snow_golem`

* **allow.special.<mob_id&gt;**
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

* **allow.powered.creeper**
    - This permission gives the ability to toggle a creeper's powered state.
    Hold spacebar while not moving to charge the toggle. Instead of blowing up the powered
    state will toggle on or off.

* **bukkit.command.demo**
    - Allows the use of the /demo command.

* **bukkit.command.credits**
    - Allows the use of the /credits command.

* **bukkit.command.ping**
    - Allows the use of the /ping command.

* **bukkit.command.tpsbar**
    - Allows the use of the /tpsbar command.

* **bukkit.gamemode**
    - Allows the user to change the gamemode of another player

* **bukkit.gamemode.<gamemode&gt;**
    - Allows the user to set their gamemode to <gamemode&gt;
    - Available gamemodes
        - adventure
        - creative
        - spectator
        - survival

* **purpur.debug.f3n**
    - Allows the use of the F3+N debug hotkey to swap gamemodes.
    Player must have this perm _and_ the gamemode perm for it to work.

* **purpur.drop.spawners**
    - Players with this permission can use a diamond pickaxe with silk
    touch enchantment to mine up any spawner cage instead of disappearing.

* **purpur.place.spawners**
    - Players with this permission can place down a spawner cage and
    have the mob type restored to what it was when it was mined using silk touch.

* **purpur.sign.edit**
    - Allows players to open the sign editor when right clicking a sign while holding a sign.

* **purpur.sign.color**
    - Allows players to use color codes on signs

* **purpur.sign.style**
    - Allows players to use style codes on signs (except the magic/obfuscated code)

* **purpur.sign.magic**
    - Allows players to use the magic/obfuscated style code on signs

* **purpur.anvil.color**
    - Allows players to use color codes in anvils

* **purpur.anvil.remove_italics**
    - Allows players to remove the italics from items renamed in the anvil by starting the text with '&r'

???+ note "Note"
    Enderchest row permissions require [`settings.blocks.ender_chest.six-rows`](https://pl3xgaming.github.io/PurpurDocs/Configuration#ender_chest) to be enabled!
