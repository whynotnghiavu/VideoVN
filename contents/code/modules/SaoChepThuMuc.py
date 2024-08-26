import os
import shutil
import re


from modules.CONST import CONST


def SaoChepThuMuc(root_dir):
    new_name = os.path.basename(root_dir)
    new_name = re.sub(r'[^a-zA-Z0-9]', '', new_name) + CONST.NEW_FOLDER
    new_name = os.path.join(os.path.dirname(root_dir), new_name)

    if os.path.exists(new_name):
        shutil.rmtree(new_name)

    shutil.copytree(root_dir, new_name)

    return new_name
