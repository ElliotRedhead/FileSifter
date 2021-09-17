import os
from tkinter.filedialog import askdirectory


def prompt_user():
    directory = input(
        "Enter path of directory to inspect (or leave blank for directory picker): "
    )
    if directory == "":
        directory = askdirectory()
    if not os.path.exists(directory) or not os.path.isdir(directory):
        print("The chosen path was not found, please input a valid directory. \r")
        return prompt_user()
    return directory


def file_sifter(directory):
    object_sizes = []
    for dir_path, dirnames, filenames in os.walk(directory):
        dir_size = 0
        for filename in filenames:
            filepath = os.path.join(dir_path, filename)
            dir_size += os.path.getsize(filepath) / 1024 ** 2
        dir_size = round(dir_size, 2)
        if dir_size > 0:
            object_sizes.append({"path": dir_path, "size(MB)": dir_size})
    object_sizes.sort(key=lambda x: x["size(MB)"], reverse=True)
    for object in object_sizes:
        print(object["path"], f"{object['size(MB)']}MB")


file_sifter(prompt_user())
