from dataclasses import dataclass


@dataclass
class DatapackFile:
    file_path: str
    file_contents: str
