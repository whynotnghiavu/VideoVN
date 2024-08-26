import os


from modules.MyLog import MyLog
from modules.CONST import CONST
from modules.MyFile import MyFile


def HopNhatTatCaFileSub(root_dir):
    sub_files = MyFile.TimKiem(root_dir, CONST.MERGE_VVN_NGHIA)

    if not os.path.exists(CONST.BACKUP_FOLDER):
        os.makedirs(CONST.BACKUP_FOLDER)

    infor_file = open(CONST.INFOR_FILE, "w", encoding="utf-8")
    merged_file = open(CONST.MERGED_FILE, "w", encoding="utf-8")

    for sub_file in sub_files:
        MyLog.info(f"HopNhatTatCaFileSub: sub_file={sub_file}")

        with open(sub_file, "r", encoding="utf-8") as srt_file:
            contents = srt_file.read()

        merged_file.write("@@@\n")
        merged_file.write(contents)
        merged_file.write("\n")

        infor_file.write(f"{sub_file}\n")

    infor_file.close()
    merged_file.close()
