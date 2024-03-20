from frankenfish_generator import (
    generate_datapack,
    write_datapack,
    MinecraftVersion,
    ResourceLocation,
)
from argparse import ArgumentParser
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
    arg_parser = ArgumentParser()
    arg_parser.add_argument("minecraft_version", choices=["1.19.2", "1.20.1"])
    args = arg_parser.parse_args()
    match args.minecraft_version:
        case "1.19.2":
            mc_version = MinecraftVersion.V1_19_2
        case "1.20.1":
            mc_version = MinecraftVersion.V1_20_1
        case _:
            raise ValueError

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

    datapack_files = generate_datapack(vanilla_fish + aquaculture_fish, mc_version)
    write_datapack(f"frankenfish-{args.minecraft_version}.zip", datapack_files)


if __name__ == "__main__":
    main()
