import win32con
import win32api
import time
win32api.SetCursorPos([30,30]) #设置鼠标位置
time.sleep(0.1)
win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0,0,0)
'''
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
time.sleep(0.1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)

常量，剩余四个参数设定为0，
MOUSEEVENTF_LEFTDOWN 模拟鼠标左键按下
MOUSEEVENTF_LEFTUP 模拟鼠标左键抬起
MOUSEEVENTF_RIGHTDOWN 模拟鼠标右键按下
MOUSEEVENTF_RIGHTUP 模拟鼠标右键按下
MOUSEEVENTF_MIDDLEDOWN 模拟鼠标中键按下
MOUSEEVENTF_MIDDLEUP 模拟鼠标中键按下

'''
