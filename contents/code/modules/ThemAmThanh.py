import os
import pysrt
from tqdm import tqdm


from moviepy.editor import VideoFileClip


from modules.CONST import CONST
from modules.MyFile import MyFile
from modules.MyNewPath import MyNewPath

from modules.TinhGiay import TinhGiay
from modules.MyExecute import MyExecute
from modules.MyNoSound import MyNoSound


def ThemAmThanh(root_dir):
    sub_files = MyFile.TimKiem(root_dir, CONST.VN2_VVN_NGHIA)
    for sub_file in tqdm(sub_files, desc='Thêm âm thanh', unit='sub_file'):
        audio_folder = MyNewPath(sub_file, CONST.VN2_VVN_NGHIA, "")
        mp4_file = MyNewPath(sub_file, CONST.VN2_VVN_NGHIA, CONST.MP4)

        video = VideoFileClip(mp4_file)
        time_video = video.duration
        video.close()

        # new_folder2 = os.path.join(audio_folder, "data")

        # if os.path.exists(new_folder2):
        #     shutil.rmtree(new_folder2)
        # os.makedirs(new_folder2, exist_ok=True)

        subs = pysrt.open(sub_file, encoding='utf-8')
        flag = pysrt.SubRipTime(hours=0, minutes=0, seconds=0, milliseconds=0)
        for sub in subs:
            # tqdm(subs, desc='Thêm âm thanh', unit='sub'):
            # for sub in tqdm(subs, desc='Thêm âm thanh', unit='sub'):
            _time = TinhGiay(sub.start - flag)
            _file = os.path.join(audio_folder, f"{sub.index:0>9} - Copy{CONST.WAV}")
            #
            #
            #
            # file Copy
            #
            #
            #
            #
            #
            MyNoSound(time=_time, file=_file)
            flag = sub.end
        # end.wav
        _time = time_video - TinhGiay(sub.end)
        _file = os.path.join(audio_folder, f"end{CONST.WAV}")
        MyNoSound(_time, _file)
