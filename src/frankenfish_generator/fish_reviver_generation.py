from .minecraft_version import MinecraftVersion
from .resource_location import ResourceLocation
from .datapack_file import DatapackFile
from .mcfunction import fix_whitespace
from itertools import starmap


def generate_fish_revivers(
    fishes: list[tuple[ResourceLocation, ResourceLocation]],
    minecraft_version: MinecraftVersion,
) -> list[DatapackFile]:
    return list(
        starmap(
            lambda item, entity: generate_fish_reviver(item, entity, minecraft_version),
            fishes,
        )
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
    if minecraft_version == MinecraftVersion.V1_19_2:
        return generate_fish_reviver_1_19_2(fish_item, fish_entity)
    else:
        raise NotImplementedError


def generate_fish_reviver_1_19_2(
    fish_item: ResourceLocation, fish_entity: ResourceLocation
) -> DatapackFile:
    function_src = """
        execute
            as @e[type=item,distance=..1,nbt={Item: {id: "%s"}}]
            at @s
            run summon %s ~ ~ ~ {
                ActiveEffects: [{Id: 11, Duration: 300, Amplifier: 5, ShowParticles: 1b}]
            }
    """ % (fish_item, fish_entity)
    function_src = fix_whitespace(function_src)

    return DatapackFile(fish_reviver_path(fish_item), function_src)
