from modules.MyLog import MyLog
from modules.MyFile import MyFile

EXTENSIONS = [
    # NOTE: Các đuôi file cần xóa
    ".wav",

    # ".de.srt",
    # ".id.srt",
    # ".pt.srt",
    # ".it.srt",
    # ".ro.srt",
    # ".es.srt",
    # ".th.srt",
    # ".fr.srt",
    # ".pl.srt",




]


def XoaFileKhongDung(root_dir):
    for i in EXTENSIONS:
        MyLog.info(f"XoaFileKhongDung: Xóa file {i}")
        MyFile.Xoa(root_dir, i)
