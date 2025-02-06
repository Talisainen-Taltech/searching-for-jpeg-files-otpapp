import os
import requests
import zipfile


def find_and_rename_jpegs(folder: str):
    if not os.path.isdir("./random_files"):
        response = requests.get("https://upload.itcollege.ee/~aleksei/random_files_without_extension.zip")

        zip_path = "./files.zip"
        with open(zip_path, "wb") as f:
            f.write(response.content)

        with zipfile.ZipFile(zip_path, "r") as zipf:
            zipf.extractall("./")

        os.remove(zip_path)

    for filename in os.listdir(folder):
        file_path = f"{folder}/{filename}"

        if os.path.isfile(file_path):
            with open(file_path, "rb") as f:
                is_jpeg = f.read(2) == b'\xFF\xD8'

            if is_jpeg and not filename.endswith(".jpeg"):
                new_name = f"{folder}/{filename}.jpeg"
                os.rename(file_path, new_name)
            elif not is_jpeg:
                os.remove(file_path)


find_and_rename_jpegs("./random_files")
