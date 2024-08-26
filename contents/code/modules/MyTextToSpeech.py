import os
import pyttsx3


from modules.TinhGiay import TinhGiay
from modules.LayDoDaiFileWAV import LayDoDaiFileWAV
from modules.MyNoSound import MyNoSound


def MyTextToSpeech(start, end, text, file):
    start = TinhGiay(start)
    end = TinhGiay(end)
    # Tỉ số
    _end = 0.3 * start + 0.7 * end

    # Tạo lần 1
    engine = pyttsx3.init()
    engine.setProperty('rate', 100)
    engine.setProperty('voice', r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An")
    engine.save_to_file(text, file)
    engine.runAndWait()

    # Đo thời gian 1
    time = LayDoDaiFileWAV(file)

    # Tính toán tỉ lệ  điều chỉnh tốc độ
    rate_adjustment = time / (_end - start)

    # Tạo lần 2
    rate = int(engine.getProperty('rate') * rate_adjustment)
    engine.setProperty('rate', rate)
    engine.save_to_file(text, file)
    engine.runAndWait()

    # Đo thời gian 2
    time = LayDoDaiFileWAV(file)
    # Vì dùng int nên thời gian vẫn sai số
    # => Thêm file âm thanh

    time = (end - start) - time
    directory, filename = os.path.split(file)
    new_filename = filename.replace(".wav", "_.wav")
    file_no_sound = os.path.join(directory, new_filename)
    MyNoSound(time, file_no_sound)
