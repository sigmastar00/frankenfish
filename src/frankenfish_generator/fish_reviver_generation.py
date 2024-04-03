from collections.abc import Iterable
from .minecraft_version import MinecraftVersion
from .resource_location import ResourceLocation
from .datapack_file import DatapackFile
from .mcfunction import fix_whitespace
from itertools import starmap


def generate_fish_revivers(
    fishes: Iterable[tuple[ResourceLocation, ResourceLocation]],
    minecraft_version: MinecraftVersion,
) -> Iterable[DatapackFile]:
    return starmap(
        lambda item, entity: generate_fish_reviver(item, entity, minecraft_version),
        fishes,
    )


def fish_reviver_path(fish_item: ResourceLocation) -> str:
    if fish_item.namespace == "minecraft":
        return f"data/frankenfish/functions/revive_{fish_item.path}.mcfunction"
    else:
        return f"data/frankenfish/functions/{fish_item.namespace}/revive_{fish_item.path}.mcfunction"


def generate_fish_reviver(
    fish_item: ResourceLocation,
    fish_entity: ResourceLocation,
    minecraft_version: MinecraftVersion,
) -> DatapackFile:
    match minecraft_version:
        case MinecraftVersion.V1_19_2 | MinecraftVersion.V1_20_1:
            return generate_fish_reviver_1_19_2(fish_item, fish_entity)


def generate_fish_reviver_1_19_2(
    fish_item: ResourceLocation, fish_entity: ResourceLocation
) -> DatapackFile:
    if fish_item.namespace == "minecraft":
        loot_table = f"frankenfish:revived_fish/{fish_item.path}"
    else:
        loot_table = f"frankenfish:revived_fish/{fish_item.namespace}/{fish_item.path}"
    function_src = """
        # give the fish resistance 5 so it doesn't die to lightning
        # also give it a loot table that only drops the fish, to prevent duping fish drops
        summon %s ~ ~ ~ { \
            ActiveEffects: [{Id: 11, Duration: 300, Amplifier: 5, ShowParticles: 1b}], \
            DeathLootTable: "%s" \
        }
        kill @s
    """ % (fish_entity, loot_table)
    function_src = fix_whitespace(function_src)

    return DatapackFile(fish_reviver_path(fish_item), function_src)
