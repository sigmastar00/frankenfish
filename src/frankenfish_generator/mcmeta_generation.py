from .minecraft_version import MinecraftVersion
from .datapack_file import DatapackFile


def generate_mcmeta(minecraft_version: MinecraftVersion) -> DatapackFile:
    match minecraft_version:
        case MinecraftVersion.V1_19_2:
            return generate_mcmeta_1_19_2()
        case MinecraftVersion.V1_20_1:
            return generate_mcmeta_1_20_1()


def generate_mcmeta_1_19_2() -> DatapackFile:
    return DatapackFile(
        "pack.mcmeta",
        """
        {
            "pack": {
                "pack_format": 10,
                "description": "Bring your fish to life! Frankenfish for Minecraft 1.19.2"
            }
        }
        """,
    )


def generate_mcmeta_1_20_1() -> DatapackFile:
    return DatapackFile(
        "pack.mcmeta",
        """
        {
            "pack": {
                "pack_format": 15,
                "description": "Bring your fish to life! Frankenfish for Minecraft 1.20.1"
            }
        }
        """,
    )
