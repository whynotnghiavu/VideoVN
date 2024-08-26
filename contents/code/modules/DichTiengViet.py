import os
from time import sleep


import pyperclip
import pyautogui


from modules.CONST import CONST


def DichTiengViet():
    text_to_copy = os.path.join(os.getcwd(), CONST.MERGED_FILE)
    pyperclip.copy(text_to_copy)

    file_tieng_viet = os.path.join(os.getcwd(), CONST.MERGED_VIETNAM_FILE)
    if os.path.exists(file_tieng_viet):
        os.remove(file_tieng_viet)

    # NOTE: Chỉ vị trí SubtitleEdit
    # ! Phiên bản 3.6.13
    # ! Link: https://github.com/SubtitleEdit/subtitleedit/releases/tag/3.6.13
    # pyautogui.hotkey('win', '1')
    pyautogui.hotkey('win', '2')
    # pyautogui.hotkey('win', '3')
    # pyautogui.hotkey('win', '4')
    # ! Chỉ vị trí phần mềm SubtitleEdit

    sleep(5)
    pyautogui.typewrite(['enter'])
    pyautogui.typewrite(['enter'])
    pyautogui.typewrite(['enter'])
    pyautogui.typewrite(['enter'])
    pyautogui.typewrite(['enter'])
    sleep(5)
    pyautogui.hotkey('ctrl', 'o')
    sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    sleep(1)
    pyautogui.typewrite(['enter'])
    pyautogui.typewrite(['enter'])
    pyautogui.typewrite(['enter'])
    pyautogui.typewrite(['enter'])
    pyautogui.typewrite(['enter'])
    sleep(5)
    pyautogui.hotkey('ctrl', 'shift', 'g')
    sleep(1)
    pyautogui.typewrite(['tab', 'tab', 'tab', 'tab'])
    sleep(1)
    pyautogui.typewrite(['enter'])
    exit()
