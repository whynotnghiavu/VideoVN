from tkinter import filedialog


from modules.MyLog import MyLog


def ChonThuMuc():
    folder = filedialog.askdirectory(title="Chọn thư mục")

    if folder:
        MyLog.info(f"Đã chọn: {folder}")
        return folder
    MyLog.error("ChonThuMuc: Chưa chọn thư mục")
