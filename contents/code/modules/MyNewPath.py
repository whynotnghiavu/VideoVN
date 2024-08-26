import os


def MyNewPath(file_path, old_ext, new_ext):
    return file_path[:-len(old_ext)] + new_ext
