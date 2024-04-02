from typing import Any
from collections.abc import Iterable
import json
from .minecraft_version import MinecraftVersion
from .resource_location import ResourceLocation
from .datapack_file import DatapackFile
from .mcfunction import fix_whitespace


def generate_fish_detectors(
    fish_items: Iterable[ResourceLocation],
    minecraft_version: MinecraftVersion,
) -> Iterable[DatapackFile]:
    return map(lambda fish: generate_fish_detector(fish, minecraft_version), fish_items)


def fish_detector_path(fish_item: ResourceLocation) -> str:
    if fish_item.namespace == "minecraft":
        return f"data/frankenfish/functions/detect_{fish_item.path}.mcfunction"
    else:
        return f"data/frankenfish/functions/{fish_item.namespace}/detect_{fish_item.path}.mcfunction"


def generate_fish_detector(
    fish_item: ResourceLocation,
    minecraft_version: MinecraftVersion,
) -> DatapackFile:
    match minecraft_version:
        case MinecraftVersion.V1_19_2 | MinecraftVersion.V1_20_1:
            return generate_fish_detector_1_19_2(fish_item)


def generate_fish_detector_1_19_2(fish_item: ResourceLocation) -> DatapackFile:
    if fish_item.namespace == "minecraft":
        reviver_name = f"frankenfish:revive_{fish_item.path}"
    else:
        reviver_name = f"frankenfish:{fish_item.namespace}/revive_{fish_item.path}"

    function_src = """
        execute \
            as @e[type=item,distance=..3.2,nbt={Item: {id: "%s"}}] \
            at @s \
            run function %s
    """ % (fish_item, reviver_name)
    function_src = fix_whitespace(function_src)

    return DatapackFile(fish_detector_path(fish_item), function_src)


def generate_fish_detector_tag(
    fishes: Iterable[ResourceLocation],
) -> DatapackFile:
    values: list[Any] = []
    for fish_item in fishes:
        if fish_item.namespace == "minecraft":
            values.append(f"frankenfish:detect_{fish_item.path}")
        else:
            values.append(
                {
                    "id": f"frankenfish:{fish_item.namespace}/detect_{fish_item.path}",
                    "required": False,
                }
            )

    return DatapackFile(
        "data/frankenfish/tags/functions/fish_detector.json",
        json.dumps({"values": values}, indent=4),
    )
