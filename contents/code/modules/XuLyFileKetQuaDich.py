import os


from modules.CONST import CONST
from modules.ThayTheVanBan import ThayTheVanBan


def XuLyFileKetQuaDich():
    file_tieng_viet = os.path.join(os.getcwd(), CONST.MERGED_VIETNAM_FILE)
    with open(file_tieng_viet, "r", encoding="utf-8") as file:
        contents = file.read()

    contents = contents.replace("@@ @", "@@@")
    contents = contents.replace("@@@", "\n\n@@@\n\n")
    contents = ThayTheVanBan(contents)

    with open(file_tieng_viet, "w", encoding="utf-8") as file:
        file.write(contents)
