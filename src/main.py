from frankenfish_generator import generate_datapack, write_datapack, MinecraftVersion


def main() -> None:
    datapack_files = generate_datapack([], MinecraftVersion.V1_19_2)
    write_datapack("frankenfish.zip", datapack_files)


if __name__ == "__main__":
    main()
