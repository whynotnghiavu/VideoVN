from modules.CONST import CONST
from modules.MyFile import MyFile


def XoaFileSub(root_dir):
    MyFile.Xoa(root_dir, CONST.VN2_VVN_NGHIA)
    MyFile.Xoa(root_dir, CONST.VN3_VVN_NGHIA)
