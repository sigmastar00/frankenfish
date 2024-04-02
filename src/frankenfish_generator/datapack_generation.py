from .datapack_file import DatapackFile
from .minecraft_version import MinecraftVersion
from .resource_location import ResourceLocation
from .mcmeta_generation import generate_mcmeta
from .fish_reviver_generation import generate_fish_revivers
from typing import Final, Any
import json

TICK_TAG: Final = DatapackFile(
    "data/minecraft/tags/functions/tick.json",
    """
    {
        "values": [
            "frankenfish:tick"
        ]
    }
    """,
)

TICK_FUNCTION: Final = DatapackFile(
    "data/frankenfish/functions/tick.mcfunction",
    "execute as @e[type=#frankenfish:lightning] at @s run function #frankenfish:fish_reviver",
)

LIGHTNING_TAG: Final = DatapackFile(
    "data/frankenfish/tags/entity_types/lightning.json",
    """
    {
        "values": [
            "lightning_bolt",
            {
                "id": "ars_nouveau:an_lightning",
                "required": false
            },
            {
                "id": "ars_elemental:flash_lightning",
                "required": false
            }
        ]
    }
    """,
)


def generate_fish_reviver_tag(
    fishes: list[tuple[ResourceLocation, ResourceLocation]],
) -> DatapackFile:
    values: list[Any] = []
    for fish_item, _ in fishes:
        if fish_item.namespace == "minecraft":
            values.append(f"frankenfish:revive_{fish_item.path}")
        else:
            values.append(
                {
                    "id": f"frankenfish:{fish_item.namespace}/revive_{fish_item.path}",
                    "required": False,
                }
            )

    return DatapackFile(
        "data/frankenfish/tags/functions/fish_reviver.json",
        json.dumps({"values": values}, indent=4),
    )


def generate_datapack(
    fishes: list[tuple[ResourceLocation, ResourceLocation]],
    minecraft_version: MinecraftVersion,
) -> list[DatapackFile]:
    mcmeta = generate_mcmeta(minecraft_version)
    revivers = generate_fish_revivers(fishes, minecraft_version)
    reviver_tag = generate_fish_reviver_tag(fishes)
    return revivers + [mcmeta, reviver_tag, TICK_TAG, LIGHTNING_TAG, TICK_FUNCTION]
