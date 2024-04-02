from typing import Final
from collections.abc import Iterable
import itertools
from .datapack_file import DatapackFile
from .minecraft_version import MinecraftVersion
from .resource_location import ResourceLocation
from .mcmeta_generation import generate_mcmeta
from .fish_reviver_generation import generate_fish_revivers
from .fish_detector_generation import (
    generate_fish_detectors,
    generate_fish_detector_tag,
)


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
    "execute as @e[type=#frankenfish:lightning] at @s run function #frankenfish:fish_detector",
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


def generate_datapack(
    fishes: Iterable[tuple[ResourceLocation, ResourceLocation]],
    minecraft_version: MinecraftVersion,
) -> list[DatapackFile]:
    mcmeta = generate_mcmeta(minecraft_version)
    detectors = generate_fish_detectors(map(lambda f: f[0], fishes), minecraft_version)
    detector_tag = generate_fish_detector_tag(map(lambda f: f[0], fishes))
    revivers = generate_fish_revivers(fishes, minecraft_version)
    return list(
        itertools.chain(
            detectors,
            revivers,
            [mcmeta, detector_tag, TICK_TAG, LIGHTNING_TAG, TICK_FUNCTION],
        )
    )
