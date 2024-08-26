from modules.MyLog import MyLog
from modules.CONST import CONST
from modules.MyFile import MyFile
from modules.MyNewPath import MyNewPath


def KiemTraTenGiongNhau(root_dir):
    mp4_files = MyFile.TimKiem(root_dir, CONST.MP4)
    sub_files = MyFile.TimKiem(root_dir, CONST.SRT)
    sub_files += MyFile.TimKiem(root_dir, CONST.VTT)

    mp4_files = [MyNewPath(mp4, CONST.MP4, "") for mp4 in mp4_files]
    # ! VTT và SRT có cùng độ dài
    sub_files = [MyNewPath(sub, CONST.SRT, "") for sub in sub_files]

    results = list(set(mp4_files) ^ set(sub_files))

    if results:
        MyLog.error("Các file khác tên:")
        for result in results:
            MyLog.error(result)
        exit()
    else:
        MyLog.info(f"KiemTraTenGiongNhau: Các file sub và video có tên giống nhau")
