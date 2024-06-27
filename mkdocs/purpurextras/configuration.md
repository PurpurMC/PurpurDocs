This page details the various configuration settings available in PurpurExtras configuration file.

## unlock-all-recipes-on-join
Unlocks all available recipes on join. Players can be exempt from this by denying them `purpurextras.unlockallrecipesonjoin` permission.

## protect-blocks-with-loot
Makes it so blocks with loot tables are protected from being destroyed. By default, they can be destroyed while holding sneak, but it's configurable. Can be bypassed with `purpurextras.lootblockprotectionbypass` permission. Message displayed can be configured. [Message type](#message-types) can be configured.

## create-suspicious-blocks
If enabled, players will be able to shift-right click on sand and gravel with items in their hands to create suspicious blocks and put held item inside. Held item will disappear from player's hand and will be added as loot inside the suspicious block. Only one item can be added per block.

## stonecutter-damage-filter
If enabled, allows filtering which entity types don't get damaged by stonecutters if [stonecutter dealing damage](https://purpurmc.org/docs/Configuration/stonecutter_1) Purpur feature is enabled.

## use-notarget-permissions
If enabled, players having `target.bypass.<mojang_mob_name>` permission won't be targetted by that type of mob.

## anvil-splits-minecarts
If enabled, dropping an anvil from significant height onto minecart with content (chest minecart, furnace minecart, etc.) in its item form, it will not destroy the item, but split the minecart and the content and drop them both.

## anvil-splits-boats
If enabled, dropping an anvil from significant height onto chest boat in its item form, it will not destroy the item, but split the boat and the chest and drop them both.

## dye-boss-bars
If enabled, allows players to dye boss health bars by right-clicking the boss with a dye item.

## loom

### max-layers
Maximum amount of layers that can be added to a banner. By default, this is 6. The client might not display more than 6 layers at the time.

## raid-totem-drops

### enabled
If enabled, drop rate of totems from evokers in raids can be configured.

### chance
Chance of evoker in a raid dropping a totem. This is a float number between 0 and 1.

## shields

### damage-reduction
Value between 0 and 1. This is the percentage of damage reduction that defending with a shield will provide. By default, shield reduces 100% of the damage (1.0).

### cooldown
Amount of ticks (1/20th of a second) of cooldown for a shield after hitting it with an axe crit. By default, this is 100 ticks (5 seconds).

## items

### beehive-lore

If true, will add lore with amount of bees and honey to the picked up hives.

## lightning-transforms-entities

If enabled, entities with type on the left will be transformed into entity of type on the right. This overrides vanilla transformations. Vanilla mob ids are used to identify mobs. There are also special cases:

- `killer_bunny` - a killer bunny
- `jeb_sheep` - rainbow sheep
- `johhny` - vindicator aggressive to most mobs
- `toast` - special variant of rabbit

## blocks

### shift-right-click-for-invisible-item-frames
Right click when sneaking on an item frame with item inside of it will make the item frame invisible. Requires `purpurextras.invisibleframes` permission.

### chorus-flowers-always-drop
Makes it so chorus flowers always drop, no matter if they were destroyed directly or not.

## block-building-above-nether

### enabled
Enables the feature.

### height-limit
Maximum height players without `purpurextras.netherbuildheightbypass` permission can build in nether worlds.

### no-permission-message
Message to display in action bar when trying to build above set limit in nether worlds.

## gameplay-settings

### respawn-anchor-needs-charges
If false, will make it so respawn anchors will never run out of charges.

### open-iron-doors-with-hand
Allows opening iron doors with a hand, just like wooden doors. Can be controlled by `purpurextras.openirondoors` permission (defaults to true).

### open-iron-trapdoors-with-hand
Allows opening iron trapdoors with a hand, just like wooden trapdoors. Can be controlled by `purpurextras.openirontrapdoors` permission (defaults to true).

### spawner-placement-requires-specific-permission
Players will need `purpurextras.spawnerplace.<mobtype>` permission to place spawners of that mob.

### cancel-damage-from-pet-owner
If enabled, pet owners will not be able to harm their own pets.

### fall-damage-when-jump-boost-applied
Toggles if entities with jump boost effect will  take fall damage

### run-faster-on-paths
If `speed-multiplier` value is higher than 0, player will gain speed potion effect of the level of that value. This only accepts integer values. Which blocks count as paths can be configured by listing them in `path-blocks` list.

## chat

### escape-commands
Allows players to send a message with a slash at the start by escaping it with backslash (`\/command` that will appear as `/command` in chat).

### send-sleep-percentage-message
If enabled, sends messages in chat containing amount of players required to sleep based on playersSleepingPercentage gamerule.

## anvil-crushes-blocks

If enabled, block list will be used. Key is the block material that will be converted from and value is block material that will be converted to. In default config if anvil falls on a cobblestone block, that cobblestone will be converted to sand.

## dispenser

### break-blocks

If a tool category is enabled, that tool dispensed from dispenser will destroy the block in front of it. It will only destroy blocks that tool can destroy, and it will destroy them like that tool was used on it, so wooden pickaxe will destroy diamond ore, but will not drop any items.

### shears-shear-pumpkin

If enabled, when shears are dispensed and there's a pumpkin in front of a dispenser, shears will be used, making carved pumpkin.

### interact-with-cauldron

If enabled, will allow dispensers fill and empty cauldrons.

### puts-discs-in-jukebox

If enabled, dispensers will be able to insert into or swap music discs in jukeboxes.

## grindstone

### gives-enchants-back

If enabled and player has books in their inventory while disenchanting item in a grindstone, books will be consumed to return the enchantments removed from the item to the player. No exp will drop when doing this.

## rideables

### mob-needs-to-be-nametagged-to-ride

If enabled, only name tagged mobs can be mounted/steered using Purpur's rideable option.

## furnace

### burn-time

If enabled, multiplier field will be used to modify fuel burn time in furnaces.

## mobs

### snow_golem

#### drop-pumpkin-when-sheared

If set to false prevents snow golems from dropping carved pumpkin when shearing them when they have it on their head.

### sheep

#### jeb-shear-random-color

Shearing a sheep named jeb_ will drop wool blocks with a random colour

## totem

### work-on-void-death

If enabled, totem of undying will save players from death in the void and will teleport them to the last place their feet touched the ground. If for any reason that position is not found, they will be teleported to world spawn.

## twerk-to-reduce-burn-time

### chance

The chance for a twerk to succeed to reducing the burn time. This is a float number between 0 and 1.

### amount

The percentage to reduce the burn time by.

## leash-snap

If enabled, a sound will play when a leash snaps due to the distance being too great.

### sound

The sound that gets played when the leash snaps. A list of sounds can be found [here](https://minecraft.wiki/w/Sounds.json).

### Volume

The volume at which the sound will be played at. This is an integer number above 0.

### Pitch

The pitch at which the sound is played at. This is a float number between -1 and 1

## Message types

### CHAT
Regular system chat message

### ACTION_BAR
Action bar message
