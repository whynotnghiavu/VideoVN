import os
import re


from modules.MyLog import MyLog


def DoiTenFolderCon(root_dir):
    for foldername, subfolders, filenames in os.walk(root_dir):

        for subfolder in subfolders:
            subfolder_path = os.path.join(foldername, subfolder)
            match = re.match(r'^\d+', os.path.basename(subfolder_path))
            if match:
                so_thu_tu = int(match.group())
                new_name = os.path.join(foldername, f"{so_thu_tu:0>9}")
                try:
                    if (subfolder_path != new_name):
                        MyLog.info(f"DoiTenFolderCon: subfolder_path={subfolder_path}")
                        MyLog.info(f"DoiTenFolderCon: new_name={new_name}")

                        if os.path.exists(new_name):
                            os.remove(new_name)

                        os.rename(subfolder_path, new_name)
                except Exception as e:
                    MyLog.error(f"Object: {subfolder_path}")
                    MyLog.error(f"Lỗi đổi tên thư mục con: {e}")
                    exit()
            else:
                MyLog.error(f"Object: {subfolder_path}")
                MyLog.error("Không tìm thấy số thứ tự.")
                exit()
