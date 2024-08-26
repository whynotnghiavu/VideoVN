import os


from modules.MyLog import MyLog
from modules.CONST import CONST
from modules.MyFile import MyFile
from modules.MyNewPath import MyNewPath
from modules.FormatFileSub import FormatFileSub


def TachFileSub(root_dir):
    infor_file = open(CONST.INFOR_FILE, "r", encoding="utf-8")
    sub_files = infor_file.readlines()

    merged_file = open(CONST.MERGED_VIETNAM_FILE, "r", encoding="utf-8")
    contents = merged_file.read()
    contents = contents.split("@@@")

    if len(contents) != len(sub_files):
        MyLog.error(f"Lỗi: Số file và tên không bằng nhau")
        MyLog.error(f"len(sub_files) = {len(sub_files)}")
        MyLog.error(f"len(contents) = {len(contents)}")
        exit()

    # "Tạo file sub Việt Nam phiên bản 1"
    MyLog.info(f"TachFileSub: Tạo file sub Việt Nam phiên bản 1")
    for i, sub_file in enumerate(sub_files):
        MyLog.info(f"TachFileSub: sub_file={sub_file}")
        new_file = MyNewPath(sub_file, CONST.MERGE_VVN_NGHIA, CONST.VN1_VVN_NGHIA)
        MyLog.info(f"TachFileSub: new_file={new_file}")

        if os.path.exists(new_file):
            os.remove(new_file)

        with open(new_file, "w", encoding="utf-8") as split_file:
            split_file.write(contents[i])

    # Tạo file sub Việt Nam phiên bản 2 (format file 1)
    MyLog.info(f"TachFileSub: Tạo file sub Việt Nam phiên bản 2 (format file 1)")
    sub_files = MyFile.TimKiem(root_dir, CONST.VN1_VVN_NGHIA)
    for sub_file in sub_files:
        MyLog.info(f"TachFileSub: sub_file={sub_file}")
        new_file = MyNewPath(sub_file, CONST.VN1_VVN_NGHIA, CONST.VN2_VVN_NGHIA)
        MyLog.info(f"TachFileSub: new_file={new_file}")

        if os.path.exists(new_file):
            os.remove(new_file)

        new_sub = FormatFileSub(sub_file)
        new_sub.save(new_file, encoding='utf-8')
