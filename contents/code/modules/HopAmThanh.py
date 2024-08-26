import os
from tqdm import tqdm
from pydub import AudioSegment


from modules.MyLog import MyLog
from modules.CONST import CONST
from modules.MyFile import MyFile
from modules.MyNewPath import MyNewPath


def HopAmThanh(root_dir):
    sub_files = MyFile.TimKiem(root_dir, CONST.VN2_VVN_NGHIA)
    for sub_file in sub_files:
        MyLog.info(f"HopAmThanh: sub_file={sub_file}")
        audio_folder = MyNewPath(sub_file, CONST.VN2_VVN_NGHIA, "")
        MyLog.info(f"HopAmThanh: audio_folder={audio_folder}")
        new_file = MyNewPath(sub_file, CONST.VN2_VVN_NGHIA, CONST.WAV)
        MyLog.info(f"HopAmThanh: new_file={new_file}")

        if os.path.exists(new_file):
            os.remove(new_file)

        wav_files = MyFile.TimKiem(audio_folder, CONST.WAV)
        merged_audio = AudioSegment.empty()
        for wav_file in tqdm(wav_files, desc='Hợp', unit='wav_file'):
            audio = AudioSegment.from_wav(wav_file)
            merged_audio += audio

        merged_audio.export(new_file, format="wav")
