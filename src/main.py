from frankenfish_generator import (
    generate_datapack,
    write_datapack,
    MinecraftVersion,
    ResourceLocation,
)
from typing import Final

VANILLA_FISH: Final = ["salmon", "cod", "pufferfish", "tropical_fish"]
AQUACULTURE_FISH: Final = [
    "atlantic_cod",
    "blackfish",
    "pacific_halibut",
    "atlantic_halibut",
    "atlantic_herring",
    "pink_salmon",
    "pollock",
    "rainbow_trout",
    "bayad",
    "boulti",
    "capitaine",
    "synodontis",
    "smallmouth_bass",
    "bluegill",
    "brown_trout",
    "carp",
    "catfish",
    "gar",
    "minnow",
    "muskellunge",
    "perch",
    "arapaima",
    "piranha",
    "tambaqui",
    "brown_shrooma",
    "red_shrooma",
    "jellyfish",
    "red_grouper",
    "tuna",
]


def main() -> None:
    vanilla_fish = list(
        map(
            lambda fish: (
                ResourceLocation("minecraft", fish),
                ResourceLocation("minecraft", fish),
            ),
            VANILLA_FISH,
        )
    )
    aquaculture_fish = list(
        map(
            lambda fish: (
                ResourceLocation("aquaculture", fish),
                ResourceLocation("aquaculture", fish),
            ),
            AQUACULTURE_FISH,
        )
    )

    datapack_files = generate_datapack(
        vanilla_fish + aquaculture_fish, MinecraftVersion.V1_19_2
    )
    write_datapack("frankenfish.zip", datapack_files)


if __name__ == "__main__":
    main()
