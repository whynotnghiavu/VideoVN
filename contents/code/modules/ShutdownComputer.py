import os


from modules.MyLog import MyLog


def ShutdownComputer():
    MyLog.error(f"ShutdownComputer: Tự động tắt máy sau 60 giây")
    os.system('shutdown /s /t 60')
