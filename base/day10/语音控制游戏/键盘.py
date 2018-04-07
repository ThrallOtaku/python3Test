import win32con
import win32api
import time
win32api.keybd_event(91,0,0,0) #键盘按下
time.sleep(0.1)
win32api.keybd_event(91,0,win32con.KEYEVENTF_KEYUP,0)#键盘松开



'''
这个函数模拟了键盘行动
参数表
参数 类型及说明
bVk Byte，欲模拟的虚拟键码
bScan Byte，键的OEM扫描码
dwFlags Long，零；或设为下述两个标志之一
KEYEVENTF_EXTENDEDKEY 指出是一个扩展键，而且在前面冠以0xE0代码
KEYEVENTF_KEYUP 模拟松开一个键
dwExtraInfo Long，通常不用的一个值。api函数GetMessageExtraInfo可取得这个值。允许使用的值取决于特定的驱动程序
注解
这个函数支持屏幕捕获（截图）。在win95和nt4.0下这个函数的行为不同

'''