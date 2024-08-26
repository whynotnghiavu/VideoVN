import os
import glob


class MyFile:
    def TimKiem(root_dir, extension):
        return glob.glob(os.path.join(root_dir, f'**/*{extension}'), recursive=True)

    def Xoa(root_dir, extension):
        file_paths = MyFile.TimKiem(root_dir, extension)
        for file_path in file_paths:
            os.remove(file_path)

    def SoLuong(root_dir, extension):
        file_paths = MyFile.TimKiem(root_dir, extension)
        return len(file_paths)
