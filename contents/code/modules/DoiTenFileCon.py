import os
import re


from modules.MyLog import MyLog
from modules.MyFile import MyFile


def DoiTenFileCon(root_dir):
    files = MyFile.TimKiem(root_dir, ".mp4")
    files += MyFile.TimKiem(root_dir, ".vtt")
    files += MyFile.TimKiem(root_dir, ".srt")

    for file in files:
        match = re.match(r'^\d+', os.path.basename(file))
        if match:
            so_thu_tu = int(match.group())
            _, ext = os.path.splitext(file)

            new_name = os.path.join(os.path.dirname(file), f"{so_thu_tu:0>9}{ext}")

            try:
                MyLog.info(f"DoiTenFileCon: file={file}")
                MyLog.info(f"DoiTenFileCon: new_name={new_name}")

                # if os.path.exists(new_name):
                #     os.remove(new_name)

                os.rename(file, new_name)
            except Exception as e:
                MyLog.error(f"Object: {file}")
                MyLog.error(f"Lỗi đổi tên file con: {e}")
                exit()

        else:
            MyLog.error(f"Object: {file}")
            MyLog.error("Không tìm thấy số thứ tự.")
            exit()
