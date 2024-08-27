import os


from modules.MyLog import MyLog
from modules.CONST import CONST
from modules.MyFile import MyFile
from modules.MyNewPath import MyNewPath
from modules.FormatFileSub import FormatFileSub


def TaoFileSubRieng(root_dir):
    sub_files = MyFile.TimKiem(root_dir, CONST.VTT)
    sub_files += MyFile.TimKiem(root_dir, CONST.SRT)

    for sub_file in sub_files:
        MyLog.info(f"TaoFileSubRieng: sub_file={sub_file}")

        # ! VTT và SRT có cùng độ dài
        new_file = MyNewPath(sub_file, CONST.SRT, CONST.ENGLISH_VVN_NGHIA)
        MyLog.info(f"TaoFileSubRieng: new_file={new_file}")

        if os.path.exists(new_file):
            os.remove(new_file)
        # # NOTE: Nếu không đổi
        # os.rename(sub_file,new_file)

        new_sub = FormatFileSub(sub_file)
        new_sub.save(new_file, encoding='utf-8')
