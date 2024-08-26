from modules.MyLog import MyLog
from modules.CONST import CONST
from modules.MyFile import MyFile


def ThongTinFile(root_dir, extensions):
    type = ""
    count = 0
    for i in extensions:
        type += f" {i} "
        count += MyFile.SoLuong(root_dir, f"{i}")
    print(f'[{type} = {count}]', end=" ")


def GhiThongTin(root_dir):
    MyLog.title(root_dir)
    if not root_dir:
        MyLog.error("GhiThongTin: Chưa chọn thư mục")
        return

    ThongTinFile(root_dir, [CONST.MP4])
    ThongTinFile(root_dir, [CONST.VTT])
    ThongTinFile(root_dir, [CONST.SRT])
    ThongTinFile(root_dir, [CONST.VTT, CONST.SRT])
    ThongTinFile(root_dir, [CONST.VTT, CONST.SRT, CONST.MP4])
    print()

    ThongTinFile(root_dir, [".rar"])
    ThongTinFile(root_dir, [".zip"])
    ThongTinFile(root_dir, [".md"])
    print()

    ThongTinFile(root_dir, [CONST.ENGLISH_VVN_NGHIA])
    ThongTinFile(root_dir, [CONST.MERGE_VVN_NGHIA])
    print()

    ThongTinFile(root_dir, [CONST.VN1_VVN_NGHIA])
    ThongTinFile(root_dir, [CONST.VN2_VVN_NGHIA])
    print()

    ThongTinFile(root_dir, [CONST.MP4_VN1_NGHIA])
    ThongTinFile(root_dir, [CONST.MP4_VN2_NGHIA])
    print()

    ThongTinFile(root_dir, [CONST.SAVE_FILE])
    ThongTinFile(root_dir, [CONST.WAV])
    ThongTinFile(root_dir, [CONST.VN3_VVN_NGHIA])
    print()
