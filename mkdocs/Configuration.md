This page details the various configuration settings exposed by Purpur in the purpur.yml file.

If you want information on settings in tuinity.yml, paper.yml, spigot.yml, bukkit.yml and server.properties you should see their respective documentation pages.

* [Server Configuration (server.properties)](https://minecraft.gamepedia.com/Server.properties)

* [Bukkit Configuration (bukkit.yml)](https://bukkit.gamepedia.com/Bukkit.yml)

* [Spigot Configuration (spigot.yml)](https://www.spigotmc.org/wiki/)

* [Paper Configuration (paper.yml)](https://paper.readthedocs.io/en/latest/server/configuration.html)

* [Tuinity Configuration (tuinity.yml)](https://github.com/Spottedleaf/Tuinity/wiki/Config)

???+ warning "Warning"
    Configuration values change frequently at times. It is possible for the information here to be incomplete. If you cannot find what you’re looking for or think something may be wrong, Contact us through our [Discord](http://purpur.pl3x.net/discord/) server.

## Global Settings

Global settings affect all worlds on the server as well as the core server functionality itself.

### verbose

- **default**: false
- **description**: Sets whether the server should dump all configuration values to the server log on startup
	
### config-version

* **Do not change this for any reason!** This is used internally to help automatically update your config
	
### command

* #### gamemode
    * ##### requires-specific-permission
        - Requires [`minecraft.command.gamemode.<gamemode>`](../Permissions#minecraftcommandgamemodegamemode) permission
        - **default**: false
        - **description**: Set to true for each gamemode to require it's own permission
* #### hide-hidden-players-from-entity-selector
    - **default**: false
    - **description**: Set to true to hide players from the entity selector if they're hidden

### allow-water-placement-in-the-end

- **default**: true
- **description**: Allows the placement of water in the end.
	
### dont-send-useless-entity-packets

- **default**: false
- **description**: Skips sending relative move packets for entities that didn't really move

???+ warning "Warning"
    The `dont-send-useless-entity-packets` option is known to cause issues with certain plugins installed, notably `Tab` and `Companions`.
	
### use-alternate-keepalive

- **default**: false
- **description**: Uses a different approach to keepalive ping timeouts. Enabling this sends a keepalive packet once per second to a player, and only kicks for timeout if none of them were responded to in 30 seconds. Responding to any of them in any order will keep the player connected. AKA, it won't kick your players because 1 packet gets dropped somewhere along the lines
	
### tps-catchup

- **default**: true
- **description**: Control tps catch-up

???+ note "Note"
    TPS catchup makes your server tick faster than 20 TPS after any period of time that below 20. This is an attempt at keeping the average TPS as close to 20 as possible, but does come with its own set of side effects
	
### server-mod-name
- **default**: Purpur
- **description**: This modified the server name that shows up when a client is outdated or when someone opens the debug screen [F3]
	
### lagging-threshold
- **default**: 19.0
- **description**: Purpur keeps track of when it is lagging in order to have the ability to change behaviors accordingly. This value is that threshold when you want to consider the server to be lagging. Right now this is only used for mob.villager.brain-ticks setting
	
### disable-give-dropping
- **default**: false
- **description**: Set to true to disable the /give command from dropping items on the floor when a player's inventory is full
	
### messages

#### afk-broadcast-away
Requires the [`kick-if-idle`](#kick-if-idle) setting to be `false`

- **default**: §e§o%s is now AFK
- **description**: This is the message that gets broadcasted when a user goes AFK (must have `player-idle-timeout` set greater than 0 & [kick-if-idle](#kick-if-idle) set as false)

#### afk-broadcast-back
Requires the [`kick-if-idle`](#kick-if-idle) setting to be `false`

- **default**: §e§o%s is no longer AFK
- **description**: This is the message that gets broadcasted when a user is no longer AFK (must have `player-idle-timeout` set greater than 0 & [kick-if-idle](#kick-if-idle) set as false)

#### afk-tab-list-prefix
Requires the [`kick-if-idle`](#kick-if-idle) setting to be `false`

- **default**: "[AFK] "
- **description**: The prefix that shows up on the playerlist before someone's name when they're AFK

#### afk-tab-list-suffix
Requires the [`kick-if-idle`](#kick-if-idle) setting to be `false`

- **default**: ""
- **description**: The suffix that shows up on the playerlist after someone's name when they're AFK

#### ping-command-output
Requires the [`bukkit.command.ping`](../Permissions#bukkitcommandping) permission

- **default**: §a%s's ping is %sms
- **description**: Output when `/ping <user>` is run.

#### cannot-ride-mob
Requires the [`allow.ride.<mob_id>`](../Permissions#allowridemob_id) permission

- **default**: §cYou cannot mount that mob
- **description**: Message that shows when someone tries to mount a mob they're not allowed to.

#### demo-command-output
Requires the [`bukkit.command.demo`](../Permissions#bukkitcommanddemo) permission

- **default**: §a%s has been shown the demo screen
- **description**: Message that shows when the demo screen is enabled for a user using the `/demo` command.

#### credits-command-output
Requires the [`bukkit.command.credits`](../Permissions#bukkitcommandcredits) permission

- **default**: §a%s has been shown the end credits
- **description**: Message that shows when the credits screen is enabled for a user using the `/credits` command.

#### unverified-username
- **default**: default
- **description**: Message that shows when a player is kicked for having an unverified username (user is in offline-mode). Setting as "default" displays the default message "Failed to verify username!"
	
### blocks

####  barrel
* ##### six-rows
    - **default**: false
    - **description**: Barrels should have 6 rows of inventory space
####  beehive
* ##### max-bees-inside
    - **default**: 3
    - **description**: The maximum amount of bees allowed inside of a beehive/bee_nest
####  ender_chest
* ##### six-rows
    - **default**: false
    - **description**: Ender chests should have six rows of inventory space
* ##### use-permissions-for-rows
    - Requires [`ender_chest.six-rows`](#six-rows) to be true
    - Requires [`purpur.enderchest.rows.<number>`](../Permissions#purpurenderchestrowsnumber) permission
    - **default**: false
    - **description**: Use permission nodes to determine the number of rows. By default, with this setting enabled, all players have `six` rows unless otherwise specified using permissions.

#### disable-mushroom-updates  
- **default**: false
- **description**: Stops the mushroom block from updating it's block state server side
#### disable-chorus-plant-updates  
- **default**: false
- **description**: Stops the chorus plant from updating it's block state server side
#### disable-note-block-updates  
- **default**: false
- **description**: Stops the note block from updating it's block state server side
####  crying_obsidian
* ##### valid-for-portal-frame
    - **default**: false
    - **description**: Set to true to make it so you can create portals out of crying obsidian
	
### timings

#### url
- **default**: "https://timings.pl3x.net"
- **description**: The server where timing reports are posted to. To use Aikar's timings server use "http://timings.aikar.co"

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
	
### seed
Check out https://minecraft.fandom.com/wiki/Configured_feature for more information on the options below

#### bamboo
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### basalt_columns
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### basalt_pillar
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### block_pile
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### blue_ice
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### bonus_chest
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### chorus_plant
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### coral_claw
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### coral_mushroom
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### coral_tree
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### decorated
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### delta_feature
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### disk
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### dripstone_cluster
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### end_island
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### end_spike
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### flower
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### forest_rock
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### fossil
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### geode
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### glow_lichen
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### glowstone_blob
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### growing_plant
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### huge_brown_mushroom
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### huge_fungus
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### huge_red_mushroom
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### ice_patch
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### ice_spike
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### iceberg
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### kelp
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### lake
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### large_dripstone
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### monster_room
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### nether_forest_vegetation
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### netherrack_replace_blobs
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### ore
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### random_boolean_selector
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### random_patch
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### random_selector
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### replace_single_block
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### root_system
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### scattered_ore
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### sea_pickle
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### seagrass
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### simple_block
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### simple_random_selector
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### small_dripstone
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### tree
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### twisting_vines
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### underwater_magma
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### vegetation_patch
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### waterlogged_vegetation_patch
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
#### weeping_vines
- **default**: -1
- **description**: The default value is `-1` for "use the world seed". anything not -1 will be a custom seed. it can accept any Integer value (-2147483648 to 2147483647)
	
### entity

#### enderman
* ##### short-height
    - **default**: false
    - **description**: allows endermen to fit into 2 block tall spaces if enabled. Since client hitbox remains the same, you can still hit them in the head
	
#### enchantment

* #### allow-infinity-and-mending-together
    - **default**: false
    - **description**: allows the mending and infinity enchantment to be on the same weapon/tool
* #### allow-infinity-on-crossbow
    - **default**: false
    - **description**: allows the infinity enchantment on a crossbow
* #### allow-unsafe-enchants
    - **default**: false
    - **description**: allows the ability to increase enchantments passed their max level
	

## World Settings

World settings are on a per-world basis. The child-node `default` is used for all worlds that do not have their own specific settings

### blocks


#### dragon_egg
* ##### teleport
    - **default**: true
    - **description**: Control whether the dragon egg will teleport when hit
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
#### powered-rail
* ##### activation-range
    - **default**: 8
    - **description**: The amount of powered rails that get activated by a single redstone source
#### beacon
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
#### sand
* ##### fix-duping
    - **default**: true
    - **description**: Set to false to re-enable the ability to sand dupe
#### dispenser
* ##### apply-cursed-to-armor-slots
    - **default**: true
    - **description**: Should dispensers apply armor to armor slots if enchanted with curse of binding
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
    - **default**: DESTROY
    - **description**: What to do with the blocks that are effected by the explosion. `DESTROY` will destroy the blocks (no item drops). `BREAK` will naturally break the blocks (items will drop). `NONE` will not break any blocks
#### sign
* ##### allow-colors
    - Requires [`purpur.sign.color`](../Permissions#purpursigncolor), [`purpur.sign.style`](../Permissions#purpursignstyle), and/or [`purpur.sign.magic`](../Permissions#purpursignmagic) permission
    - **default**: false
    - **description**: Allow players to use color codes on signs
* ##### right-click-edit
    - Requires [`purpur.sign.edit`](../Permissions#purpursignedit) permission
    - **default**: false
    - **description**: Ability to edit signs by right clicking them with another sign in hand
#### magma-block
* ##### damage-when-sneaking
    - **default**: false
    - **description**: Set to true to enable damage when sneaking
* ##### damage-with-frost-walker
    - **default**: false
    - **description**: Set to true to enable damage when walking with boots enchanted with frost-walker
#### lava
* ##### infinite-source
    - **default**: false
    - **description**: Allow lava to take on infinite supply properties similar to water (&lt;infinite-required-sources&gt; source blocks flowing together creates a new source block)
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
#### piston
* ##### block-push-limit
    - **default**: 12
    - **description**: The amount of blocks a piston can push
#### bed
* ##### explode
    - **default**: true
    - **description**: Whether beds explode. Setting this to false just makes the bed blip out of existence
* ##### explosion-power
    - **default**: 5.0
    - **description**: The blast radius of the explosion. (For comparison, TNT is 4.0 and charged creepers are 6.0)
* ##### explosion-fire
    - **default**: true
    - **description**: Whether the explosion can cause fire or not
* ##### explosion-effect
    - **default**: DESTROY
    - **description**: What to do with the blocks that are effected by the explosion. `DESTROY` will destroy the blocks (no item drops). `BREAK` will naturally break the blocks (items will drop). `NONE` will not break any blocks
#### farmland
* ##### get-moist-from-below
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
* ##### feather-fall-distance-affects-trampling
    - **default**: false
    - **description**: Set to true if entities can stop trampling if they fall a distance equal to their feather falling level, plus the extra block necessary to trample in the first place. Feather Falling 1 requires you to fall over 3+ blocks to trample. FF 2 requires 4+, etc.
#### spawner
* ##### deactivate-by-redstone
    - **default**: false
    - **description**: Allow spawners to be deactivated by redstone
#### dispenser
* ##### place-anvils
    - **default**: false
    - **description**: Allows anvils to be placed by dispensers
#### anvil
* ##### allow-colors
    - Requires [`purpur.anvil.color`](../Permissions#purpuranvilcolor) permission
    - **default**: false
    - **description**: Allows players to use color codes in anvils
* ##### cumulative-cost
    - **default**: true
    - **description**: If the cumulative cost should apply when an item is used in an anvil
#### stonecutter
* ##### damage
    - **default**: 0.0
    - **description**: If a value is set, Mobs will also avoid walking over the stonecutter. 
#### no-random-tick
- **default**: []
- **description**: List of blocks that will not randomly tick (Only applies to the [blocks affected by random tick](https://minecraft.fandom.com/wiki/Tick#Random_tick))
#### furnace
* ##### infinite-fuel
    - **default**: false
    - **description**: Allows the furnace to be infinitely powered by lava placed underneath it
#### blue_ice
* ##### allow-snow-formation
    - **default**: true
    - **description**: Set to false to disallow snow formation on blue ice
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
    - **description**: Allows you to set the doors that require redstone to be operated
#### twisting_vines
* ##### growth-modifier
    - **default**: 0.10
    - **description**: Changes the rate of growth of the vine
* ##### max-growth-age
    - **default**: 25
    - **description**: The max growth age that the plant can grow
#### weeping_vines
* ##### growth-modifier
    - **default**: 0.10
    - **description**: Changes the rate of growth of the vine
* ##### max-growth-age
    - **default**: 25
    - **description**: The max growth age that the plant can grow
#### kelp
* ##### max-growth-age
    - **default**: 25
    - **description**: The max growth age that the plant can grow
#### end-crystal
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
        - **default**: DESTROY
        - **description**: The type of explosion effect. Available values are `NONE`, `BREAK`, and `DESTROY`.
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
        - **default**: DESTROY
        - **description**: The type of explosion effect. Available values are `NONE`, `BREAK`, and `DESTROY`.

	
### mobs

#### ender_dragon
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
* ##### ridable-max-y
    - **default**: 256
    - **description**: Maximum height this mob can fly to while being ridden
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
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
* ##### attributes
    * ###### max_health
        - **default**: 12.0
        - **description**: Max health attribute
#### endermite
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
* ##### attributes
    * ###### max_health
        - **default**: 8.0
        - **description**: Max health attribute
#### mooshroom
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
* ##### breeding-delay-ticks
    - **default**: 6000
    - **description**: The amount of ticks to wait before being able to breed again
* ##### attributes
    * ###### max_health
        - **default**: 10.0
        - **description**: Max health attribute
#### polar_bear
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
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
#### vindicator
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
* ##### johnny
    * ###### spawn-chance
        - **default**: 0.0
        - **description**: Percent chance (0.0 - 1.0) a vindicator named "Johnny" will spawn instead of a vindicator
* ##### attributes
    * ###### max_health
        - **default**: 24.0
        - **description**: Max health attribute
#### zombie_horse
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
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
#### wither
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
* ##### ridable-max-y
    - **default**: 256
    - **description**: Maximum height this mob can fly to while being ridden
* ##### can-ride-vehicles
    - **default**: false
    - **description**: Set to true for the wither to gain the ability to ride vehicles
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
#### wither_skeleton
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
* ##### takes-wither-damage
    - **default**: false
    - **description**: Allows wither skeletons to receive the wither effect (from wither roses, etc)
* ##### attributes
    * ###### max_health
        - **default**: 20.0
        - **description**: Max health attribute
#### zombie_villager
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
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
#### wandering_trader
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
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
#### silverfish
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
* ##### bypass-mob-griefing
    - **default**: false
    - **description**: Set to true for silverfish to bypass the mob griefing gamerule
* ##### attributes
    * ###### max_health
        - **default**: 8.0
        - **description**: Max health attribute
#### zombified_piglin
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
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
#### snow_golem
???+ info "The formula used to determine the amount of ticks between shots"
    ``` sh
    ((sqrt(distanceToTarget) / attack-distance) / snow-ball-modifier) * (max-shoot-interval-ticks - min-shoot-interval-ticks) + min-shoot-interval-ticks
    ```
    If `min-shoot-interval-ticks` and `max-shoot-interval-ticks` are both set to 0, snow golems won't shoot any snowballs.

* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
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
#### skeleton_horse
* ##### can-swim
    - **default**: false
    - **description**: Can skeleton horses swim in water. False makes them sink to the bottom (vanilla default)
* ##### ridable-in-water
    - **default**: true
    - **description**: Makes this mob ridable in water (it wont eject you)
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
#### phantom
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
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
    * ###### min-time-since-slept
        - **default**: 72000
        - **description**: Minimum number of ticks since the player has last slept before spawning
    * ###### delay
        * min
            - **default**: 1200
            - **description**: Minimum time (in ticks) between spawn attempts (globally)
        * max
            - **default**: 2400
            - **description**: Maximum time (in ticks) between spawn attempts (globally)
    * ###### overhead
        * min
            - **default**: 20
            - **description**: Minimum number of blocks to spawn at above players head
        * max
            - **default**: 35
            - **description**: Maximum number of blocks to spawn at above players head
        * radius
            - **default**: 10
            - **description**: Radius of blocks to spawn at above players head
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
#### chicken
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
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
#### creeper
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
* ##### allow-griefing
    - **default**: true
    - **description**: Set to false to stop the creeper from griefing.
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
#### donkey
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
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
#### cow
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
* ##### feed-mushrooms-for-mooshroom
    - **default**: 0
    - **description**: Number of mushrooms to feed a cow to make it transform into a mooshroom. Value of 0 disables feature
* ##### breeding-delay-ticks
    - **default**: 6000
    - **description**: The amount of ticks to wait before being able to breed again
* ##### attributes
    * ###### max_health
        - **default**: 10.0
        - **description**: Max health attribute
#### enderman
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
* ##### allow-griefing
    - **default**: true
    - **description**: Set to false to stop the enderman from griefing
* ##### can-despawn-with-held-block
    - **default**: false
    - **description**: Makes the enderman despawn even if it's holding a block
* ##### bypass-mob-griefing
    - **default**: false
    - **description**: Set to true for enderman to bypass the mob griefing gamerule
* ##### takes-damage-from-water
    - **default**: true
    - **description**: Set to false for this mob to stop taking damage from water
* ##### aggressive-towards-spawned-endermites
    - **default**: false
    - **description**: Set to true to make enderman aggro towards spawned endermites
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
#### evoker
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
* ##### bypass-mob-griefing
    - **default**: false
    - **description**: Set to true for evokers to bypass the mob griefing gamerule
* ##### attributes
    * ###### max_health
        - **default**: 24.0
        - **description**: Max health attribute
#### drowned
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
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
#### pillager
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
* ##### bypass-mob-griefing
    - **default**: false
    - **description**: Set to true for pillagers to bypass the mob griefing gamerule
* ##### attributes
    * ###### max_health
        - **default**: 24.0
        - **description**: Max health attribute
#### fox
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
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
#### giant
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
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
#### hoglin
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
* ##### breeding-delay-ticks
    - **default**: 6000
    - **description**: The amount of ticks to wait before being able to breed again
* ##### attributes
    * ###### max_health
        - **default**: 40.0
        - **description**: Max health attribute
#### squid
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### immune-to-EAR
    - **default**: true
    - **description**: Makes this mob immune to EAR (Entity Activation Range)
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
#### villager
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
* ##### brain-ticks
    - **default**: 1
    - **description**: How often (in ticks) should villager's tick their brain logic. Vanilla value is to tick every tick (1). Higher amounts makes them tick less often to reduce lag, but setting it too high could result is unresponsive villagers
* ##### use-brain-ticks-only-when-lagging
    - **default**: true
    - **description**: Only use the brain ticks setting when the server is lagging (see lagging-threshold above). If set to false, the brain ticks setting is always used
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
* ##### lobotomize
    * ###### enabled
        - **default**: false
        - **description**: Lobotomizes the villager if it cannot move (Does not disable trading)
    * ###### check-interval
        - **default**: 60
        - **description**: The interval in ticks to check if a villager is lobotomized 
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
#### mule
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
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
#### wolf
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
* ##### milk-cures-rabid-wolves
    - **default**: true
    - **description**: Set to false for rabid wolves to not be cured by milk
* ##### spawn-rabid-chance
    - **default**: 0.0
    - **description**: Percent chance (0.0 - 1.0) that a wolf will spawn as rabid
* ##### default-collar-color
    - **default**: RED
    - **description**: Set the default collar color when a wolf is tamed. [Available Colors](https://purpur.pl3x.net/javadoc/org/bukkit/Color.html)
* ##### breeding-delay-ticks
    - **default**: 6000
    - **description**: The amount of ticks to wait before being able to breed again
* ##### attributes
    * ###### max_health
        - **default**: 8.0
        - **description**: Max health attribute
#### zoglin
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
* ##### attributes
    * ###### max_health
        - **default**: 40.0
        - **description**: Max health attribute
#### ocelot
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
* ##### breeding-delay-ticks
    - **default**: 6000
    - **description**: The amount of ticks to wait before being able to breed again
* ##### attributes
    * ###### max_health
        - **default**: 10.0
        - **description**: Max health attribute
#### shulker
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
* ##### attributes
    * ###### max_health
        - **default**: 30.0
        - **description**: Max health attribute
#### horse
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
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
#### piglin
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
* ##### portal-spawn-modifier
    - **default**: 2000
    - **description**: Allows changing the modifier for the piglin spawn chance from a portal block
based on the world difficulty. [Read more here](https://github.com/pl3xgaming/Purpur/blob/ver/1.16.5/patches/server/0198-Piglin-portal-spawn-modifier.patch)
* ##### attributes
    * ###### max_health
        - **default**: 16.0
        - **description**: Max health attribute
#### piglin_brute
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
* ##### attributes
    * ###### max_health
        - **default**: 50.0
        - **description**: Max health attribute
#### skeleton
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
* ##### attributes
    * ###### max_health
        - **default**: 8.0
        - **description**: Max health attribute
#### stray
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
* ##### attributes
    * ###### max_health
        - **default**: 20.0
        - **description**: Max health attribute
#### panda
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
* ##### breeding-delay-ticks
    - **default**: 6000
    - **description**: The amount of ticks to wait before being able to breed again
* ##### attributes
    * ###### max_health
        - **default**: 20.0
        - **description**: Max health attribute
#### strider
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
* ##### give-saddle-back
    - **default**: false
    - **description**: Sneak and right-click a pig with a saddle on it's back to remove it with this option enabled
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
#### rabbit
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
#### husk
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
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
#### spider
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
* ##### attributes
    * ###### max_health
        - **default**: 16.0
        - **description**: Max health attribute
#### sheep
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
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
#### ravager
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
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
#### pig
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
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
#### witch
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
* ##### attributes
    * ###### max_health
        - **default**: 26.0
        - **description**: Max health attribute
#### zombie
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
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
    - **description**: disable to stop zombie aggressiveness towards villagers when lagging
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
#### dolphin
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
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
#### bat
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
* ##### ridable-max-y
    - **default**: 256
    - **description**: Maximum height this mob can fly to while being ridden
* ##### attributes
    * ###### max_health
        - **default**: 6.0
        - **description**: Max health attribute
#### bee
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
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
* ##### attributes
    * ###### max_health
        - **default**: 10.0
        - **description**: Max health attribute
#### blaze
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
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
#### cat
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
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
#### cod
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### attributes
    * ###### max_health
        - **default**: 3.0
        - **description**: Max health attribute
#### elder_guardian
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### attributes
    * ###### max_health
        - **default**: 80.0
        - **description**: Max health attribute
#### ghast
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
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
#### guardian
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### attributes
    * ###### max_health
        - **default**: 30.0
        - **description**: Max health attribute
#### illusioner
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
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
#### iron_golem
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
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
#### llama
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable. Llama's must be tamed and saddled (with carpet) to be WASD controllable.
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
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
#### trader_llama
* ##### ridable
    - **default**: false
    - **description**: Makes this mob mountable and WASD controllable. Trader llama's must be tamed to be WASD controllable. Being saddled (carpet) is not a requirement since it technically always has a carpet.
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
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
#### magma_cube
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
* ##### attributes
    * ###### max_health
        - **default**: "size * size"
        - **description**: The Max health equation used to calculate the max health
#### parrot
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
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
#### pufferfish
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### attributes
    * ###### max_health
        - **default**: 3.0
        - **description**: Max health attribute
#### salmon
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### attributes
    * ###### max_health
        - **default**: 3.0
        - **description**: Max health attribute
#### slime
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
* ##### attributes
    * ###### max_health
        - **default**: "size * size"
        - **description**: The Max health equation used to calculate the max health
#### tropical_fish
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### attributes
    * ###### max_health
        - **default**: 3.0
        - **description**: Max health attribute
#### turtle
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
* ##### breeding-delay-ticks
    - **default**: 6000
    - **description**: The amount of ticks to wait before being able to breed again
* ##### attributes
    * ###### max_health
        - **default**: 30.0
        - **description**: Max health attribute
#### vex
* ##### ridable
    - **default**: false
    - **description**: Makes this mob WASD controllable
* ##### ridable-in-water
    - **default**: false
    - **description**: Makes this mob ridable in water (it wont eject you)
* ##### ridable-max-y
    - **default**: 256
    - **description**: Maximum height this mob can fly to while being ridden
* ##### attributes
    * ###### max_health
        - **default**: 14.0
        - **description**: Max health attribute
	
### gameplay-mechanics

#### use-better-mending
- **default**: false
- **description**: Set to true for mending enchantment to always repair the most damaged equipment first
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
#### projectile-offset
* ##### bow
    - **default**: 1.0
    - **description**: The projectile offset of a bow
* ##### crossbow
    - **default**: 1.0
    - **description**: The projectile offset of a crossbow
* ##### egg
    - **default**: 1.0
    - **description**: The projectile offset of a egg
* ##### ender-pearl
    - **default**: 1.0
    - **description**: The projectile offset of a ender-pearl
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
#### totem-of-undying-works-in-inventory
- **default**: false
- **description**: Allows the totem of undying to work in your inventory, not just your offhand
#### entity-blindness-multiplier
- **default**: 1
- **description**: How blind a mob is when affected with the blindness potion effect
#### entities-pick-up-loot-bypass-mob-griefing
- **default**: false
- **description**: Mobs that can pick up loot will continue to pick up loot even if the `mobGriefing` gamerule is disabled
#### fix-climbing-bypassing-cramming-rule
- **default**: false
- **description**: Stops entities from bypassing the cramming gamerule by climbing
#### milk-cures-bad-omen
- **default**: true
- **description**: Allow players to drink milk to cure bad omen status effect
#### trident-loyalty-void-return-height
- **default**: 0.0
- **description**: The void height at which a trident with loyalty will return to it's thrower. A value of 0.0 or higher disables this feature.
#### void-damage-dealt
- **default**: 4.0
- **description**: The amount of void damage dealt
#### void-damage-height
- **default**: -64.0
- **description**: The height at which void damage begins
#### entity-lifespan
- **default**: 0
- **description**: Disabled by default (0), Amount of ticks an entity will live before disappearing. Interacting with a player resets the timer
#### silk-touch
Requires the [`purpur.drop.spawners`](../Permissions#purpurdropspawners) and [`purpur.place.spawners`](../Permissions#purpurplacespawners) permissions

* ##### enabled
    - **default**: false
    - **description**: Makes it so you can mine spawners using a tool with silk touch 
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
    - **default**: Spawner
    - **description**: The name of the spawner
* ##### spawner-lore
    - **default**:
        ``` yaml
        - Spawns a {mob}
        ```
    - **description**: The lore of the spawner
#### boat
* ##### eject-players-on-land
    - **default**: false
    - **description**: Boats should eject players when on land
* ##### do-fall-damage
    - **default**: true
    - **description**: Set to false for boats to not do fall damage to players
#### armorstand
* ##### step-height
    - **default**: 0.0
    - **description**: Set the default step height of armorstands. Useful for plugins that utilize armorstands as vehicles to be able to drive over blocks without jumping, etc
* ##### set-name-visible-when-placing-with-custom-name
    - **default**: false
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
* ##### can-skip-night
    - **default**: true
    - **description**: Set to false to disable the players' ability to skip the night by sleeping
* ##### critical-damage-multiplier
    - **default**: 1.5
    - **description**: The percentage of damage a critical attack adds to the base damage
* ##### spawn-invulnerable-ticks
    - **default**: 60
    - **description**: Gives you the ability to control how long a player is invulnerable when they first spawn in.
* ##### invulnerable-while-accepting-resource-pack
    - **default**: false
    - **description**: Sets the player as invulnerable while they download the resource pack.
* ##### fix-stuck-in-portal
    - **default**: false
    - **description**: If the player is stuck inside a portal with no way of getting out, walking to another block will reset the portal cooldown, allowing them to teleport back through the portal
* ##### one-punch-in-creative
    - **default**: false
    - **description**: If the player is in creative and hits an entity with an empty hand, the entity instantly dies
* ##### sleep-ignore-nearby-mobs
    - **default**: false
    - **description**: Set to true to allow sleep even if there are mobs nearby
* ##### idle-timeout
    * ###### kick-if-idle
        - **default**: true
        - **description**: Kick players if they become idle (see server.properties for player-idle-timeout time)
    * ###### tick-nearby-entities
        - **default**: true
        - **description**: Should entities tick normally when nearby players are afk. False will require at least 1 non-afk player in order to tick
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
* ##### teleport-if-outside-border
    - **default**: false
    - **description**: Teleports you to spawn if you somehow get outside the world border
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
* ##### shears
    * ###### damage-if-sprinting
        - **default**: false
        - **description**: Holding shears while sprinting will randomly damage the player (Don't run with scissors!)
    * ###### sprinting-damage
        - **default**: 1
        - **description**: The amount of damage to give if `damage-if-sprinting` is enabled
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
    - **description**: How much damage an elytra takes during flight each second
* ##### damage-multiplied-by-speed
    - **default**: 0.0
    - **description**: Damage is multiplied by speed if flight is faster than set speed. Value of 0 disables this multiplier
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
#### raid-cooldown-seconds
- **default**: 0
- **description**: How long you should wait before another raid can be initiated
#### projectile-despawn-rates
* ##### dragon_fireball
    - **default**: -1
    - **description**: The rate at which the projectile despawns. -1 means disabled
* ##### egg
    - **default**: -1
    - **description**: The rate at which the projectile despawns. -1 means disabled
* ##### ender_pearl
    - **default**: -1
    - **description**: The rate at which the projectile despawns. -1 means disabled
* ##### experience_bottle
    - **default**: -1
    - **description**: The rate at which the projectile despawns. -1 means disabled
* ##### firework_rocket
    - **default**: -1
    - **description**: The rate at which the projectile despawns. -1 means disabled
* ##### fishing_bobber
    - **default**: -1
    - **description**: The rate at which the projectile despawns. -1 means disabled
* ##### fireball
    - **default**: -1
    - **description**: The rate at which the projectile despawns. -1 means disabled
* ##### llama_spit
    - **default**: -1
    - **description**: The rate at which the projectile despawns. -1 means disabled
* ##### potion
    - **default**: -1
    - **description**: The rate at which the projectile despawns. -1 means disabled
* ##### shulker_bullet
    - **default**: -1
    - **description**: The rate at which the projectile despawns. -1 means disabled
* ##### small_fireball
    - **default**: -1
    - **description**: The rate at which the projectile despawns. -1 means disabled
* ##### snowball
    - **default**: -1
    - **description**: The rate at which the projectile despawns. -1 means disabled
* ##### wither_skull
    - **default**: -1
    - **description**: The rate at which the projectile despawns. -1 means disabled
#### entities-can-use-portals
- **default**: true
- **description**: Set to false to stop entities from being able to use portals
#### persistent-tileentity-display-names-and-lore
- **default**: false
- **description**: Set to true to make TE's display names and lores persist after breaking (ex. named custom player heads retain their name)
#### persistent-droppable-entity-display-names
- **default**: false
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
    - minecraft:grass_block
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
	
