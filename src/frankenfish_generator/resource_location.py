from dataclasses import dataclass


@dataclass
class ResourceLocation:
    namespace: str
    path: str

    def __str__(self) -> str:
        return f"{self.namespace}:{self.path}"
