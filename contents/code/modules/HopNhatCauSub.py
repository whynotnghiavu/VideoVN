import os
import pysrt


from modules.MyLog import MyLog
from modules.CONST import CONST
from modules.MyFile import MyFile
from modules.MyNewPath import MyNewPath


def HopNhatCauSub(root_dir):
    sub_files = MyFile.TimKiem(root_dir, CONST.ENGLISH_VVN_NGHIA)

    for sub_file in sub_files:
        MyLog.info(f"HopNhatCauSub: sub_file={sub_file}")
        new_file = MyNewPath(sub_file, CONST.ENGLISH_VVN_NGHIA, CONST.MERGE_VVN_NGHIA)
        MyLog.info(f"HopNhatCauSub: new_file={new_file}")

        if os.path.exists(new_file):
            os.remove(new_file)

        subs_old = pysrt.open(sub_file, encoding='utf-8')
        subs_new = pysrt.SubRipFile()

        if (len(subs_old) == 0):
            MyLog.error(f"File sub không có nội dung: {sub_file}")
            exit()

        flag = 0
        index = 1
        text = ""

        for i in range(len(subs_old)):
            text += " " + subs_old[i].text
            try:
                condition = subs_old[i].text[-1]
            except:
                condition = " "
            # NOTE: Chỉnh sửa điều kiện ngắt câu
            # Trong youtube không có dấu thì ngắt 500 kí tự
            # if len(text) > 500:
            # Ngắt theo kí tự
            # if condition in [".", "?", "..."]:
            # xxxxxxxxxxxxxxx
            # if condition in [".", "?", "..."] and len(text) > 100:
            # if condition in [".", "?", "..."] and len(text) > 150:
            # if condition in [".", "?", "..."] and len(text) > 200:
            # if condition in [".", "?", "..."] and len(text) > 300:
            # xxxxxxxxxxxxxxx
            # if len(text) > 1000 or (len(text) > 100 and condition in [".", "?", "..."]):
            # ! Chỉnh sửa điều kiện ngắt câu

            if condition in [".", "?", "..."] and len(text) > 150:
                try:
                    # !Code khác chỉ 1?
                    # !Code khác chỉ 1?
                    # !Code khác chỉ 1?
                    # !Code khác chỉ 1?
                    # !Code khác chỉ 1?
                    # !Code khác chỉ 1?
                    # !Code khác chỉ 1?
                    # !Code khác chỉ 1?
                    subs_new.append(
                        pysrt.SubRipItem(
                            index=index,
                            start=subs_old[flag].start.to_time(),
                            end=subs_old[i].end.to_time(),
                            text=text.strip()
                        )
                    )
                except:
                    subs_new.append(
                        pysrt.SubRipItem(
                            index=index,
                            start=subs_old[flag].start.to_time(),
                            end=subs_old[flag].start.to_time(),
                            text=text.strip()
                        )
                    )

                flag = i + 1
                index += 1
                text = ""

            subs_new.save(new_file, encoding='utf-8')
