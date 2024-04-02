from collections.abc import Iterable
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
NETHER_DEPTHS_FISH: Final[list[str | tuple[str, str]]] = [
    "lava_pufferfish",
    "obsidianfish",
    "searing_cod",
    "bonefish",
    "wither_bonefish",
    "blazefish",
    "magmacubefish",
    "glowdine",
    "soulsucker",
    ("fortress_grouper", "fortressgrouper"),
    "eyeball_fish",
]


def make_fish_list(
    namespace: str,
    input: Iterable[str | tuple[str, str]],
) -> list[tuple[ResourceLocation, ResourceLocation]]:
    result = list()
    for fish in input:
        if isinstance(fish, tuple):
            result.append(
                (
                    ResourceLocation(namespace, fish[0]),
                    ResourceLocation(namespace, fish[1]),
                )
            )
        else:
            result.append(
                (ResourceLocation(namespace, fish), ResourceLocation(namespace, fish))
            )
    return result


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

    vanilla_fish = make_fish_list("minecraft", VANILLA_FISH)
    aquaculture_fish = make_fish_list("aquaculture", AQUACULTURE_FISH)
    nether_depths_fish = make_fish_list("netherdepthsupgrade", NETHER_DEPTHS_FISH)

    datapack_files = generate_datapack(
        vanilla_fish + aquaculture_fish + nether_depths_fish, mc_version
    )
    write_datapack(f"frankenfish-{args.minecraft_version}.zip", datapack_files)


if __name__ == "__main__":
    main()
