from .minecraft_version import MinecraftVersion
from .datapack_file import DatapackFile


def generate_mcmeta(minecraft_version: MinecraftVersion) -> DatapackFile:
    match minecraft_version:
        case MinecraftVersion.V1_19_2:
            return generate_mcmeta_1_19_2()
        case _:
            raise NotImplementedError


def generate_mcmeta_1_19_2() -> DatapackFile:
    return DatapackFile(
        "pack.mcmeta",
        """
        {
            "pack": {
                "pack_format": 10,
                "description": "Fishify Revivify!"
            }
        }
        """,
    )
