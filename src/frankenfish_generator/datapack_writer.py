from .datapack_file import DatapackFile
from zipfile import ZipFile, ZIP_DEFLATED
import dataclasses


def write_datapack(
    output_zip_filepath: str, datapack_files: list[DatapackFile]
) -> None:
    with ZipFile(output_zip_filepath, "w", ZIP_DEFLATED) as zip_file:
        for compressed_file_name, file_contents in map(
            dataclasses.astuple, datapack_files
        ):
            zip_file.writestr(compressed_file_name, file_contents)
