import os
import shutil
import re


from modules.CONST import CONST


def copy_folders_and_files(root_folder, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    for root, dirs, files in os.walk(root_folder):
        # Tạo Folder
        for dir in dirs:
            dest_dir_path = os.path.join(dest_folder, os.path.relpath(os.path.join(root, dir), root_folder))
            if not os.path.exists(dest_dir_path):
                os.makedirs(dest_dir_path)

        # Tạo File
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, root_folder)
            dest_file_path = os.path.join(dest_folder, relative_path + CONST.SAVE_FILE)
            dest_file_dir = os.path.dirname(dest_file_path)

            if not os.path.exists(dest_file_dir):
                os.makedirs(dest_file_dir)

            # Copy files of size 0KB
            if file.endswith(CONST.SAVE_FILE) and os.path.getsize(file_path) == 0:
                shutil.copy2(file_path, dest_file_path)
            else:
                open(dest_file_path, 'w').close()


def LuuCauTrucThuMuc(root_dir):

    save_folder = os.path.basename(root_dir)
    save_folder = re.sub(r'[^a-zA-Z0-9]', '', save_folder) + CONST.SAVE_FOLDER
    save_folder = os.path.join(os.path.dirname(root_dir), save_folder)

    if os.path.exists(save_folder):
        shutil.rmtree(save_folder)

    copy_folders_and_files(root_dir, save_folder)
