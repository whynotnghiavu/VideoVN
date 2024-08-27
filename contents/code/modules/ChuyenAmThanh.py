import os
import shutil
import pysrt
from tqdm import tqdm


from modules.MyLog import MyLog
from modules.CONST import CONST
from modules.MyFile import MyFile
from modules.MyNewPath import MyNewPath
from modules.MyTextToSpeech import MyTextToSpeech


def ChuyenAmThanh(root_dir):
    sub_files = MyFile.TimKiem(root_dir, CONST.VN2_VVN_NGHIA)
    for sub_file in sub_files:
        MyLog.info(f"ChuyenAmThanh: sub_file={sub_file}")
        audio_folder = MyNewPath(sub_file, CONST.VN2_VVN_NGHIA, "")
        MyLog.info(f"ChuyenAmThanh: audio_folder={audio_folder}")

        if os.path.exists(audio_folder):
            shutil.rmtree(audio_folder)
        os.makedirs(audio_folder, exist_ok=True)

        subs = pysrt.open(sub_file, encoding='utf-8')
        for sub in tqdm(subs, desc='Chuyển', unit='sub'):
            audio_file = os.path.join(audio_folder, f"{sub.index:0>9}{CONST.WAV}")
            MyTextToSpeech(sub.start, sub.end, sub.text, audio_file)
