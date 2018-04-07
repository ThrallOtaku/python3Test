import win32gui
import win32con
import time
import math
wangwang=win32gui.FindWindow("StandardFrame","阿里旺旺")


while True:
    SE = 0.0
    while  SE-3.1415926535*2  <0.000001:
        SE+=0.1
        newx = int(400+400*math.cos(SE))
        newy = int(400+400*math.sin(SE))
        win32gui.SetWindowPos(wangwang,  # 操作记事本
                          win32con.HWND_TOPMOST,  # 最上方
                          newx,  # 位置x
                          newy,  # 位置y
                          300,  # 长度
                          300,  # 宽度
                          win32con.SWP_SHOWWINDOW)
    print(SE)
