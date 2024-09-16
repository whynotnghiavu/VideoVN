import re
import os


def rename_file(old_name):
    new_name = old_name
    if os.path.isfile(new_name):
        new_name = os.path.basename(new_name)
        new_name = re.sub(r'[^a-z.0-9]', '', new_name)
        new_name = os.path.join((os.path.dirname(old_name)), new_name)
    print(old_name)
    print(new_name)

    if new_name != old_name:
        os.rename(old_name, new_name)


def rename_folder(old_name):
    new_name = old_name
    if os.path.isfile(new_name):
        new_name = os.path.basename(new_name)
        new_name = re.sub(r'[^a-z0-9]', '', new_name)
        new_name = os.path.join((os.path.dirname(old_name)), new_name)
    if new_name != old_name:
        os.rename(old_name, new_name)


def my_rename(folder_path):
    # Sử dụng os.walk để lặp qua tất cả các thư mục, thư mục con và tệp
    for folder, subfolders, files in os.walk(folder_path):
        # print(f"Thư mục: {folder}")
        rename_folder(folder)

        # Lặp qua tất cả các thư mục con
        for subfolder in subfolders:
            subfolder_path = os.path.join(folder, subfolder)
            # print(f"Thư mục con: {subfolder_path}")
            rename_folder(subfolder_path)

        # Lặp qua tất cả các tệp trong thư mục hiện tại
        for file in files:
            file_path = os.path.join(folder, file)
            # print(f"Tệp: {file_path}")
            rename_file(file_path)


# Thư mục gốc
folder_root = r"C:\Users\vvn20206205\Desktop\Authorization"
my_rename(folder_root)
