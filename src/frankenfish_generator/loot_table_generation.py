from collections.abc import Iterable
import json
from .resource_location import ResourceLocation
from .datapack_file import DatapackFile


def generate_loot_tables(
    fish_items: Iterable[ResourceLocation],
) -> Iterable[DatapackFile]:
    return map(generate_loot_table, fish_items)


def loot_table_path(fish_item: ResourceLocation) -> str:
    if fish_item.namespace == "minecraft":
        return f"data/frankenfish/loot_tables/revived_fish/{fish_item.path}.json"
    else:
        return f"data/frankenfish/loot_tables/revived_fish/{fish_item.namespace}/{fish_item.path}.json"


def generate_loot_table(fish_item: ResourceLocation) -> DatapackFile:
    return DatapackFile(
        loot_table_path(fish_item),
        json.dumps(
            {
                "type": "entity",
                "pools": [
                    {
                        "rolls": 1,
                        "entries": [
                            {"weight": 1, "type": "item", "name": str(fish_item)}
                        ],
                    }
                ],
            }
        ),
    )
