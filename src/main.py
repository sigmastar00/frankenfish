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
ENVIRONMENTAL_FISH: Final = ["koi"]
CRITTERS_AND_COMPANIONS_FISH: Final = ["koi_fish"]
ALEXS_MOBS_FISH: Final[list[str | tuple[str, str, str]]] = [
    ("blobfish", "blobfish", "BlobfishScale: 1.0f"),
    "cosmic_cod",
    "flying_fish",
]


def make_fish_list(
    namespace: str,
    input: Iterable[str | tuple[str, str] | tuple[str, str, str | None]],
) -> list[tuple[ResourceLocation, ResourceLocation, str | None]]:
    result: list[tuple[ResourceLocation, ResourceLocation, str | None]] = []
    for fish in input:
        if isinstance(fish, tuple):
            if len(fish) == 2:
                result.append(
                    (
                        ResourceLocation(namespace, fish[0]),
                        ResourceLocation(namespace, fish[1]),
                        None,
                    )
                )
            elif len(fish) == 3:
                result.append(
                    (
                        ResourceLocation(namespace, fish[0]),
                        ResourceLocation(namespace, fish[1]),
                        fish[2],
                    )
                )
        else:
            result.append(
                (
                    ResourceLocation(namespace, fish),
                    ResourceLocation(namespace, fish),
                    None,
                )
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
    environmental_fish = make_fish_list("environmental", ENVIRONMENTAL_FISH)
    critters_and_companions_fish = make_fish_list(
        "crittersandcompanions", CRITTERS_AND_COMPANIONS_FISH
    )
    alexs_mobs_fish = make_fish_list("alexsmobs", ALEXS_MOBS_FISH)

    match mc_version:
        case MinecraftVersion.V1_19_2:
            all_fish = (
                vanilla_fish
                + aquaculture_fish
                + nether_depths_fish
                + environmental_fish
                + critters_and_companions_fish
                + alexs_mobs_fish
            )
        case MinecraftVersion.V1_20_1:
            all_fish = (
                vanilla_fish
                + aquaculture_fish
                + nether_depths_fish
                + critters_and_companions_fish
                + alexs_mobs_fish
            )

    datapack_files = generate_datapack(all_fish, mc_version)
    write_datapack(f"frankenfish-{args.minecraft_version}.zip", datapack_files)


if __name__ == "__main__":
    main()
