This page details the various configuration settings exposed by Purpur in the purpur.yml file.

If you want information on settings in paper.yml, spigot.yml, bukkit.yml and server.properties you should see their respective documentation pages.

* [Server Configuration (server.properties)](https://minecraft.fandom.com/wiki/Server.properties)

* [Bukkit Configuration (bukkit.yml)](https://bukkit.fandom.com/wiki/Bukkit.yml)

* [Spigot Configuration (spigot.yml)](https://www.spigotmc.org/wiki/spigot-configuration/)

* [Paper Configuration (paper.yml)](https://docs.papermc.io/paper/reference/paper-global-configuration)

* [Pufferfish Configuration (pufferfish.yml)](https://docs.pufferfish.host/setup/pufferfish-fork-configuration/)

???+ warning "Warning"
    Configuration values change frequently at times. It is possible for the information here to be incomplete. If you cannot find what you’re looking for or think something may be wrong, Contact us through our [Discord]({{ social[0].link }}) server.

## Global Settings

Global settings affect all worlds on the server as well as the core server functionality itself.

### verbose

- **default**: false
- **description**: Sets whether the server should dump all configuration values to the server log on startup

### config-version

* **Do not change this for any reason!** Purpur uses this internally to help automatically update your config

### command

* #### uptime
    * ##### format
        - **default**: "&lt;days>&lt;hours>&lt;minutes>&lt;seconds>"
        - **description**: The format the `<uptime>` placeholder uses for [`uptime-command-output`](#uptime-command-output)
    * ##### day
        - **default**: "%02d day, "
        - **description**: Output of `<day>` placeholder in [command.uptime.format](#format) option
    * ##### days
        - **default**: "%02d days, "
        - **description**: Output of `<days>` placeholder in [command.uptime.format](#format) option
    * ##### hour
        - **default**: "%02d hour, "
        - **description**: Output of `<hour>` placeholder in [command.uptime.format](#format) option
    * ##### hours
        - **default**: "%02d hours, "
        - **description**: Output of `<hours>` placeholder in [command.uptime.format](#format) option
    * ##### minute
        - **default**: "%02d minute, and "
        - **description**: Output of `<minute>` placeholder in [command.uptime.format](#format) option
    * ##### minutes
        - **default**: "%02d minutes, and "
        - **description**: Output of `<minutes>` placeholder in [command.uptime.format](#format) option
    * ##### second
        - **default**: "%02d second"
        - **description**: Output of `<second>` placeholder in [command.uptime.format](#format) option
    * ##### seconds
        - **default**: "%02d seconds"
        - **description**: Output of `<seconds>` placeholder in [command.uptime.format](#format) option
* #### gamemode
    * ##### requires-specific-permission
        - Requires [`minecraft.command.gamemode.<gamemode>`](permissions#minecraftcommandgamemodegamemode) permission
        - **default**: false
        - **description**: Set to true for each gamemode to require its own permission
* #### tpsbar
    * ##### title
        `<tps>` - The current TPS

        `<mspt>` - The current MSPT

        `<ping>` - The current ping

        - **default**: &lt;gray>TPS&lt;yellow>:&lt;/yellow> &lt;tps> MSPT&lt;yellow>:&lt;/yellow>
      &lt;mspt> Ping&lt;yellow>:&lt;/yellow> &lt;ping>ms
        - **description**: The format of the bossbar when the server runs the `/tpsbar` command

    * ##### overlay
        - **default**: NOTCHED_20
        - **description**:
            Sets the overlay type of the Bossbar  
            Available options: `PROGRESS`, `NOTCHED_6`, `NOTCHED_10`, `NOTCHED_12`, `NOTCHED_20`
    * ##### fill-mode
        - **default**: MSPT
        - **description**:
            What the BossBar bar should show
            Available options: `TPS`, `MSPT`, `PING` 
    * ##### progress-color
        Available options: `PINK`, `BLUE`, `RED`, `GREEN`, `YELLOW`, `PURPLE`, `WHITE`
        * ###### good
            - **default**: GREEN
            - **description**: What color should show when `fill-mode` is "good"
        * ###### medium
            - **default**: YELLOW
            - **description**: What color should show when `fill-mode` is "medium"
        * ###### low
            - **default**: RED
            - **description**: What color should show when `fill-mode` is "low"
    * ##### text-color
        `<text>` - The format from [`settings.command.tpsbar.title`](#title)
        * ###### good
            - **default**: &lt;gradient:#55ff55:#00aa00>&lt;text>&lt;/gradient>
            - **description**: The gradient of `<text>` when `fill-mode` is "good"
        * ###### medium
            - **default**: &lt;gradient:#ffff55:#ffaa00>&lt;text>&lt;/gradient>
            - **description**: The gradient of `<text>` when `fill-mode` is "medium"
        * ###### low
            - **default**: &lt;gradient:#ff5555:#aa0000>&lt;text>&lt;/gradient>
            - **description**: The gradient of `<text>` when `fill-mode` is "low"
    * ##### tick-interval
        - **default**: 20
        - **description**: How often the bossbar should update
* #### rambar
    * ##### title
        `<used>` - The current amount of ram used.

        `<xmx>` - The max set Xmx.

        `<percent>` - The percentage of ram used.

      - **default**: '"&lt;gray>Ram&lt;yellow>:&lt;/yellow> &lt;used>/&lt;xmx> (&lt;percent>)"'
      - **description**: The format of the bossbar when the server runs the `/rambar` command

    * ##### overlay
        - **default**: NOTCHED_20
        - **description**:
          Sets the overlay type of the Bossbar  
          Available options: `PROGRESS`, `NOTCHED_6`, `NOTCHED_10`, `NOTCHED_12`, `NOTCHED_20`
    * ##### progress-color
      Available options: `PINK`, `BLUE`, `RED`, `GREEN`, `YELLOW`, `PURPLE`, `WHITE`
        * ###### good
            - **default**: GREEN
            - **description**: What color should show when the ram used "good"
        * ###### medium
            - **default**: YELLOW
            - **description**: What color should show when the ram used is "medium"
        * ###### low
            - **default**: RED
            - **description**: What color should show when the ram used is "low"
    * ##### text-color
      `<text>` - The format from [`settings.command.tpsbar.title`](#title)
        * ###### good
            - **default**: &lt;gradient:#55ff55:#00aa00>&lt;text>&lt;/gradient>
            - **description**: The gradient of `<text>` when the ram used is "good"
        * ###### medium
            - **default**: &lt;gradient:#ffff55:#ffaa00>&lt;text>&lt;/gradient>
            - **description**: The gradient of `<text>` when the ram used is "medium"
        * ###### low
            - **default**: &lt;gradient:#ff5555:#aa0000>&lt;text>&lt;/gradient>
            - **description**: The gradient of `<text>` when the ram used is "low"
    * ##### tick-interval
        - **default**: 20
        - **description**: How often the bossbar should update
* #### compass
    * ##### title
        - **default**: "S  ·  ◈  ·  ◈  ·  ◈  ·  SW  ·  ◈  ·  ◈  ·  ◈  ·  W  ·  ◈  ·  ◈  ·  ◈  ·  NW  ·  ◈  ·  ◈  ·  ◈  ·  N  ·  ◈  ·  ◈  ·  ◈  ·  NE  ·  ◈  ·  ◈  ·  ◈  ·  E  ·  ◈  ·  ◈  ·  ◈  ·  SE  ·  ◈  ·  ◈  ·  ◈  ·  
S  ·  ◈  ·  ◈  ·  ◈  ·  SW  ·  ◈  ·  ◈  ·  ◈  ·  W  ·  ◈  ·  ◈  ·  ◈  ·  NW  ·  ◈  ·  ◈  ·  ◈  ·  N  ·  ◈  ·  ◈  ·  ◈  ·  NE  ·  ◈  ·  ◈  ·  ◈  ·  E  ·  ◈  ·  ◈  ·  ◈  ·  SE  ·  ◈  ·  ◈  ·  ◈  ·  "
        - **description**: The format of the bossbar when the server runs the [`/compass`](commands#compass) command

    * ##### overlay
        - **default**: PROGRESS
        - **description**:
            Sets the overlay type of the Bossbar  
            Available options: `PROGRESS`, `NOTCHED_6`, `NOTCHED_10`, `NOTCHED_12`, `NOTCHED_20`
    * ##### progress-color
        Available options: `PINK`, `BLUE`, `RED`, `GREEN`, `YELLOW`, `PURPLE`, `WHITE`
        - **default**: GREEN
        - **description**: The color of the bossbar
    * ##### percent
        - **default**: 1.0
        - **description**: How filled the bossbar is ranging from 0.0 to 1.0
    * ##### tick-interval
        - **default**: 5
        - **description**: How often the bossbar should update
* #### hide-hidden-players-from-entity-selector
    - **default**: false
    - **description**: Set to true to hide players from the entity selector if they're hidden

### allow-water-placement-in-the-end

- **default**: true
- **description**: Allows the placement of water in the end.

### use-alternate-keepalive

- **default**: false
- **description**: Uses a different approach to keepalive ping timeouts. Enabling this sends a keepalive packet once per second to a player, and only kicks for timeout if none of them were responded to in 30 seconds. Responding to any of them in any order will keep the player connected. AKA, it won't kick your players because one packet gets dropped somewhere along the lines

### tps-catchup

- **default**: true
- **description**: Control tps catch-up

???+ note "Note"
    TPS catchup makes your server tick faster than 20 TPS after any period of time that is below 20. This is an attempt at keeping the average TPS as close to 20 as possible, but does come with its own set of side effects, an example being when players get insta-killed by mobs during a lag spike

### server-mod-name
- **default**: Purpur
- **description**: This modifies the server name that shows up when a client is outdated or when someone opens the debug screen [F3]

### fix-projectile-looting-transfer
- **default**: false
- **description**: Addresses [`MC-3304`](https://bugs.mojang.com/browse/MC-3304) by preventing looting from being applied to deaths caused by a projectile, unless if a plugin changed the looting modifier.

### clamp-attributes
- **default**: true
- **description**: Controls if attributes should have their values clamped.

### limit-armor
- **default**: true
- **description**: Controls if armor should limit how much damage they can reduce.

### username-valid-characters
- **default**: ^[a-zA-Z0-9_.]*$
- **description**: Characters that can be used in usernames. Configurable with regex.

### lagging-threshold
- **default**: 19.0
- **description**: Purpur keeps track of when it is lagging in order to have the ability to change behaviors accordingly. This value is that threshold when you want to consider the server to be lagging. ~~Right now this is only used for mob.villager.brain-ticks setting~~

### fix-network-serialized-items-in-creative
- **default**: false
- **description**: Set to true to fix items modified by NetworkItemSerializeEvent that persist even though they're client-sided due to the creative client using creative inventory actions

### disable-give-dropping
- **default**: false
- **description**: Set to true to disable the /give command from dropping items on the floor when a player's inventory is full

### player-deaths-always-show-item
- **default**: false
- **description**: Set to true to always show the item used to kill the player in player death messages.

### messages

#### afk-broadcast-away
Requires the [`kick-if-idle`](#kick-if-idle) setting to be `false`

- **default**: &lt;yellow>&lt;italic>%s is now AFK
- **description**: This is the message that gets broadcasted when a user goes AFK (must have `player-idle-timeout` set greater than 0 & [kick-if-idle](#kick-if-idle) set as false)

#### afk-broadcast-back
Requires the [`kick-if-idle`](#kick-if-idle) setting to be `false`

- **default**: &lt;yellow>&lt;italic>%s is no longer AFK
- **description**: This is the message that gets broadcasted when a user is no longer AFK (must have `player-idle-timeout` set greater than 0 & [kick-if-idle](#kick-if-idle) set as false)

### afk-broadcast-use-display-name
Requires the [`kick-if-idle`](#kick-if-idle) setting to be `false`
Requires [`afk-broadcast-away`](#afk-broadcast-away) or [`afk-broadcast-back`](#afk-broadcast-back) to have a non-null value

- **default**: false
- **description**: Uses a plain-text version of the player's display name in the AFK broadcast, instead of their username.
- **NOTE**: This option does NOT set a player's TAB name

#### afk-tab-list-prefix
Requires the [`kick-if-idle`](#kick-if-idle) setting to be `false`

- **default**: "[AFK] "
- **description**: The prefix that shows up on the playerlist before someone's name when they're AFK

#### afk-tab-list-suffix
Requires the [`kick-if-idle`](#kick-if-idle) setting to be `false`

- **default**: ""
- **description**: The suffix that shows up on the playerlist after someone's name when they're AFK

#### cannot-ride-mob
Requires the [`allow.ride.<mob_id>`](permissions#allowridemob_id) permission

- **default**: &lt;red>You cannot mount that mob
- **description**: Message that shows when someone tries to mount a mob they're not allowed to.

#### dont-run-with-scissors
Requires the [`damage-if-sprinting`](#damage-if-sprinting) option to be enabled

- **default**: &lt;red>&lt;italic>Don't run with scissors!
- **description**: Actionbar message that shows when someone attempts to run with scissors

#### ping-command-output
Requires the [`bukkit.command.ping`](permissions#bukkitcommandping) permission

- **default**: &lt;green>%s's ping is %sms
- **description**: Output when `/ping <user>` is run.

#### uptime-command-output
Requires the [`bukkit.command.uptime`](permissions#bukkitcommanduptime) permission
`<uptime>` - The format from [`<global>.command.uptime.format`](#format)

- **default**: &lt;green>Server uptime is &lt;uptime>
- **description**: Message that shows when the `/uptime` command is ran.

#### demo-command-output
Requires the [`bukkit.command.demo`](permissions#bukkitcommanddemo) permission

- **default**: &lt;green>%s has been shown the demo screen
- **description**: Message that shows when the demo screen is enabled for a user using the `/demo` command.

#### credits-command-output
Requires the [`bukkit.command.credits`](permissions#bukkitcommandcredits) permission

- **default**: &lt;green>%s has been shown the end credits
- **description**: Message that shows when the credits screen is enabled for a user using the `/credits` command.

#### tpsbar-command-output
Requires the [`bukkit.command.tpsbar`](permissions#bukkitcommandtpsbar) permission

- **default**: &lt;green>Tpsbar toggled &lt;onoff> for &lt;target>
- **description**: Message that shows when the tpsbar is enabled for a user using the `/tpsbar` command.

#### ram-command-output

- **default**: '&lt;green>Ram Usage: &lt;used>/&lt;xmx> (&lt;percent>)'
- **description**: A chat message that shows the ram usage when someone uses the `/ram` command.

#### rambar-command-output

- **default**: &lt;green>Rambar toggled &lt;onoff> for &lt;target>
- **description**: Message that shows when the rambar is enabled for a user using the `/rambar` command.

#### unverified-username
- **default**: default
- **description**: Message that shows when a player is kicked for having an unverified username (user is in offline-mode). Setting as "default" displays the default message "Failed to verify username!"

#### sleep-skipping-night
- **default**: default
- **description**: The actionbar message that appears when the night has been skipped. Set to "default" to let the client's use their own translatable components. Set to an empty string to disable it.

#### sleeping-players-percent
- **default**: default
- **description**: The actionbar message that appears when a player is asleep. Set to "default" to let the clients use their own translatable components. Set to an empty string to disable it. Available placeholders: `<count>` - the current amount of players sleeping, `<total>` - the total amount of players needed to sleep

#### sleep-not-possible
- **default**: default
- **description**: The actionbar message that appears when a player tries to sleep, but the `playersSleepingPercentage` gamerule is set to a value greater than 100. Set to "default" to let the clients use their own translatable components. Set to an empty string to disable it.

#### death-message
* ##### stonecutter
    - **default**: &lt;player> has sawed themself in half
    - **description**: The death message that appears when the player is killed because they were standing on a stonecutter
* ##### run-with-scissors
    - **default**: &lt;player> slipped and fell on their shears
    - **description**: The death message that appears when the player is killed because they were running with scissors

### network
#### kick-for-out-of-order-chat
- **default**: true
- **description**: Set to false to stop the server from kicking a player for their chat being out of order 
####  upnp-port-forwarding
- **default**: false
- **description**: Attempt to automatically port forward using UPnP when the server starts up
####  max-joins-per-second
- **default**: false
- **description**: Set to true to make the `max-joins-per-tick` setting in paper.yml be used per second instead of per tick

### blocks

####  barrel
* ##### rows
    - **default**: 3
    - **description**: The amount of rows a barrel should have. Min: 1, Max: 6
####  beehive
* ##### max-bees-inside
    - **default**: 3
    - **description**: The maximum amount of bees allowed inside of a beehive/bee_nest
####  grindstone
* ##### ignored-enchants
    - **default**:
        ``` yaml
        - minecraft:binding_curse
        - minecraft:vanishing_curse
        ```
    - **description**: The enchantments that aren't removed from grindstones
* ##### remove-attributes
    - **default**: false
    - **description**: Set to true to allow the grindstone to remove the attributes from an item
* ##### remove-name-and-lore
    - **default**: false
    - **description**: Set to true to allow the grindstone to remove the name and lore from an item
####  ender_chest
* ##### six-rows
    - **default**: false
    - **description**: When enabled, ender chests should have six rows of inventory space
* ##### use-permissions-for-rows
    - Requires [`ender_chest.six-rows`](#six-rows) to be true
    - Requires [`purpur.enderchest.rows.<number>`](permissions#purpurenderchestrowsnumber) permission
    - **default**: false
    - **description**: Use permission nodes to determine the number of rows. By default, with this setting enabled, all players have `six` rows unless otherwise specified using permissions.

#### disable-mushroom-updates  
- **default**: false
- **description**: Stops the mushroom block from updating it's block state server side
#### disable-chorus-plant-updates  
- **default**: false
- **description**: Stops the chorus plant from updating it's block state server side
####  crying_obsidian
* ##### valid-for-portal-frame
    - **default**: false
    - **description**: Set to true to make it so you can create portals out of crying obsidian
#### twisting_vines
* ##### max-growth-age
    - **default**: 25
    - **description**: The max growth age that the plant can grow
#### weeping_vines
* ##### max-growth-age
    - **default**: 25
    - **description**: The max growth age that the plant can grow
#### cave_vines
* ##### max-growth-age
    - **default**: 25
    - **description**: The max growth age that the plant can grow
#### kelp
* ##### max-growth-age
    - **default**: 25
    - **description**: The max growth age that the plant can grow
#### anvil
* ##### cumulative-cost
    - **default**: true
    - **description**: If the cumulative cost should apply when an item is used in an anvil
#### lightning_rod
* ##### range
    - **default**: 128
    - **description**: Change the range in which the lightning rod redirects lightning
### broadcasts

#### advancement

##### only-broadcast-to-affected-player
- **default**: false
- **description**: Broadcasts the advancment messages in chat only to the affected player

#### death

##### only-broadcast-to-affected-player
- **default**: false
- **description**: Broadcasts the death messages in chat only to the affected player

### logger

#### suppress-init-legacy-material-errors
- **default**: false
- **description**: Suppress warnings about plugins initializing the legacy material api
#### suppress-ignored-advancement-warnings
- **default**: false
- **description**: Suppress warnings about unknown attributes in console and logs
#### suppress-unrecognized-recipe-errors
- **default**: false
- **description**: Suppress warnings about attempts to load an unrecognized recipe
#### suppress-setblock-in-far-chunk-errors
- **default**: false
- **description**: Suppress errors where setBlock was detected in a far chunk
#### suppress-library-loader
- **default**: false
- **description**: Suppress logs related to the library loader

### food-properties
- **default**: {}
- **description:** Modify to change food properties. An example using all settings with explanations:
``` yaml
spider_eye:                # The food to edit
  nutrition: 2              # The amount of hunger points restored
  saturation-modifier: 0.8  # The amount of saturation restored. Equation used is "nutrition * saturation-modifier * 2"
  is-meat: false            # Marks a food as edible for wolfs
  can-always-eat: false     # Marks if this food can be eaten even at full hunger
  fast-food: false          # How long it takes to eat food (false: 32 ticks, true: 16 ticks)
  effects:                  # List of all the effects to be applied when eaten (can have multiple effects)
    poison:                 # Effect to apply
      duration: 100         # Duration of effect (in ticks)
      chance: 1.0           # Chance for effect to be applied (0.0 - 1.0)
      visible: true         # Shows particles
      amplifier: 1          # Amplification of effect
      ambient: false        # Set to true to make particles less obtrusive on screen (like beacon effects)
      show-icon: true       # Show effect icon on HUD
```

### entity

#### enderman
* ##### short-height
    - **default**: false
    - **description**: Allows endermen to fit into 2 block tall spaces if enabled. Since client hitbox remains the same, you can still hit them in the head

### enchantment

* ##### allow-infinity-and-mending-together
    - **default**: false
    - **description**: Allows the mending and infinity enchantment to be on the same weapon/tool
* ##### allow-infinity-on-crossbow
    - **default**: false
    - **description**: Allows the infinity enchantment on crossbows
* ##### allow-looting-on-shears
    - **default**: false
    - **description**: Allows the looting enchantment on shears
* ##### allow-unsafe-enchant-command
    - **default**: false
    - **description**: Allows the ability to increase enchantments passed their max level through the command
* ##### clamp-levels
    - **default**: true
    - **description**: Setting this to `false` allows levels to go up to `32767` by storing them as shorts instead of bytes.

???+ note "Note"
    Clients will not display levels higher than `255`

####  anvil
* ##### allow-unsafe-enchants
    - **default**: false
    - **description**: This option is required to make the following unsafe enchantment settings work.
* ##### allow-inapplicable-enchants
    - **default**: true
    - **description**: Allows applying enchantments on tools or armour that are normally not applicable. For example, sharpness on a pickaxe.
* ##### allow-incompatible-enchants
    - **default**: true
    - **description**: Allows applying enchantments together that are normally incompatible. For example, protection and fire protection or fortune and silk touch.
* ##### allow-higher-enchants-levels
    - **default**: true
    - **description**: Allows the ability to increase enchantments passed their maximum level. For example, efficiency V + efficiency V = efficiency VI.
* ##### replace-incompatible-enchants
    - **default**: false
    - **description**: When applying enchantments together that are incompatible, instead of using the enchantment in the base item, the enchantment will be replaced by the enchantment on the secondary item.

## world-settings

World settings are on a per-world basis. The child-node `default` is used for all worlds that do not have their own specific settings.

For a more clear explanation of the world settings section of the config, feel free to read through Paper's explanation here: https://docs.papermc.io/paper/per-world-configuration

### hunger

#### starvation-damage
- **default**: 1.0
- **description**: The amount of damage starvation will do

### settings

#### entity
* #### shared-random
- **default**: true
- **description**: Setting this to false allows RNG manipulation. Paper patches RNG manipulation by using a shared (and locked) random source. This comes with a performance gain, but technical players may prefer to turn this off for the ability to manipulate RNG.

???+ warning "Warning"
    The shared-random setting is not tested by the Purpur team and can be seen as unsafe. (The shared random is designed to be multithread safe. Undoing this patch *can* cause ConcurrentModificationExceptions to fire in some situations, with or without plugins. And increase memory usage.)


### blocks

#### enchantment-table
* ##### lapis-persists
    - **default**: false
    - **description**: Setting this to true makes it so lapis lazuli can stay in the enchanting table slot, so you can leave your lapis lazuli in the table
#### dragon_egg
* ##### teleport
    - **default**: true
    - **description**: Control whether the dragon egg will teleport when hit
#### observer
* ##### disable-clock
    - **default**: false
    - **description**: Set to true to disable observer clocks
#### azalea
* ##### growth-chance
    - **default**: 0.0
    - **description**: Chance for azalea to grow into trees naturally
#### flowering_azalea
* ##### growth-chance
    - **default**: 0.0
    - **description**: Chance for flowering azalea to grow into trees naturally
#### campfire
* ##### lit-when-placed
    - **default**: true
    - **description**: Set to false to stop the campfire from being lit when placed
#### cactus
* ##### breaks-from-solid-neighbors
    - **default**: true
    - **description**: Whether a cactus will break from a solid block next to it
* ##### affected-by-bonemeal
    - **default**: false
    - **description**: Set to true to make it so cacti can be bonemealed
#### sugar_cane
* ##### affected-by-bonemeal
    - **default**: false
    - **description**: Set to true to make it so sugarcane can be bonemealed
#### nether_wart
* ##### affected-by-bonemeal
    - **default**: false
    - **description**: Set to true to make it so netherwart can be bonemealed
#### cauldron
* ##### fill-chances
    * ###### rain
        - **default**: 0.05
        - **description**: The speed in which a cauldron fills with rain (depends on random tick)
    * ###### powder-snow
        - **default**: 0.1
        - **description**: The speed in which a cauldron fills with powdered snow (depends on random tick)
    * ###### dripstone-water
        - **default**: 0.17578125
        - **description**: The speed in which a cauldron below a down-facing pointed dripstone that has water placed a block above it fills with water (depends on random tick)
    * ###### dripstone-lava
        - **default**: 0.05859375
        - **description**: The speed in which a cauldron below a down-facing pointed dripstone that has lava placed a block above it fills with lava (depends on random tick)
#### turtle_egg
* ##### break-from-exp-orbs
    - **default**: true
    - **description**: Allow exp orbs to damage/break turtle eggs
* ##### break-from-items
    - **default**: true
    - **description**: Allow dropped items to damage/break turtle eggs
* ##### break-from-minecarts
    - **default**: true
    - **description**: Allow minecarts to damage/break turtle eggs
* ##### bypass-mob-griefing
    - **default**: false
    - **description**: Set to true for turtle eggs to bypass the mob griefing gamerule
* ##### random-tick-crack-chance
    - **default**: 500
    - **description**: The chance a turtle egg will crack
* ##### feather-fall-distance-affects-trampling
    - **default**: false
    - **description**: Set to true to stop trampling if entities fall a distance equal to their feather falling level, plus the extra block necessary to trample in the first place. Feather Falling 1 requires you to fall over 3+ blocks to trample. FF 2 requires 4+, etc.
#### powered-rail
* ##### activation-range
    - **default**: 8
    - **description**: The amount of powered rails that get activated by a single redstone source
#### conduit
* ##### valid-ring-blocks
    - **default**:
        ``` yaml
        - minecraft:prismarine
        - minecraft:prismarine_bricks
        - minecraft:sea_lantern
        - minecraft:dark_prismarine
        ```
    - **description**: Blocks that can be used to build a conduit
* ##### effect-distance
    - **default**: 16
    - **description**: The effective radius of the conduit for every seven blocks in the frame
* ##### mob-damage
    * ###### distance
        - **default**: 8
        - **description**: The distance (in blocks) to damage hostile mobs
    * ###### damage-amount
        - **default**: 4
        - **description**: The amount of damage to apply to hostile mobs every 2 seconds if they are in contact with water/rain
#### beacon
* ##### allow-effects-with-tinted-glass
    - **default**: false
    - **description**: Whether to allow beacon effects to activate when it's covered by tinted glass
* ##### effect-range
    * ###### level-1
        - **default**: 20
        - **description**: Amount of blocks the effect range reaches for this level
    * ###### level-2
        - **default**: 30
        - **description**: Amount of blocks the effect range reaches for this level
    * ###### level-3
        - **default**: 40
        - **description**: Amount of blocks the effect range reaches for this level
    * ###### level-4
        - **default**: 50
        - **description**: Amount of blocks the effect range reaches for this level
#### sponge
* ##### absorbs-lava
    - **default**: false
    - **description**: Set to true to allow sponges to absorb lava
* ##### absorption
    * ###### area
        - **default**: 64
        - **description**: Area of blocks that a sponge absorbs water
    * ###### radius
        - **default**: 6
        - **description**: The radius of blocks that a sponge absorbs water
#### composter
* ##### sneak-to-bulk-process
    - **default**: false
    - **description**: Set to true to allow bulk processing of food/plant items by sneak right-clicking with the item in hand
####  coral
* ##### die-outside-water
    - **default**: true
    - **description**: Set to false to keep coral alive when placed on land
#### sculk_shrieker
* ##### can-summon-default
    - **default**: false
    - **description**: Set to true to set `can_summon` to `true` on placement
#### slab
* ##### break-individual-slabs-when-sneaking
    - **default**: false
    - **description**: Set to true to allow breaking individual slabs in a double slab block while sneaking
#### packed_ice
* ##### allow-mob-spawns
    - **default**: true
    - **description**: Set to false to disallow mob spawning on packed ice
#### blue_ice
* ##### allow-mob-spawns
    - **default**: true
    - **description**: Set to false to disallow mob spawning on blue ice
* ##### allow-snow-formation
    - **default**: true
    - **description**: Set to false to disallow snow formation on blue ice
#### sand
* ##### fix-duping
    - **default**: true
    - **description**: Set to false to re-enable the ability to sand dupe. You might also need to disable [`safe-teleporting`](#safe-teleporting)
#### end_portal
* ##### safe-teleporting
    - **default**: true
    - **description**: Toggles protection against unsafe code in the handling of end portal teleportation. Disabling this may be necessary for some exploits
#### respawn_anchor
* ##### explode
    - **default**: true
    - **description**: Whether respawn anchors explode. Setting this to false just makes the respawn anchors blip out of existence
* ##### explosion-power
    - **default**: 5.0
    - **description**: The blast radius of the explosion. (For comparison, TNT is 4.0 and charged creepers are 6.0)
* ##### explosion-fire
    - **default**: true
    - **description**: Whether the explosion can cause fire or not
* ##### explosion-effect
    - **default**: BLOCK
    - **description**: What to do with the blocks that are effected by the explosion.

        ???+ note "Available Values"
            All values will break blocks

            - `TNT` - all items will drop unless the `tntExplosionDropDecay` gamerule is set to `true`
            - `MOB` - some items will drop unless the `mobExplosionDropDecay` gamerule is set to `false`
            - `BLOCK` - some items will drop unless the `blockExplosionDropDecay` gamerule is set to `false`
            - `NONE` - all items will drop

#### sign
* ##### allow-colors
    - Requires [`purpur.sign.color`](permissions#purpursigncolor), [`purpur.sign.style`](permissions#purpursignstyle), and/or [`purpur.sign.magic`](permissions#purpursignmagic) permission
    - **default**: false
    - **description**: Allow players to use color codes on signs
#### magma-block
* ##### damage-when-sneaking
    - **default**: false
    - **description**: Set to true to enable damage when sneaking
* ##### damage-with-frost-walker
    - **default**: false
    - **description**: Set to true to enable damage when walking with boots enchanted with frost-walker
#### lava
* ##### infinite-required-sources
    - **default**: 2
    - **description**: The amount of sources required to have infinite lava
* ##### speed
    * ###### nether
        - **default**: 10
        - **description**: Delay in ticks between physics/flowing (lower is faster)
    * ###### not-nether
        - **default**: 30
        - **description**: Delay in ticks between physics/flowing (lower is faster)
#### water
* ##### infinite-required-sources
    - **default**: 2
    - **description**: The amount of sources required to have infinite water
#### piston
* ##### block-push-limit
    - **default**: 12
    - **description**: The amount of blocks a piston can push
#### bed
* ##### explode
    - **default**: true
    - **description**: Whether beds explode. Setting this to false just makes the bed blip out of existence
* ##### explode-on-villager-sleep
    - **default**: false
    - **description**: Whether beds explode when a villager sleeps in one.
* ##### explosion-power
    - **default**: 5.0
    - **description**: The blast radius of the explosion. (For comparison, TNT is 4.0 and charged creepers are 6.0)
* ##### explosion-fire
    - **default**: true
    - **description**: Whether the explosion can cause fire or not
* ##### explosion-effect
    - **default**: BLOCK
    - **description**: What to do with the blocks that are effected by the explosion.

        ???+ note "Available Values"
            All values will break blocks

            - `TNT` - all items will drop unless the `tntExplosionDropDecay` gamerule is set to `true`
            - `MOB` - some items will drop unless the `mobExplosionDropDecay` gamerule is set to `false`
            - `BLOCK` - some items will drop unless the `blockExplosionDropDecay` gamerule is set to `false`
            - `NONE` - all items will drop
#### farmland
* ##### gets-moist-from-below
    - **default**: false
    - **description**: Allow soil to moisten from water directly below it
* ##### use-alpha-farmland
    - **default**: false
    - **description**: Stops the farmland from getting trampled if a fence or a cobble wall is placed directly underneath it
* ##### bypass-mob-griefing
    - **default**: false
    - **description**: Set to true for farmland to bypass the mob griefing gamerule
* ##### only-players-trample
    - **default**: false
    - **description**: Set to true if only players may trample farmland.
* ##### disable-trampling
    - **default**: false
    - **description**: Set to true to disable trampling completely.
* ##### trample-height
    - **default**: -1.0
    - **description**: Set the height a player/entity needs to fall before it tramples farmland

???+ note "Note"
        Trample height is in block height or an exact distance. During testing was found that the values for fallDistance are very inconsistent. The results of these tests can be found here:
        Value set -> Actual fall distance needed to trample
        1.0 -> 1.25
        1.5 -> 1.75
        2.0 -> 2.25
        2.5 -> 2.87
        3.0 -> 3.5
        3.5 -> 4.25
        4.0 -> 4.25
        4.5 -> 5.0
        5.0 -> 5.87
        5.5 -> 5.87
        6.0 -> 6.75

* ##### feather-fall-distance-affects-trampling
    - **default**: false
    - **description**: Set to true to stop trampling if entities fall a distance equal to their feather falling level, plus the extra block necessary to trample in the first place. Feather Falling 1 requires you to fall over 3+ blocks to trample. FF 2 requires 4+, etc.
#### spawner
* ##### deactivate-by-redstone
    - **default**: false
    - **description**: Allow spawners to be deactivated by redstone
* ##### fix-mc-238526
    - **default**: false
    - **description**: Fix spawners not spawning water animals correctly; MC-238526
#### dispenser
* ##### apply-cursed-to-armor-slots
    - **default**: true
    - **description**: Should dispensers apply armor to armor slots if enchanted with curse of binding
* ##### place-anvils
    - **default**: false
    - **description**: Allows anvils to be placed by dispensers
#### anvil
* ##### use-mini-message
    - Requires [`purpur.anvil.minimessage`](permissions#purpuranvilminimessage) permission
    - **default**: false
    - **description**:  Allows players to use MiniMessage tags in an anvil.
* ##### allow-colors
    - Requires [`purpur.anvil.color`](permissions#purpuranvilcolor) permission
    - **default**: false
    - **description**: Allows players to use color codes in anvils
* ##### iron-ingots-used-for-repair
    - **default**: 0
    - **description**: The amount of iron ingots required to repair an anvil
* ##### obsidian-used-for-damage
    - **default**: 0
    - **description**: The amount of obsidian required to damage an anvil
#### stonecutter
* ##### damage
    - **default**: 0.0
    - **description**: If a value is set, Mobs will also avoid walking over the stonecutter.
#### furnace
* ##### use-lava-from-underneath
    - **default**: false
    - **description**: Allows the furnace to be infinitely powered by lava placed underneath it
#### chest
* ##### open-with-solid-block-on-top
    - **default**: false
    - **description**: Allows for chests to open even with a solid block on top
#### shulker_box
* ##### allow-oversized-stacks
    - **default**: false
    - **description**: Controls whether overstacked items are allowed in shulker boxes (default fixes chunk ban issue PaperMC/Paper#4748)
#### door
* ##### requires-redstone
    - **default**: []
    - **description**: Allows you to set the doors that require redstone to be operated (oak, spruce, etc)
#### powder_snow
* ##### bypass-mob-griefing
    - **default**: false
    - **description**: Set to true for powdered snow to bypass the mob griefing gamerule
#### end-crystal
* ##### cramming-amount
    - **default**: 0
    - **description**: Controls how many end crystals can occupy the same hitbox space. When set to a certain number, any additional crystals will cause an explosion.
* ##### baseless
    * ###### explode
        - **default**: true
        - **description**: Set to false to stop the crystal from exploding
    * ###### explosion-power
        - **default**: 6.0
        - **description**: The power of the end crystal's explosion
    * ###### explosion-fire
        - **default**: false
        - **description**: Set to true to place fire when the end-crystal explodes
    * ###### explosion-effect
        - **default**: BLOCK
        - **description**: What to do with the blocks that are effected by the explosion.

            ???+ note "Available Values"
                All values will break blocks

                - `TNT` - all items will drop unless the `tntExplosionDropDecay` gamerule is set to `true`
                - `MOB` - some items will drop unless the `mobExplosionDropDecay` gamerule is set to `false`
                - `BLOCK` - some items will drop unless the `blockExplosionDropDecay` gamerule is set to `false`
                - `NONE` - all items will drop

* ##### base
    * ###### explode
        - **default**: true
        - **description**: Set to false to stop the crystal from exploding
    * ###### explosion-power
        - **default**: 6.0
        - **description**: The power of the end crystal's explosion
    * ###### explosion-fire
        - **default**: false
        - **description**: Set to true to place fire when the end-crystal explodes
    * ###### explosion-effect
        - **default**: BLOCK
        - **description**: What to do with the blocks that are effected by the explosion.

            ???+ note "Available Values"
                All values will break blocks

                - `TNT` - all items will drop unless the `tntExplosionDropDecay` gamerule is set to `true`
                - `MOB` - some items will drop unless the `mobExplosionDropDecay` gamerule is set to `false`
                - `BLOCK` - some items will drop unless the `blockExplosionDropDecay` gamerule is set to `false`
                - `NONE` - all items will drop


### mobs

#### allay
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it won't eject you)
* ##### respect-nbt
    - **default**: []
    - **description**: It ensures that Allays respect the NBT from the items they pick up. If you add stored enchantments to the list to respect, then if you give an Allay a sword with an enchantment, it will only pick up swords with the same enchantments.
#### frog
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### ridable-jump-height
    - **default**: 0.65
    - **description**: The height this mob can jump when riding it (in blocks)
* ##### breeding-delay-ticks
    - **default**: 6000
    - **description**: The amount of ticks to wait before being able to breed again
#### tadpole
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
#### warden
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
#### ender_dragon
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### ridable-max-y
    - **default**: 256
    - **description**: Maximum height this mob can fly to while being ridden
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### always-drop-full-exp
    - **default**: false
    - **description**: When true all valid ender dragon deaths will drop the full amount of experience orbs as if it were the first dragon death
* ##### bypass-mob-griefing
    - **default**: false
    - **description**: Set to true for the ender dragon to bypass the mob griefing gamerule
* ##### can-ride-vehicles
    - **default**: false
    - **description**: Set to true for the ender dragon to gain the ability to ride vehicles
* ##### attributes
    * ###### max_health
        - **default**: 200.0
        - **description**: Max health attribute
#### cave_spider
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### attributes
    * ###### max_health
        - **default**: 12.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### endermite
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### attributes
    * ###### max_health
        - **default**: 8.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### mooshroom
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### breeding-delay-ticks
    - **default**: 6000
    - **description**: The amount of ticks to wait before being able to breed again
* ##### attributes
    * ###### max_health
        - **default**: 10.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### polar_bear
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### breedable-item
    - **default**: ""
    - **description**: Item to tempt/feed polar bears and make them breed
* ##### breeding-delay-ticks
    - **default**: 6000
    - **description**: The amount of ticks to wait before being able to breed again
* ##### attributes
    * ###### max_health
        - **default**: 30.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### vindicator
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### johnny
    * ###### spawn-chance
        - **default**: 0.0
        - **description**: Percent chance (0.0 - 1.0) a vindicator named "Johnny" will spawn instead of a vindicator
* ##### attributes
    * ###### max_health
        - **default**: 24.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### zombie_horse
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### spawn-chance
    - **default**: 0.0
    - **description**: Percent chance (0.0 - 1.0) a zombie horse will spawn instead of a skeleton horse (natural spawns during thunderstorms)
* ##### attributes
    * ###### max_health
        * min
            - **default**: 15.0
            - **description**: Min health attribute
        * max
            - **default**: 15.0
            - **description**: Max health attribute
    * ###### jump_strength
        * min
            - **default**: 0.4
            - **description**: Min jump_strength attribute
        * max
            - **default**: 1.0
            - **description**: Max jump_strength attribute
    * ###### movement_speed
        * min
            - **default**: 0.2
            - **description**: Min movement_speed attribute
        * max
            - **default**: 0.2
            - **description**: Max movement_speed attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### wither
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### ridable-max-y
    - **default**: 256
    - **description**: Maximum height this mob can fly to while being ridden
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### can-ride-vehicles
    - **default**: false
    - **description**: Set to true for the wither to gain the ability to ride vehicles
* ##### play-spawn-sound
    - **default**: true
    - **description**: Play the wither's spawn sound globally when it is spawned
* ##### explosion-radius
    - **default**: 1.0
    - **description**: The explosion radius of a wither's projectile attack
* ##### health-regen-amount
    - **default**: 1.0
    - **description**: The regen amount of the wither
* ##### health-regen-delay
    - **default**: 20
    - **description**: How long to delay the health regen
* ##### bypass-mob-griefing
    - **default**: false
    - **description**: Set to true for withers to bypass the mob griefing gamerule
* ##### attributes
    * ###### max_health
        - **default**: 300.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### wither_skeleton
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### attributes
    * ###### max_health
        - **default**: 20.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### zombie_villager
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### cure
    * ###### enabled
        - **default**: true
        - **description**: Set to false to stop zombie villagers from being curable 
* ##### curing_time
    * ###### min
        - **default**: 3600
        - **description**: The minimum amount of ticks to randomly choose from when curing
    * ###### max
        - **default**: 6000
        - **description**: The maximum amount of ticks to randomly choose from when curing
* ##### jockey
    * ###### only-babies
        - **default**: true
        - **description**: Only babies can ride chickens
    * ###### chance
        - **default**: 0.05
        - **description**: Percent chance (0.0 - 1.0) of riding a chicken when spawned
    * ###### try-existing-chickens
        - **default**: true
        - **description**: Scan for existing chickens to spawn on
* ##### attributes
    * ###### max_health
        - **default**: 20.0
        - **description**: Max health attribute
    * ###### spawn_reinforcements
        - **default**: 0.1
        - **description**: Percent chance (0.0 - 1.0) this mob will spawn reinforcements
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### wandering_trader
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### can-be-leashed
    - **default**: false
    - **description**: Allow players to use leads on villagers (trader not included)
* ##### allow-trading
    - **default**: true
    - **description**: Set to false to disable trading with wandering traders
* ##### follow-emerald-blocks
    - **default**: false
    - **description**: Villagers will be tempted by emerald blocks and follow players holding them
* ##### attributes
    * ###### max_health
        - **default**: 20.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### silverfish
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### bypass-mob-griefing
    - **default**: false
    - **description**: Set to true for silverfish to bypass the mob griefing gamerule
* ##### attributes
    * ###### max_health
        - **default**: 8.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### zombified_piglin
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### count-as-player-kill-when-angry
    - **default**: true
    - **description**: Set to false to stop zombified piglins from dropping XP if they were angered (but not killed) by a player
* ##### jockey
    * ###### only-babies
        - **default**: true
        - **description**: Only babies can ride chickens
    * ###### chance
        - **default**: 0.05
        - **description**: Percent chance (0.0 - 1.0) of riding a chicken when spawned
    * ###### try-existing-chickens
        - **default**: true
        - **description**: Scan for existing chickens to spawn on
* ##### attributes
    * ###### max_health
        - **default**: 20.0
        - **description**: Max health attribute
    * ###### spawn_reinforcements
        - **default**: 0.0
        - **description**: Percent chance (0.0 - 1.0) this mob will spawn reinforcements
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### snow_golem
???+ info "The formula used to determine the amount of ticks between shots"
    ``` sh
    ((sqrt(distanceToTarget) / attack-distance) / snow-ball-modifier) * (max-shoot-interval-ticks - min-shoot-interval-ticks) + min-shoot-interval-ticks
    ```
    If `min-shoot-interval-ticks` and `max-shoot-interval-ticks` are both set to 0, snow golems won't shoot any snowballs.

* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### leave-trail-when-ridden
    - **default**: false
    - **description**: Leaves a trail where a snowman walks when being ridden
* ##### drops-pumpkin-when-sheared
    - **default**: true
    - **description**: Control if shearing a snowman makes the pumpkin drop to the ground
* ##### pumpkin-can-be-added-back
    - **default**: false
    - **description**: Control if pumpkins can be placed back onto snowmen
* ##### min-shoot-interval-ticks
    - **default**: 20
    - **description**: Min amount of interval ticks that get shot
* ##### max-shoot-interval-ticks
    - **default**: 20
    - **description**: Max amount of interval ticks that get shot
* ##### snow-ball-modifier
    - **default**: 10.0
    - **description**: The modifier value of snow-ball projectiles
* ##### attack-distance
    - **default**: 1.25
    - **description**: The distance at which the snow golem will attack
* ##### bypass-mob-griefing
    - **default**: false
    - **description**: Set to true for snow golems to bypass the mob griefing gamerule
* ##### takes-damage-from-water
    - **default**: true
    - **description**: Set to false for this mob to stop taking damage from water
* ##### attributes
    * ###### max_health
        - **default**: 4.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### skeleton_horse
* ##### can-swim
    - **default**: false
    - **description**: Can skeleton horses swim in water. False makes them sink to the bottom (vanilla default)
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### attributes
    * ###### max_health
        * min
            - **default**: 15.0
            - **description**: Min health attribute
        * max
            - **default**: 15.0
            - **description**: Max health attribute
    * ###### jump_strength
        * min
            - **default**: 0.4
            - **description**: Min jump_strength attribute
        * max
            - **default**: 1.0
            - **description**: Max jump_strength attribute
    * ###### movement_speed
        * min
            - **default**: 0.2
            - **description**: Min movement_speed attribute
        * max
            - **default**: 0.2
            - **description**: Max movement_speed attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### phantom
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### attacked-by-crystal-range
    - **default**: 0.0
    - **description**: Radius crystals scan for phantoms to attack. Value of 0 disables feature
* ##### attacked-by-crystal-damage
    - **default**: 1.0
    - **description**: Amount of damage per second crystals deal to phantoms. Value of 1.0 is half a heart
* ##### orbit-crystal-radius
    - **default**: 0.0
    - **description**: Radius which phantoms scan for crystals to orbit. Value of 0 disables feature
* ##### burn-in-light
    - **default**: 0
    - **description**: What light level the phantoms will burn at
* ##### burn-in-daylight
    - **default**: true
    - **description**: Whether phantoms burn in daylight or not
* ##### flames-on-swoop
    - **default**: false
    - **description**: Set to true for phantoms to shoot flames on swoop
* ##### ignore-players-with-torch
    - **default**: false
    - **description**: Whether phantoms avoid players with a torch in their hand
* ##### allow-griefing
    - **default**: false
    - **description**: Whether a phantom's flames can burn items
* ###### size
    * min
        - **default**: 0
        - **description**: Minimum size to randomly choose from when spawning naturally
    * max
        - **default**: 0
        - **description**: Maximum size to randomly choose from when spawning naturally
* ##### spawn
    * ###### min-sky-darkness
        - **default**: 5
        - **description**: The amount of darkness in the sky (5 is dark enough for thunderstorms, but not regular rain)
    * ###### only-above-sea-level
        - **default**: true
        - **description**: Only spawn on players above sea level
    * ###### only-with-visible-sky
        - **default**: true
        - **description**: Only spawn on players that have visible sky above them
    * ###### local-difficulty-chance
        - **default**: 3.0
        - **description**: Local difficulty must be greater than a random value chosen between 0.0 and this value
    * ###### per-attempt
        * min
            - **default**: 1
            - **description**: Minimum number of phantoms to spawn per attempt
        * max
            - **default**: -1
            - **description**: Maximum number of phantoms to spawn per attempt (Use -1 to base this off of world difficulty)
* ##### attributes
    * ###### max_health
        - **default**: 20.0
        - **description**: Max health attribute
    * ###### attack_damage
        - **default**: "6 + size"
        - **description**: The base value to set for the attack damage of the phantom
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### chicken
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### retaliate
    - **default**: false
    - **description**: If a chicken is hit, it will attack back
* ##### breeding-delay-ticks
    - **default**: 6000
    - **description**: The amount of ticks to wait before being able to breed again
* ##### attributes
    * ###### max_health
        - **default**: 4.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### creeper
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### encircle-target
    - **default**: false
    - **description**: Set to true for this mob to circle around the player as it ignites
* ##### allow-griefing
    - **default**: true
    - **description**: Set to false to stop the creeper from griefing.
* ##### bypass-mob-griefing
    - **default**: false
    - **description**: Set to true for creepers to bypass the mob griefing gamerule
* ##### naturally-charged-chance
    - **default**: 0.0
    - **description**: Percent chance (0.0 - 1.0) creepers are charged (powered) when spawning
* ##### explode-when-killed
    - **default**: false
    - **description**: Makes the creeper explode when killed
* ##### health-impacts-explosion
    - **default**: false
    - **description**: Makes the creeper's explosion be proportionate to the amount of health it has (lower health, weaker explosion)
* ##### attributes
    * ###### max_health
        - **default**: 10.0
        - **description**: Max health attribute
* ##### head-visibility-percent
    - **default**: 0.5
    - **description**: Increase or decrease the percentage to make the detection range of the mob smaller or larger when a player is wearing the mobs corresponding head
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### donkey
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### breeding-delay-ticks
    - **default**: 6000
    - **description**: The amount of ticks to wait before being able to breed again
* ##### attributes
    * ###### max_health
        * min
            - **default**: 15.0
            - **description**: Min health attribute
        * max
            - **default**: 30.0
            - **description**: Max health attribute
    * ###### jump_strength
        * min
            - **default**: 0.5
            - **description**: Min jump strength attribute
        * max
            - **default**: 0.5
            - **description**: Max jump strength attribute
    * ###### movement_speed
        * min
            - **default**: 0.175
            - **description**: Min movement speed attribute
        * max
            - **default**: 0.175
            - **description**: Max movement speed attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### cow
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### feed-mushrooms-for-mooshroom
    - **default**: 0
    - **description**: Number of mushrooms to feed a cow to make it transform into a mooshroom. Value of 0 disables feature
* ##### breeding-delay-ticks
    - **default**: 6000
    - **description**: The amount of ticks to wait before being able to breed again
* ##### naturally-aggressive-to-players
    * ###### chance
        - **default**: 0.0
        - **description**: Percent chance (0.0 - 1.0) this mob will spawn aggressive towards players
    * ###### damage
        - **default**: 2.0
        - **description**: The amount of damage it will do to players
* ##### attributes
    * ###### max_health
        - **default**: 10.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### enderman
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### allow-griefing
    - **default**: true
    - **description**: Set to false to stop the enderman from griefing
* ##### can-despawn-with-held-block
    - **default**: false
    - **description**: Makes the enderman despawn even if it's holding a block
* ##### ignore-projectiles
    - **default**: false
    - **description**: Stops the enderman from being immune to projectiles
* ##### bypass-mob-griefing
    - **default**: false
    - **description**: Set to true for enderman to bypass the mob griefing gamerule
* ##### takes-damage-from-water
    - **default**: true
    - **description**: Set to false for this mob to stop taking damage from water
* ##### aggressive-towards-endermites
    - **default**: true
    - **description**: Set to false to stop enderman from being aggro towards *all* types of spawned endermites 
* ##### aggressive-towards-endermites-only-spawned-by-player-thrown-ender-pearls
    - **default**: false
    - **description**: Set to true to make enderman aggro towards endermites *only* if they've been spawned by a player thrown ender pearl. This option does nothing if `aggressive-towards-endermites` is false
* ##### ignore-players-wearing-dragon-head
    - **default**: false
    - **description**: Set to true to make enderman ignore players that wear the dragon head
* ##### disable-player-stare-aggression
    - **default**: false
    - **description**: Set to true to stop an enderman from going aggro by a player looking into the enderman's eyes
* ##### attributes
    * ###### max_health
        - **default**: 40.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### evoker
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### bypass-mob-griefing
    - **default**: false
    - **description**: Set to true for evokers to bypass the mob griefing gamerule
* ##### attributes
    * ###### max_health
        - **default**: 24.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### drowned
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### can-break-doors
    - **default**: false
    - **description**: Set to true to allow drowned to break doors
* ##### jockey
    * ###### only-babies
        - **default**: true
        - **description**: Only babies can ride chickens
    * ###### chance
        - **default**: 0.05
        - **description**: Percent chance (0.0 - 1.0) of riding a chicken when spawned
    * ###### try-existing-chickens
        - **default**: true
        - **description**: Scan for existing chickens to spawn on
* ##### attributes
    * ###### max_health
        - **default**: 20.0
        - **description**: Max health attribute
    * ###### spawn_reinforcements
        - **default**: 0.1
        - **description**: Percent chance (0.0 - 1.0) this mob will spawn reinforcements
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### pillager
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### bypass-mob-griefing
    - **default**: false
    - **description**: Set to true for pillagers to bypass the mob griefing gamerule
* ##### attributes
    * ###### max_health
        - **default**: 24.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### fox
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### tulips-change-type
    - **default**: false
    - **description**: Feeding a white/orange tulip changes type snow/regular
* ##### breeding-delay-ticks
    - **default**: 6000
    - **description**: The amount of ticks to wait before being able to breed again
* ##### bypass-mob-griefing
    - **default**: false
    - **description**: Set to true for foxes to bypass the mob griefing gamerule
* ##### attributes
    * ###### max_health
        - **default**: 10.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### giant
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### step-height
    - **default**: 2.0
    - **description**: How many blocks giants can walk up without having to jump
* ##### jump-height
    - **default**: 1.0
    - **description**: Jump height modifier. Default value of 1.0 makes giants jump about as high as their waist
* ##### movement-speed
    - **default**: 0.5
    - **description**: Movement speed attribute
* ##### attack-damage
    - **default**: 50.0
    - **description**: Attack damage (in half hearts)
* ##### have-ai
    - **default**: false
    - **description**: Control if giant zombies have AI instead of just standing there
* ##### have-hostile-ai
    - **default**: false
    - **description**: Control if giant zombies have hostile AI also
* ##### attributes
    * ###### max_health
        - **default**: 100.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### hoglin
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### breeding-delay-ticks
    - **default**: 6000
    - **description**: The amount of ticks to wait before being able to breed again
* ##### attributes
    * ###### max_health
        - **default**: 40.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### glow_squid
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### can-fly
    - **default**: false
    - **description**: Makes it so squids can fly, Oh my!
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### attributes
    * ###### max_health
        - **default**: 10.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
* ##### rainglow-mode
    - **default**: rainbow
    - **description**: Lets you change the colours of your glow squids. You can choose from the following options:
        ``` yaml
        Basic:
        - rainbow: red, orange, yellow, green, blue, indigo and violet.
        - all_colors: blue, red, green, pink, yellow, orange, indigo, purple, white, gray and black.
        - monochrome: white, grey, and black.
        - vanilla: just blue.
        
        Pride:
        - trans_pride: blue, white and pink.
        - lesbian_pride: red, orange, white, pink and purple.
        - bi_pride: blue, pink and purple.
        - pan_pride: pink, yellow and blue.
        - ace_pride: black, gray, white and purple.
        - aro_pride: black, gray, white and green.
        - genderfluid: blue, pink, purple, white and black.
        - enby_pride: yellow, white, black and purple.
        ```

???+ note "Note"
    Please note that you must have the [`Rainglow Fabric mod`](https://modrinth.com/mod/rainglow) installed on your client in order for this to work.

#### squid
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### immune-to-EAR
    - **default**: true
    - **description**: Makes this mob immune to EAR (Entity Activation Range - See spigot.yml)
* ##### water-offset-check
    - **default**: 0.0
    - **description**: Stops squids from floating on top of water
* ##### can-fly
    - **default**: false
    - **description**: Makes it so squids can fly, Oh my!
* ##### attributes
    * ###### max_health
        - **default**: 10.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### villager
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### bypass-mob-griefing
    - **default**: false
    - **description**: Ignores the `mobGriefing` gamerule and allows the villagers to drop items, allowing them to breed
* ##### can-be-leashed
    - **default**: false
    - **description**: Allow players to use leads on villagers (trader not included)
* ##### follow-emerald-blocks
    - **default**: false
    - **description**: Villagers will be tempted by emerald blocks and follow players holding them
* ##### allow-trading
    - **default**: true
    - **description**: Set to false to disable trading with villagers
* ##### display-trade-item
    - **default**: true
    - **description**: Set to false to stop the villager from displaying the trade item
* ##### lobotomize
    * ###### enabled
        - **default**: false
        - **description**: Lobotomizes the villager if it cannot move (Does not disable trading)
    * ###### check-interval
        - **default**: 100
        - **description**: The interval in ticks to check if a villager is lobotomized 
* ##### minimum-demand
    - **default**: 0
    - **description**: Addresses MC-163962 where villager demand decreases indefinitely. Paper adds a patch to fix this by preventing demand from going below zero. This option allows the minimum demand to be configurable.
* ##### can-breed
    - **default**: true
    - **description**: Whether villagers can breed or not
* ##### breeding-delay-ticks
    - **default**: 6000
    - **description**: The amount of ticks to wait before being able to breed again
* ##### clerics-farm-warts
    - **default**: false
    - **description**: Set to true for clerics to farm nether wart
* ##### cleric-wart-farmers-throw-warts-at-villagers
    - **default**: true
    - **description**: Set to false for clerics to not throw nether wart at other villagers
* ##### spawn-iron-golem
    * ###### radius
        - **default**: 0
        - **description**: Radius villagers search for existing iron golems before spawning more. Value of 0 disables features
    * ###### limit
        - **default**: 0
        - **description**: Maximum amount of iron golems villagers can spawn in configured radius
* ##### attributes
    * ###### max_health
        - **default**: 20.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### mule
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### breeding-delay-ticks
    - **default**: 6000
    - **description**: The amount of ticks to wait before being able to breed again
* ##### attributes
    * ###### max_health
        * min
            - **default**: 15.0
            - **description**: Min health attribute
        * max
            - **default**: 30.0
            - **description**: Max health attribute
    * ###### jump_strength
        * min
            - **default**: 0.5
            - **description**: Min jump strength attribute
        * max
            - **default**: 0.5
            - **description**: Max jump strength attribute
    * ###### movement_speed
        * min
            - **default**: 0.175
            - **description**: Min movement speed attribute
        * max
            - **default**: 0.175
            - **description**: Max movement speed attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### wolf
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### milk-cures-rabid-wolves
    - **default**: true
    - **description**: Set to false for rabid wolves to not be cured by milk
* ##### spawn-rabid-chance
    - **default**: 0.0
    - **description**: Percent chance (0.0 - 1.0) that a wolf will spawn as rabid
* ##### default-collar-color
    - **default**: RED
    - **description**: Set the default collar color when a wolf is tamed. [Available Colors]({{ project.javadoc }}/org/bukkit/Color.html)
* ##### breeding-delay-ticks
    - **default**: 6000
    - **description**: The amount of ticks to wait before being able to breed again
* ##### attributes
    * ###### max_health
        - **default**: 8.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### zoglin
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### attributes
    * ###### max_health
        - **default**: 40.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### ocelot
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### breeding-delay-ticks
    - **default**: 6000
    - **description**: The amount of ticks to wait before being able to breed again
* ##### attributes
    * ###### max_health
        - **default**: 10.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### shulker
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### change-color-with-dye
    - **default**: false
    - **description**: Lets you change the color of the shulker by right-clicking it with a dye
* ##### spawn-from-bullet:
    * ###### base-chance
        - **default**: 1.0
        - **description**: Base chance
    * ###### require-open-lid
        - **default**: true
        - **description**: Require shulkers to have their lid open to spawn from bullet
    * ###### nearby-range
        - **default**: 8.0
        - **description**: The nearby range to check for shulkers
    * ###### nearby-equation
        - **default**: `(nearby - 1) / 5.0`
        - **description**: The equation to use for calculating a shulker spawning from a bullet (`nearby` is the amount of shulker entities nearby) Make this blank to always spawn if there's a shulker nearby
    * ###### random-color
        - **default**: false
        - **description**: Set the shulker to a random color when spawned from a bullet
* ##### attributes
    * ###### max_health
        - **default**: 30.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### horse
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### breeding-delay-ticks
    - **default**: 6000
    - **description**: The amount of ticks to wait before being able to breed again
* ##### attributes
    * ###### max_health
        * min
            - **default**: 15.0
            - **description**: Min health attribute
        * max
            - **default**: 30.0
            - **description**: Max health attribute
    * ###### jump_strength
        * min
            - **default**: 0.4
            - **description**: Min jump strength attribute
        * max
            - **default**: 1.0
            - **description**: Max jump strength attribute
    * ###### movement_speed
        * min
            - **default**: 0.1125
            - **description**: Min movement speed attribute
        * max
            - **default**: 0.3375
            - **description**: Max movement speed attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### piglin
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### bypass-mob-griefing
    - **default**: false
    - **description**: Set to true for piglins to bypass the mob griefing gamerule
* ##### portal-spawn-modifier
    - **default**: 2000
    - **description**: Allows changing the modifier for the piglin spawn chance from a portal block
based on the world difficulty. [Read more here]({{ project.source }}/blob/61fc0a557fc0eedececd63d44d43ce6431bc23bb/patches/server/0167-Piglin-portal-spawn-modifier.patch)
* ##### attributes
    * ###### max_health
        - **default**: 16.0
        - **description**: Max health attribute
* ##### head-visibility-percent
    - **default**: 0.5
    - **description**: Increase or decrease the percentage to make the detection range of the mob smaller or larger when a player is wearing the mobs corresponding head
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### piglin_brute
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### attributes
    * ###### max_health
        - **default**: 50.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### skeleton
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### attributes
    * ###### max_health
        - **default**: 8.0
        - **description**: Max health attribute
* ##### head-visibility-percent
    - **default**: 0.5
    - **description**: Increase or decrease the percentage to make the detection range of the mob smaller or larger when a player is wearing the mobs corresponding head
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
* ##### feed-wither-roses
    - **default**: 0
    - **description**: Right-clicking a skeleton while holding a wither rose will convert the skeleton into a wither skeleton. With the value being how many wither roses you would need to convert the skeleton, and 0 meaning the feature is disabled.
* ##### bow-accuracy
    - **default**: 14 - difficulty * 4
    - **description**: Change the accuracy with which Skeletons shoot. The outcome of the formula is the divergence (spread). The higher the value, the less accurate the shot is.
      ``` yaml
      easy:   14 - 1 * 4 = 10
      normal: 14 - 2 * 4 = 6
      hard:   14 - 3 * 4 = 2
      ```
#### stray
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### attributes
    * ###### max_health
        - **default**: 20.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### goat
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### breeding-delay-ticks
    - **default**: 6000
    - **description**: The amount of ticks to wait before being able to breed again
* ##### attributes
    * ###### max_health
        - **default**: 10.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### panda
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### breeding-delay-ticks
    - **default**: 6000
    - **description**: The amount of ticks to wait before being able to breed again
* ##### attributes
    * ###### max_health
        - **default**: 20.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### strider
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### give-saddle-back
    - **default**: false
    - **description**: Sneak and right-click a strider with a saddle on it's back to remove it with this option enabled
* ##### breeding-delay-ticks
    - **default**: 6000
    - **description**: The amount of ticks to wait before being able to breed again
* ##### takes-damage-from-water
    - **default**: true
    - **description**: Set to false for this mob to stop taking damage from water
* ##### attributes
    * ###### max_health
        - **default**: 20.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### rabbit
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### spawn-killer-rabbit-chance
    - **default**: 0.0
    - **description**: Percent chance (0.0-1.0) the killer rabbit naturally spawns
* ##### spawn-toast-chance
    - **default**: 0.0
    - **description**: Percent chance (0.0-1.0) to naturally spawn a rabbit named Toast
* ##### breeding-delay-ticks
    - **default**: 6000
    - **description**: The amount of ticks to wait before being able to breed again
* ##### bypass-mob-griefing
    - **default**: false
    - **description**: Set to true for rabbits to bypass the mob griefing gamerule
* ##### attributes
    * ###### max_health
        - **default**: 3.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### husk
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### jockey
    * ###### only-babies
        - **default**: true
        - **description**: Only babies can ride chickens
    * ###### chance
        - **default**: 0.05
        - **description**: Percent chance (0.0 - 1.0) of riding a chicken when spawned
    * ###### try-existing-chickens
        - **default**: true
        - **description**: Scan for existing chickens to spawn on
* ##### attributes
    * ###### max_health
        - **default**: 20.0
        - **description**: Max health attribute
    * ###### spawn_reinforcements
        - **default**: 0.1
        - **description**: Percent chance (0.0 - 1.0) this mob will spawn reinforcements
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### spider
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### attributes
    * ###### max_health
        - **default**: 16.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### sheep
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### breeding-delay-ticks
    - **default**: 6000
    - **description**: The amount of ticks to wait before being able to breed again
* ##### bypass-mob-griefing
    - **default**: false
    - **description**: Set to true for sheep to bypass the mob griefing gamerule
* ##### attributes
    * ###### max_health
        - **default**: 8.0
        - **description**: Max health attribute
* ##### jeb-shear-random-color
    - **default**: false
    - **description**: Shearing a sheep named jeb_ will drop a wool block with a random colour
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### ravager
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### bypass-mob-griefing
    - **default**: false
    - **description**: Set to true for ravagers to bypass the mob griefing gamerule
* ##### griefable-blocks
    - **default**:
        ``` yaml
        - minecraft:oak_leaves
        - minecraft:spruce_leaves
        - minecraft:birch_leaves
        - minecraft:jungle_leaves
        - minecraft:acacia_leaves
        - minecraft:dark_oak_leaves
        - minecraft:beetroots
        - minecraft:carrots
        - minecraft:potatoes
        - minecraft:wheat
        ```
    - **description**: Whitelist of blocks that can be broken by the ravager
* ##### attributes
    * ###### max_health
        - **default**: 100.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### pig
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### give-saddle-back
    - **default**: false
    - **description**: Sneak and right-click a pig with a saddle on it's back to remove it with this option enabled
* ##### breeding-delay-ticks
    - **default**: 6000
    - **description**: The amount of ticks to wait before being able to breed again
* ##### attributes
    * ###### max_health
        - **default**: 10.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### witch
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### attributes
    * ###### max_health
        - **default**: 26.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### zombie
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### jockey
    * ###### only-babies
        - **default**: true
        - **description**: Only babies can ride chickens
    * ###### chance
        - **default**: 0.05
        - **description**: Percent chance (0.0 - 1.0) of riding a chicken when spawned
    * ###### try-existing-chickens
        - **default**: true
        - **description**: Scan for existing chickens to spawn on
* ##### aggressive-towards-villager-when-lagging
    - **default**: true
    - **description**: Set to false to stop zombie aggressiveness towards villagers when lagging
* ##### bypass-mob-griefing
    - **default**: false
    - **description**: Set to true for zombies to bypass the mob griefing gamerule
* ##### attributes
    * ###### max_health
        - **default**: 20.0
        - **description**: Max health attribute
    * ###### spawn_reinforcements
        - **default**: 0.1
        - **description**: Percent chance (0.0 - 1.0) this mob will spawn reinforcements
* ##### head-visibility-percent
    - **default**: 0.5
    - **description**: Increase or decrease the percentage to make the detection range of the mob smaller or larger when a player is wearing the mobs corresponding head
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### dolphin
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### naturally-aggressive-to-players-chance
    - **default**: 0.0
    - **description**: Percent chance (0.0 - 1.0) this mob will spawn aggressive towards players
* ##### disable-treasure-searching
    - **default**: false
    - **description**: Stops the dolphin from treasure hunting
* ##### spit
    * ###### cooldown
        - **default**: 20
        - **description**: The cooldown of the dolphin spit
    * ###### speed
        - **default**: 1.0
        - **description**: The speed of the dolphin spit
    * ###### damage
        - **default**: 2.0
        - **description**: The damage of the dolphin spit
* ##### attributes
    * ###### max_health
        - **default**: 10.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### axolotl
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### breeding-delay-ticks
    - **default**: 6000
    - **description**: The amount of ticks to wait before being able to breed again
* ##### attributes
    * ###### max_health
        - **default**: 14.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### bat
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### ridable-max-y
    - **default**: 256
    - **description**: Maximum height this mob can fly to while being ridden
* ##### attributes
    * ###### max_health
        - **default**: 6.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### bee
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### ridable-max-y
    - **default**: 256
    - **description**: Maximum height this mob can fly to while being ridden
* ##### breeding-delay-ticks
    - **default**: 6000
    - **description**: The amount of ticks to wait before being able to breed again
* ##### can-work-at-night
    - **default**: false
    - **description**: Controls whether bees can work during the night
* ##### can-work-in-rain
    - **default**: false
    - **description**: Controls whether bees can work during rainy weather
* ##### dies-after-sting
    - **default**: true
    - **description**: Set whether a bee should die after stinging
* ##### attributes
    * ###### max_health
        - **default**: 10.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### blaze
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### ridable-max-y
    - **default**: 256
    - **description**: Maximum height this mob can fly to while being ridden
* ##### takes-damage-from-water
    - **default**: true
    - **description**: Set to false for this mob to stop taking damage from water
* ##### attributes
    * ###### max_health
        - **default**: 20.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### cat
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### default-collar-color
    - **default**: RED
    - **description**: Set the default collar color when a cat is tamed. [Available Colors]({{ project.javadoc }}/org/bukkit/Color.html)
* ##### spawn-delay
    - **default**: 1200
    - **description**: Number of ticks between attempting to naturally spawn a cat
* ##### scan-range-for-other-cats
    * ###### swamp-hut
        - **default**: 16
        - **description**: Do not spawn a cat if another cat is found within this range. Set to 0 to disable
    * ###### village
        - **default**: 48
        - **description**: Do not spawn a cat if another cat is found within this range. Set to 0 to disable
* ##### breeding-delay-ticks
    - **default**: 6000
    - **description**: The amount of ticks to wait before being able to breed again
* ##### attributes
    * ###### max_health
        - **default**: 10.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### cod
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### attributes
    * ###### max_health
        - **default**: 3.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### elder_guardian
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### attributes
    * ###### max_health
        - **default**: 80.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### ghast
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### ridable-max-y
    - **default**: 256
    - **description**: Maximum height this mob can fly to while being ridden
* ##### allow-griefing
    - **default**: true
    - **description**: Set to false to stop the ghast from griefing
* ##### attributes
    * ###### max_health
        - **default**: 10.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### guardian
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### attributes
    * ###### max_health
        - **default**: 30.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### illusioner
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### naturally-spawn
    - **default**: false
    - **description**: Control if illusioners naturally spawn in the game
* ##### movement-speed
    - **default**: 0.5
    - **description**: Movement speed attribute
* ##### follow-range
    - **default**: 18.0
    - **description**: Follow range attribute
* ##### attributes
    * ###### max_health
        - **default**: 32.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### iron_golem
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### healing-calms-anger
    - **default**: false
    - **description**: Calms the iron golem when it's healed if it's angry
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### can-spawn-in-air
    - **default**: false
    - **description**: Set whether iron golems can spawn in the air, like in 1.12 and below
* ##### can-swim
    - **default**: false
    - **description**: Set whether iron golems can swim or not
* ##### poppy-calms-anger
    - **default**: false
    - **description**: Giving the iron golem a poppy calms it down when it's angry
* ##### attributes
    * ###### max_health
        - **default**: 100.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### llama
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable. Llama's must be tamed and saddled (with carpet) to be WASD controllable.
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### breeding-delay-ticks
    - **default**: 6000
    - **description**: The amount of ticks to wait before being able to breed again
* ##### join-caravans
    - **default**: true
    - **description**: Set to false to disable the [llama caravan feature](https://minecraft.gamepedia.com/Llama#Leading)
* ##### attributes
    * ###### max_health
        * min
            - **default**: 15.0
            - **description**: Min health attribute
        * max
            - **default**: 30.0
            - **description**: Max health attribute
    * ###### jump_strength
        * min
            - **default**: 0.5
            - **description**: Min jump strength attribute
        * max
            - **default**: 0.5
            - **description**: Max jump strength attribute
    * ###### movement_speed
        * min
            - **default**: 0.175
            - **description**: Min movement speed attribute
        * max
            - **default**: 0.175
            - **description**: Max movement speed attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### trader_llama
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable.
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable. Trader llama's must be tamed to be WASD controllable. Being saddled (carpet) is not a requirement since it technically always has a carpet.
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### breeding-delay-ticks
    - **default**: 6000
    - **description**: The amount of ticks to wait before being able to breed again
* ##### attributes
    * ###### max_health
        * min
            - **default**: 15.0
            - **description**: Min health attribute
        * max
            - **default**: 30.0
            - **description**: Max health attribute
    * ###### jump_strength
        * min
            - **default**: 0.5
            - **description**: Min jump strength attribute
        * max
            - **default**: 0.5
            - **description**: Max jump strength attribute
    * ###### movement_speed
        * min
            - **default**: 0.175
            - **description**: Min movement speed attribute
        * max
            - **default**: 0.175
            - **description**: Max movement speed attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### magma_cube
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### attributes
    * ###### max_health
        - **default**: "size * size"
        - **description**: The Max health equation used to calculate the max health
    * ###### attack_damage
        - **default**: "size"
        - **description**: The base value to set for the attack damage of the magma cube
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### parrot
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### ridable-max-y
    - **default**: 256
    - **description**: Maximum height this mob can fly to while being ridden
* ##### can-breed
    - **default**: false
    - **description**: Gives parrots the ability to breed using any type of seeds (baby parrots don't exist D:, so "adult" parrots pop out)
* ##### attributes
    * ###### max_health
        - **default**: 6.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### pufferfish
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### attributes
    * ###### max_health
        - **default**: 3.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### salmon
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### attributes
    * ###### max_health
        - **default**: 3.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### slime
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### attributes
    * ###### max_health
        - **default**: "size * size"
        - **description**: The Max health equation used to calculate the max health
    * ###### attack_damage
        - **default**: "size"
        - **description**: The base value to set for the attack damage of the slime
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### tropical_fish
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### attributes
    * ###### max_health
        - **default**: 3.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### turtle
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### breeding-delay-ticks
    - **default**: 6000
    - **description**: The amount of ticks to wait before being able to breed again
* ##### attributes
    * ###### max_health
        - **default**: 30.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### vex
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### takes-damage-from-water
    - **default**: false
    - **description**: Set to true for this mob to start taking damage from water
* ##### ridable-max-y
    - **default**: 256
    - **description**: Maximum height this mob can fly to while being ridden
* ##### attributes
    * ###### max_health
        - **default**: 14.0
        - **description**: Max health attribute
* ##### always-drop-exp
    - **default**: false
    - **description**: Set to true if this mob should always drop experience
#### camel
* ##### breeding-delay-ticks
    - **default**: 6000
    - **description**: The amount of ticks to wait before being able to breed again
* ##### attributes
    * ###### max_health
        * min
            - **default**: 32.0
            - **description**: Min health attribute
        * max
            - **default**: 32.0
            - **description**: Max health attribute
    * ###### jump_strength
        * min
            - **default**: 0.42
            - **description**: Min jump strength attribute
        * max
            - **default**: 0.42
            - **description**: Max jump strength attribute
    * ###### movement_speed
        * min
            - **default**: 0.09
            - **description**: Min movement speed attribute
        * max
            - **default**: 0.09
            - **description**: Max movement speed attribute
#### sniffer
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable
* ##### controllable
    - **default**: true
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob mountable in water (it wont eject you)
* ##### breeding-delay-ticks
    - **default**: 6000
    - **description**: The amount of ticks to wait before being able to breed again
* ##### attributes
    * ###### max_health
    - **default**: 14.0
    - **description**: Max health attribute

### gameplay-mechanics

#### arrow
* ##### movement-resets-despawn-counter
    - **default**: true
    - **description**: Setting this to false prevents keeping arrows alive indefinitely (such as when the block the arrow is stuck in gets removed, like a piston head going up/down).
#### use-better-mending
- **default**: false
- **description**: Set to true for mending enchantment to always repair the most damaged equipment first
#### mending-multiplier
- **default**: 1.0
- **description**: How effective mending is at repairing items, higher values mean less xp is used to repair items. (1.0 = 100%)
#### mobs-ignore-rails
- **default**: false
- **description**: Set to true to allow mobs to walk over rails
#### rain-stops-after-sleep
- **default**: true
- **description**: Set to false to make rain continue even after a player sleeps
#### thunder-stops-after-sleep
- **default**: true
- **description**: Set to false to make thunder continue even after a player sleeps
#### mob-last-hurt-by-player-time
- **default**: 100
- **description**: Allows you to change the amount of ticks required for a mob's death to count as a player kill after being hurt by the player (projectile or directly)
#### halloween
* ##### force
    - **default**: false
    - **description**: Set to true to force the world into halloween
* ##### head-chance
    - **default**: 0.25
    - **description**: Percent chance (0.0 - 1.0) a zombie or skeleton will spawn with a jack o' lantern/carved pumpkin on it's head
#### mob-effects
* ##### health-regen-amount
    - **default**: 1.0
    - **description**: The amount at which this effect affects entities
* ##### minimal-health-poison-amount
    - **default**: 1.0
    - **description**: The amount at which this effect affects entities
* ##### poison-degeneration-amount
    - **default**: 1.0
    - **description**: The amount at which this effect affects entities
* ##### wither-degeneration-amount
    - **default**: 1.0
    - **description**: The amount at which this effect affects entities
* ##### hunger-exhaustion-amount
    - **default**: 0.005
    - **description**: The amount at which this effect affects entities
* ##### saturation-regen-amount
    - **default**: 1.0
    - **description**: The amount at which this effect affects entities
#### projectiles-bypass-mob-griefing
* **default**: false
* **description**: Set to true for projectiles to bypass the mob griefing gamerule
#### projectile-offset
* ##### bow
    - **default**: 1.0
    - **description**: The projectile offset of a bow
* ##### crossbow
    - **default**: 1.0
    - **description**: The projectile offset of a crossbow
* ##### egg
    - **default**: 1.0
    - **description**: The projectile offset of an egg
* ##### ender-pearl
    - **default**: 1.0
    - **description**: The projectile offset of an ender-pearl
* ##### throwable-potion
    - **default**: 1.0
    - **description**: The projectile offset of a throwable-potion
* ##### trident
    - **default**: 1.0
    - **description**: The projectile offset of a trident
* ##### snowball
    - **default**: 1.0
    - **description**: The projectile offset of a snowball
#### drowning
* ##### air-ticks
    - **default**: 300
    - **description**: How long you can breathe underwater before you start drowning
* ##### ticks-per-damage
    - **default**: 20
    - **description**: Amount of ticks between the drowning damage
* ##### damage-from-drowning
    - **default**: 2.0
    - **description**: Amount of damage done while drowning
#### tick-fluids
- **default**: true
- **description**: Set to false to stop fluids from ticking. [Screenshot of a simple plugin that uses this option](https://media.discordapp.net/attachments/595431462510002206/821169659382333440/unknown.png). Attachment: [FreezeFluids-1.0.jar](https://cdn.discordapp.com/attachments/720375089123688488/820951359519326218/FreezeFluids-1.0.jar)
#### disable-drops-on-cramming-death
- **default**: false
- **description**: Stops entities from dropping loot on death, if killed by cramming gamerule
#### entity-blindness-multiplier
- **default**: 1
- **description**: How blind a mob is when affected with the blindness potion effect
#### entities-pick-up-loot-bypass-mob-griefing
- **default**: false
- **description**: Mobs that can pick up loot will continue to pick up loot even if the `mobGriefing` gamerule is disabled
#### milk-cures-bad-omen
- **default**: true
- **description**: Allow players to drink milk to cure bad omen status effect
#### milk-clears-beneficial-effects
- **default**: true
- **description**: Set to false to have milk clear only negative status effects
#### trident-loyalty-void-return-height
- **default**: 0.0
- **description**: The void height at which a trident with loyalty will return to it's thrower. A value of 0.0 or higher disables this feature.
#### void-damage-dealt
- **default**: 4.0
- **description**: The amount of void damage dealt
#### void-damage-height
- **default**: -64.0
- **description**: The height at which void damage begins
#### clamp-explosion-radius
- **default**: true
- **description**: Set to false to allow setting a negative `ExplosionRadius` value on explosions
#### entity-lifespan
- **default**: 0
- **description**: Disabled by default (0), Amount of ticks an entity will live before disappearing. Interacting with a player resets the timer
#### silk-touch
Requires the [`purpur.drop.spawners`](permissions#purpurdropspawners) and [`purpur.place.spawners`](permissions#purpurplacespawners) permissions

* ##### enabled
    - **default**: false
    - **description**: Makes it so you can mine spawners using a tool with silk touch
* ##### minimal-level
    - **default**: 1
    - **description**: The minimal level of the Silktouch enchantment required to pick up mined spawners
* ##### tools
    - **default**:
    ``` yaml
    - minecraft:iron_pickaxe
    - minecraft:golden_pickaxe
    - minecraft:diamond_pickaxe
    - minecraft:netherite_pickaxe
    ```
    - **description**: Whitelist of tools that can mine spawners with silk touch
* ##### spawner-name
    - **default**: "&lt;reset>&lt;white>Monster Spawner"
    - **description**: The name of the spawner
* ##### spawner-lore
    - **default**:
        ``` yaml
        - Spawns a <mob>
        ```
    - **description**: The lore of the spawner
#### boat
* ##### eject-players-on-land
    - **default**: false
    - **description**: Set to true for boats to eject players when on land
* ##### do-fall-damage
    - **default**: false
    - **description**: Set to false for boats to not do fall damage to players
#### armorstand
* ##### step-height
    - **default**: 0.0
    - **description**: Set the default step height of armorstands. Useful for plugins that utilize armorstands as vehicles to be able to drive over blocks without jumping, etc
* ##### set-name-visible-when-placing-with-custom-name
    - **default**: true
    - **description**: Makes the name visible when placing with a custom name
* ##### fix-nametags
    - **default**: false
    - **description**: Makes the name visible when using a Name Tag on an Armor Stand
* ##### place-with-arms-visible
    - **default**: false
    - **description**: Makes the arms visible when placed
* ##### can-movement-tick
    - **default**: true
    - **description**: Set to false to disallow armorstands from moving
* ##### can-move-in-water
    - **default**: true
    - **description**: Set to false to disallow armorstands from moving in water
* ##### can-move-in-water-over-fence
    - **default**: true
    - **description**: Set to false to disallow armorstands from moving in water over a fence
#### player
* ##### exp-pickup-delay-ticks
    - **default**: 2
    - **description**: The delay a player can pick up experience after it is dropped
* ##### shift-right-click-repairs-mending-points
    - **default**: 0
    - **description**: The amount of experience points to use from the player's bar for repairing items enchanted with mending in the player's inventory
* ##### spawn-invulnerable-ticks
    - **default**: 60
    - **description**: Gives you the ability to control how long a player is invulnerable when they first spawn in.
* ##### invulnerable-while-accepting-resource-pack
    - **default**: false
    - **description**: Sets the player as invulnerable while they download the resource pack.
* ##### teleport-if-outside-border
    - **default**: false
    - **description**: Teleports you to spawn if you somehow get outside the world border
* ##### teleport-on-nether-ceiling-damage
    - **default**: false
    - **description**: Teleports you to spawn if you take damage while on top of the nether ceiling
* ##### allow-void-trading
    - **default**: false
    - **description**: Allows the ability to continuously trade with a villager through an End Gateway exploit.
* ##### totem-of-undying-works-in-inventory
    - **default**: false
    - **description**: Allows the totem of undying to work anywhere in your inventory, not just your offhand
* ##### ridable-in-water
    - **default**: false
    - **description**: Lets mobs/players ride on players if the player is in the water
* ##### fix-stuck-in-portal
    - **default**: false
    - **description**: If the player is stuck inside a portal with no way of getting out, walking to another block will reset the portal cooldown, allowing them to teleport back through the portal
* ##### one-punch-in-creative
    - **default**: false
    - **description**: If the player is in creative and hits an entity with an empty hand, the entity instantly dies
* ##### sleep-ignore-nearby-mobs
    - **default**: false
    - **description**: Set to true to allow sleep even if there are mobs nearby
* ##### can-skip-night
    - **default**: true
    - **description**: Set to false to disable the players' ability to skip the night by sleeping
* ##### critical-damage-multiplier
    - **default**: 1.5
    - **description**: The percentage of damage a critical attack adds to the base damage
* ##### burp-when-full
    - **default**: false
    - **description**: Plays a burp sound after a player fills the hunger bar completely by eating
* ##### burp-delay
    - **default**: 10
    - **description**: Amount of ticks to delay sound; `burp-when-full` option must be enabled
* ##### portal-wait-time
    - **default**: 80
    - **description**: Amount of ticks to wait before letting the player teleport through the portal
* ##### creative-portal-wait-time
    - **default**: 1
    - **description**: Amount of ticks to wait before letting the creative player teleport through the portal
* ##### curse-of-binding
    * ###### remove-with-weakness
        - **default**: false
        - **description**: Allows the player to remove curse of binding armor when they have a weakness effect applied to them
* ##### idle-timeout
    * ###### kick-if-idle
        - **default**: true
        - **description**: Kick players if they become idle (see server.properties for player-idle-timeout time)
    * ###### tick-nearby-entities
        - **default**: true
        - **description**: Should entities tick normally when nearby players are AFK. False will require at least 1 non-AFK player in order to tick
    * ###### mobs-target
        - **default**: true
        - **description**: Should mobs target nearby AFK players
    * ###### count-as-sleeping
        - **default**: false
        - **description**: Should AFK players count as sleeping? (allows active players to skip night by sleeping, even if AFK players are not in bed)
    * ###### update-tab-list
        - **default**: false
        - **description**: Should AFK players have their name updated in the tab list (puts `[AFK]` in front of their name)
* ##### exp-dropped-on-death
    * ###### equation
        - **default**: expLevel * 7
        - **description**: How much exp to drop on death. Available NMS variables are `expLevel`, `expTotal`, and `exp`
    * ###### maximum
        - **default**: 100
        - **description**: Maximum amount of exp value to drop on death
* ##### netherite-fire-resistance
    * ###### duration
        - **default**: 0
        - **description**: Set how long the fire resistance lasts. Set to 0 to disable
    * ###### amplifier
        - **default**: 0
        - **description**: Set the amplifier for the fire resistance effect
    * ###### ambient
        - **default**: false
        - **description**: Set to true for the particle effects to be less intrusive on the screen
    * ###### show-particles
        - **default**: false
        - **description**: Set to true for the fire resistance potion effect to show particles
    * ###### show-icon
        - **default**: true
        - **description**: Set to false for the fire resistance effect to not display it's icon
#### minecart
* ##### max-speed
    - **default**: 0.4
    - **description**: Max speed of a minecart when controlled
* ##### place-anywhere
    - **default**: false
    - **description**: Whether minecarts can be placed anywhere, not just on rails
* ##### powered-rail
    * ###### boost-modifier
        - **default**: 0.06
        - **description**: the speed boost that minecarts gain from hitting a powered rail (Doesn't affect furnace minecarts)
* ##### controllable
    * ###### enabled
        - **default**: false
        - **description**: Whether minecarts can be controlled when not on rails
    * ###### fall-damage
        - **default**: true
        - **description**: Set to true to give fall damage to the player while in a minecart
    * ###### step-height
        - **default**: 1.0
        - **description**: The step height in which a minecarts can go up to the next block without jumping
    * ###### hop-boost
        - **default**: 0.5
        - **description**: Jump power when pressing spacebar on a controllable minecart
    * ###### base-speed
        - **default**: 0.1
        - **description**: Base speed of minecart when controlled
    * ###### block-speed
        - **default**:
            ``` yaml
            grass_block: 0.3
            stone: 0.5
            ```
        - **description**: List of speed overrides per block type
#### item
* ##### end-crystal
    * ###### place-anywhere
        - **default**: false
        - **description**: Allows you to place an end crystal on any block, not just obsidian and bedrock
* ##### shears
    * ###### damage-if-sprinting
        - **default**: false
        - **description**: Holding shears while sprinting will randomly damage the player (Don't run with scissors!)
    * ###### ignore-in-water
        - **default**: false
        - **description**: Should damage be ignored while in water if `damage-if-sprinting` is enabled
    * ###### ignore-in-lava
        - **default**: false
        - **description**: Should damage be ignored while in lava if `damage-if-sprinting` is enabled
    * ###### sprinting-damage
        - **default**: 1
        - **description**: The amount of damage to give if `damage-if-sprinting` is enabled
    * ###### defuse-tnt-chance
        - **default**: 0.0
        - **description**: Percent chance (0.0 - 1.0) that right-clicking primed TNT will defuse it
* ##### snowball
    * ###### extinguish
        * ###### fire
            - **default**: false
            - **description**: Whether snowballs, when thrown, should extinguish fires
        * ###### candles
            - **default**: false
            - **description**: Whether snowballs, when thrown, should extinguish candles
        * ###### campfires
            - **default**: false
            - **description**: Whether snowballs, when thrown, should extinguish campfires
* ##### shulker_box
    * ###### drop-contents-when-destroyed
        - **default**: true
        - **description**: Whether the shulker box should drop it's contents when it's been destroyed
* ##### compass
    * ###### holding-shows-bossbar
        - **default**: false
        - **description**: If the bossbar from the [`/compass`](commands#compass) command should show when holding a compass
* ##### glow_berries
    * ###### eat-glow-duration
        - **default**: 0
        - **description**: Amount of ticks the player will glow after eating a glow berry. Set to 0 to disable
* ##### ender-pearl
    * ###### damage
        - **default**: 5
        - **description**: The amount of damage to take after teleporting using an ender pearl
    * ###### cooldown
        - **default**: 20
        - **description**: The cooldown after using an ender pearl (in ticks)
    * ###### creative-cooldown
        - **default**: 20
        - **description**: The cooldown after using an ender pearl while in creative (in ticks)
    * ###### endermite-spawn-chance
        - **default**: 0.05
        - **description**: Percent chance (0.0 - 1.0) an endermite will spawn after teleporting using an ender pearl
* ##### immune
    * ###### explosion
        - **default**: []
        - **description**: List of items that are immune to explosions
    * ###### fire
        - **default**: []
        - **description**: List of items that are immune to fire
    * ###### lightning
        - **default**: []
        - **description**: List of items that are immune to lightning
    * ###### cactus
        - **default**: []
        - **description**: List of items that are immune to cactus
    ???+ note "Example of item immune list:"
        ``` yaml
        explosion:
          - minecraft:diamond
          - minecraft:diamond_block
          - minecraft:diamond_sword
        ```

???+ warning "Warning"
    These item immune lists can cause client desync issues, such as invisible items on the ground! There is nothing that can be done about that from the server-side code.

#### elytra
* ##### damage-per-second
    - **default**: 1
    - **description**: How much damage an elytra's durability takes during flight each second
* ##### damage-multiplied-by-speed
    - **default**: 0.0
    - **description**: Damage is multiplied by speed if flight is faster than set speed. Value of 0 disables this multiplier
* ##### kinetic-damage
    - **default**: true
    - **description**: Should players take damage when flying into a wall
* ##### ignore-unbreaking
    - **default**: false
    - **description**: Should elytras ignore the unbreaking enchantment
* ##### damage-per-boost
    * ###### firework
        - **default**: 0
        - **description**: How much damage to deal to the elytra when firework boost activates
    * ###### trident
        - **default**: 0
        - **description**: How much damage to deal to the elytra when trident riptide boost activates
#### mob-spawning
* ##### village-cats
    - **default**: default
    - **description**: Set to true to spawn in the world that this option is a part of
* ##### raid-patrols
    - **default**: default
    - **description**: Set to true to spawn in the world that this option is a part of
* ##### phantoms
    - **default**: default
    - **description**: Set to true to spawn in the world that this option is a part of
* ##### wandering-traders
    - **default**: default
    - **description**: Set to true to spawn in the world that this option is a part of
* ##### village-sieges
    - **default**: default
    - **description**: Set to true to spawn in the world that this option is a part of
* ##### ignore-creative-players
    - **default**: false
    - **description**: Option to choose whether or not to ignore creative players when spawning mobs.
#### raid-cooldown-seconds
- **default**: 0
- **description**: How long you should wait before another raid can be initiated
#### entities-can-use-portals
- **default**: true
- **description**: Set to false to stop entities from being able to use portals
#### persistent-tileentity-display-names-and-lore
- **default**: false
- **description**: Set to true to make TE's display names and lores persist after breaking (ex. named custom player heads retain their name)
#### persistent-droppable-entity-display-names
- **default**: true
- **description**: Set to true to make entity's display names and lores persist after breaking (ex. named armor stands retain their name)
#### infinity-bow
* ##### normal-arrows
    - **default**: true
    - **description**: Set to true to make the Infinity enchantment work on this arrow type
* ##### spectral-arrows
    - **default**: false
    - **description**: Set to true to make the Infinity enchantment work on this arrow type
* ##### tipped-arrows
    - **default**: false
    - **description**: Set to true to make the Infinity enchantment work on this arrow type
* ##### works-without-arrows
    - **default**: false
    - **description**: Set to true for the infinity bow to work without arrows
#### daylight-cycle-ticks
* ##### daytime
    - **default**: 12000
    - **description**: Set how long the daylight cycle is ticked
* ##### nighttime
    - **default**: 12000
    - **description**: Set how long the nighttime cycle is ticked
#### animal-breeding-cooldown-seconds
- **default**: 0
- **description**: Adds a cooldown to breeding animals per animal type
#### projectile-damage
* ##### snowball
    - **default**: -1
    - **description**: Set how much damage a snowball does (-1 will make damage be 3 for blazes & 0 for all other entities which is default)
#### entity-left-handed-chance
- **default**: 0.05
- **description**: Percent chance (0.0 - 1.0) an entity will spawn left-handed
#### fireballs-bypass-mob-griefing
- **default**: false
- **description**: Set to true for fireballs to bypass the mob griefing gamerule
#### note-block-ignore-above
- **default**: false
- **description**: Set to true for note blocks to continue making sound even if there is a block above it
#### impose-teleport-restrictions-on-gateways
- **default**: false
- **description**: Set to true to impose teleport restrictions on gateways. This broadcasts the `EntityTeleportHinderedEvent` event which gives the ability to retry teleports if they fail due to having passengers/being vehicles
#### always-tame-in-creative
- **default**: false
- **description**: Set to true to have 100% chance of taming a mob
#### shovel-turns-block-to-grass-path
- **default**:
    ``` yaml
    - minecraft:coarse_dirt
    - minecraft:dirt
    - minecraft:grass_block
    - minecraft:mycelium
    - minecraft:podzol
    - minecraft:rooted_dirt
    ```
- **description**: List of blocks that can be turned into a grass path when right-clicked with a shovel

### ridable-settings

#### babies-are-ridable
- **default**: true
- **description**: Set to false to stop babies from being ridable
#### untamed-tamables-are-ridable
- **default**: true
- **description**: Set to false to stop untamed tamables from being ridable
#### use-night-vision
- **default**: false
- **description**: Set to true to give night vision to riders while on a ridable
#### use-dismounts-underwater-tag
- **default**: true
- **description**: Set to false to use `<mob>.ridable-in-water` options instead of the [`DISMOUNTS_UNDERWATER`](https://minecraft.fandom.com/wiki/Tag#Entity_types) tag
