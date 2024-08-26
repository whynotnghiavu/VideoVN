import os


from modules.MyLog import MyLog
from modules.CONST import CONST
from modules.MyFile import MyFile
from modules.MyNewPath import MyNewPath


def DoiTenFileSub(root_dir):
    sub_files = MyFile.TimKiem(root_dir, CONST.VN2_VVN_NGHIA)
    for sub_file in sub_files:
        MyLog.info(f"DoiTenFileSub: sub_file={sub_file}")
        new_file = MyNewPath(sub_file, CONST.VN2_VVN_NGHIA, CONST.VN3_VVN_NGHIA)
        MyLog.info(f"DoiTenFileSub: new_file={new_file}")

        if os.path.exists(new_file):
            os.remove(new_file)

        os.rename(sub_file, new_file)
