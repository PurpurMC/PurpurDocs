This page details the various configuration settings available in PurpurExtras configuration file.

## anvil-crushes-blocks

If enabled, block list will be used. Key is the block material that will be converted from and value is block material that will be converted to. In default config if anvil falls on a cobblestone block, that cobblestone will be converted to sand.

## anvil-splits-boats

If enabled, dropping an anvil from significant height onto chest boat in its item form, it will not destroy the item, but split the boat and the chest and drop them both.

## anvil-splits-minecarts

If enabled, dropping an anvil from significant height onto minecart with content (chest minecart, furnace minecart, etc.) in its item form, it will not destroy the item, but split the minecart and the content and drop them both.

## block-building-above-nether

### enabled

Enables the feature.

### height-limit

Maximum height players without `purpurextras.netherbuildheightbypass` permission can build in nether worlds.

### no-permission-message

Message to display in action bar when trying to build above set limit in nether worlds.

## blocks

### chorus-flowers-always-drop

Makes it so chorus flowers always drop, no matter if they were destroyed directly or not.

### shift-right-click-for-invisible-item-frames

Right click when sneaking on an item frame with item inside of it will make the item frame invisible. Requires `purpurextras.invisibleframes` permission.

## chat

### escape-commands

Allows players to send a message with a slash at the start by escaping it with backslash (`\/command` that will appear as `/command` in chat).

### send-sleep-percentage-message

If enabled, sends messages in chat containing amount of players required to sleep based on playersSleepingPercentage gamerule.

## create-suspicious-blocks

If enabled, players will be able to shift-right click on sand and gravel with items in their hands to create suspicious blocks and put held item inside. Held item will disappear from player's hand and will be added as loot inside the suspicious block. Only one item can be added per block.

## creeper-squid

Squids will act as Creepers - they will explode if within `agro-distance` after a fuse of `fuse-ticks` ticks, as well as moving towards you at a velocity of `velocity`. Explosion power / radius is also configurable through `explosion-radius`.

### enabled

Enables the feature.

### fuse-ticks

The amount of time it takes for the "fuse" to last.

### agro-distance

The detection range (in blocks).

### explosion-radius

The radius of the explosion.

### velocity

The speed at which it moves towards the player.

## dispenser

### break-blocks

If a tool category is enabled, that tool dispensed from dispenser will destroy the block in front of it. It will only destroy blocks that tool can destroy, and it will destroy them like that tool was used on it, so wooden pickaxe will destroy diamond ore, but will not drop any items.

### interact-with-cauldron

If enabled, will allow dispensers fill and empty cauldrons.

### puts-discs-in-jukebox

If enabled, dispensers will be able to insert into or swap music discs in jukeboxes.

### shears-shear-pumpkin

If enabled, when shears are dispensed and there's a pumpkin in front of a dispenser, shears will be used, making carved pumpkin.

## dye-boss-bars

If enabled, allows players to dye boss health bars by right-clicking the boss with a dye item.

## furnace

### burn-time

If enabled, multiplier field will be used to modify fuel burn time in furnaces.

## gameplay-settings

### cancel-damage-from-pet-owner

If enabled, pet owners will not be able to harm their own pets.

### fall-damage-when-jump-boost-applied

Toggles if entities with jump boost effect will  take fall damage

### open-iron-doors-with-hand

Allows opening iron doors with a hand, just like wooden doors. Can be controlled by `purpurextras.openirondoors` permission (defaults to true).

### open-iron-trapdoors-with-hand

Allows opening iron trapdoors with a hand, just like wooden trapdoors. Can be controlled by `purpurextras.openirontrapdoors` permission (defaults to true).

### respawn-anchor-needs-charges

If false, will make it so respawn anchors will never run out of charges.

### run-faster-on-paths

Makes running on path blocks apply movement speed modifier. The equivalent of a single level of potion of swiftness is `0.2` and `add_scalar` type.

#### enabled

Decides if feature is active or not.

#### path-blocks

List of blocks that will be considered as paths. By default, this is just `minecraft:grass_path`.

#### attribute-modifier-type

Available values here are `add_number`, `add_scalar` and `multiply_scalar_1`.

#### value

The decimal value of the attribute modifier.

### spawner-placement-requires-specific-permission

Players will need `purpurextras.spawnerplace.<mobtype>` permission to place spawners of that mob.

## grindstone

### gives-enchants-back

If enabled and player has books in their inventory while disenchanting item in a grindstone, books will be consumed to return the enchantments removed from the item to the player. No exp will drop when doing this.

## items

### beehive-lore

If true, will add lore with amount of bees and honey to the picked up hives.

## leash-snap

If enabled, a sound will play when a leash snaps due to the distance being too great.

### pitch

The pitch at which the sound is played at. This is a float number between -1 and 1

### sound

The sound that gets played when the leash snaps. A list of sounds can be found [here](https://minecraft.wiki/w/Sounds.json).

### volume

The volume at which the sound will be played at. This is an integer number above 0.

## loom

### max-layers

Maximum amount of layers that can be added to a banner. By default, this is 6. The client might not display more than 6 layers at the time.

## lightning-transforms-entities

If enabled, entities with type on the left will be transformed into entity of type on the right. This overrides vanilla transformations. Vanilla mob ids are used to identify mobs. There are also special cases:

- `killer_bunny` - a killer bunny
- `jeb_sheep` - rainbow sheep
- `johnny` - vindicator aggressive to most mobs
- `toast` - special variant of rabbit

## mobs

### sheep

#### jeb-shear-random-color

Shearing a sheep named `jeb_` will drop wool blocks with a random colour

### snow_golem

#### drop-pumpkin-when-sheared

If set to false prevents snow golems from dropping carved pumpkin when shearing them when they have it on their head.

## protect-blocks-with-loot

Makes it so blocks with loot tables are protected from being destroyed. By default, they can be destroyed while holding sneak, but it's configurable. Can be bypassed with `purpurextras.lootblockprotectionbypass` permission. Message displayed can be configured. [Message type](#message-types) can be configured.

## raid-totem-drops

### enabled

If enabled, drop rate of totems from evokers in raids can be configured.

### chance

Chance of evoker in a raid dropping a totem. This is a float number between 0 and 1.

## rideables

### mob-needs-to-be-nametagged-to-ride

If enabled, only name tagged mobs can be mounted/steered using Purpur's rideable option.

## shields

### cooldown

Amount of ticks (1/20th of a second) of cooldown for a shield after hitting it with an axe crit. By default, this is 100 ticks (5 seconds).

### damage-reduction

Value between 0 and 1. This is the percentage of damage reduction that defending with a shield will provide. By default, shield reduces 100% of the damage (1.0).

## stonecutter-damage-filter

If enabled, allows filtering which entity types don't get damaged by stonecutters if [stonecutter dealing damage](https://purpurmc.org/docs/Configuration/stonecutter_1) Purpur feature is enabled.

## totem

### work-on-void-death

If enabled, totem of undying will save players from death in the void and will teleport them to the last place their feet touched the ground. If for any reason that position is not found, they will be teleported to world spawn.

## twerk-to-reduce-burn-time

### amount

The percentage to reduce the burn time by.

### chance

The chance for a twerk to succeed to reducing the burn time. This is a float number between 0 and 1.

## unlock-all-recipes-on-join

Unlocks all available recipes on join. Players can be exempt from this by denying them `purpurextras.unlockallrecipesonjoin` permission.

## use-notarget-permissions

If enabled, players having `target.bypass.<mojang_mob_name>` permission won't be targetted by that type of mob.

## Message types

### CHAT
Regular system chat message

### ACTION_BAR
Action bar message
