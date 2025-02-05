import os


def find_and_rename_jpegs(folder: str):
    for filename in os.listdir(folder):
        file_path = f"{folder}/{filename}"

        if os.path.isfile(file_path):
            with open(file_path, "rb") as f:
                is_jpeg = f.read(2) == b'\xFF\xD8'

            if is_jpeg and not filename.endswith(".jpeg"):
                new_name = f"{folder}/{filename}.jpeg"
                os.rename(file_path, new_name)


find_and_rename_jpegs("./random_files")
