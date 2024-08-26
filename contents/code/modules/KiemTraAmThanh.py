# pip install pyttsx3
# https://www.youtube.com/watch?v=qVMHoCtjLag
import pyttsx3


def KiemTraAmThanh():
    text = "Kiểm tra âm thanh tiếng Việt"
    engine = pyttsx3.init()
    engine.setProperty('voice', r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An")
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    print(text)


if __name__ == "__main__":
    KiemTraAmThanh()
