import os


from modules.MyLog import MyLog
from modules.CONST import CONST
from modules.MyFile import MyFile
from modules.MyExecute import MyExecute
from modules.MyNewPath import MyNewPath


def GhepAmThanh(root_dir):
    sub_files = MyFile.TimKiem(root_dir, CONST.VN2_VVN_NGHIA)
    for sub_file in sub_files:
        MyLog.info(f"GhepAmThanh: sub_file={sub_file}")

        mp4_file = MyNewPath(sub_file, CONST.VN2_VVN_NGHIA, CONST.MP4)
        MyLog.info(f"GhepAmThanh: mp4_file={mp4_file}")

        audio_file = MyNewPath(sub_file, CONST.VN2_VVN_NGHIA, CONST.WAV)
        MyLog.info(f"GhepAmThanh: audio_file={audio_file}")

        video_vn1_file = MyNewPath(sub_file, CONST.VN2_VVN_NGHIA, CONST.MP4_VN1_NGHIA)
        MyLog.info(f"GhepAmThanh: video_vn1_file={video_vn1_file}")

        video_vn2_file = MyNewPath(sub_file, CONST.VN2_VVN_NGHIA, CONST.MP4_VN2_NGHIA)
        MyLog.info(f"GhepAmThanh: video_vn2_file={video_vn2_file}")

        if os.path.exists(video_vn1_file):
            os.remove(video_vn1_file)

        if os.path.exists(video_vn2_file):
            os.remove(video_vn2_file)

        MyExecute(f'ffmpeg -i {mp4_file} -c:v copy -an {video_vn1_file}')
        MyExecute(f'ffmpeg -i {video_vn1_file} -i {audio_file} -c:v copy -c:a aac -strict experimental {video_vn2_file}')
