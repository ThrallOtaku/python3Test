import win32con
import win32api
import time
#第一个参数，键盘对应数字，查表
#第二个，第四个没用
#第三个参数，0代表按下，win32con.KEYEVENTF_KEYUP松开
while True:
    win32api.keybd_event(91, 0, 0, 0)  # 键盘按下 91win
    time.sleep(0.1)
    win32api.keybd_event(77, 0, 0, 0)  # 键盘按下  68  D
    time.sleep(0.1)
    win32api.keybd_event(77, 0, win32con.KEYEVENTF_KEYUP, 0)  # 键盘松开  D 68
    win32api.keybd_event(91, 0, win32con.KEYEVENTF_KEYUP, 0)  # 键盘松开