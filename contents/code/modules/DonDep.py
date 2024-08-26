import os
import shutil


from modules.CONST import CONST
from modules.MyFile import MyFile
from modules.MyNewPath import MyNewPath


def DonDep(root_dir):
    # Xóa file video .mp4 và phiên bản 1
    mp4_files = MyFile.TimKiem(root_dir, CONST.MP4)
    for mp4_file in mp4_files:
        if not mp4_file.endswith(CONST.MP4_VN2_NGHIA):
            os.remove(mp4_file)
    # Xóa thư mục phụ của âm thanh video
    sub_files = MyFile.TimKiem(root_dir, CONST.VN2_VVN_NGHIA)
    for sub_file in sub_files:
        audio_folder = MyNewPath(sub_file, CONST.VN2_VVN_NGHIA, "")

        if os.path.exists(audio_folder):
            shutil.rmtree(audio_folder)

    MyFile.Xoa(root_dir, CONST.WAV)
    MyFile.Xoa(root_dir, CONST.SRT)
    MyFile.Xoa(root_dir, CONST.VTT)
    MyFile.Xoa(root_dir, CONST.ENGLISH_VVN_NGHIA)
    MyFile.Xoa(root_dir, CONST.MERGE_VVN_NGHIA)
    MyFile.Xoa(root_dir, CONST.VN1_VVN_NGHIA)
    # NOTE: Xóa các file khác
    # MyFile.Xoa(root_dir, ".zip")
    # MyFile.Xoa(root_dir, ".txt")
    # ! Xóa các file khác
