import win32process #进程模块
import win32con#系统定义
import win32api#调用系统模块
import ctypes#C语言类型
import win32gui #界面
import time

#一个常量，标识最高权限打开一个进程
PROCESS_ALL_ACCESS=(0x000F0000|0x00100000|0xFFF) # |位运算，0x十六进制
window=win32gui.FindWindow("MainWindow","植物大战僵尸中文版")#查找窗体
hid,pid=win32process.GetWindowThreadProcessId(window) #根据窗体抓取进程编号
phand=win32api.OpenProcess(PROCESS_ALL_ACCESS,False,pid)#用最高权限打开进程编号
date=ctypes.c_long()#C语言的整数类型，读取数据
#加载内核模块
mydll=ctypes.windll.LoadLibrary("C:\\Windows\\System32\\kernel32.dll")

while  True:
    mydll.ReadProcessMemory(int(phand), 244866760, ctypes.byref(date), 4, None)  # 读取内存
    print(date.value)
    if  date.value <300:
        newdata = ctypes.c_long(500)  # 设定修改数据为2048
        mydll.WriteProcessMemory(int(phand), 244866760, ctypes.byref(newdata), 4, None)
    time.sleep(1)





#读取内存，  int(phand)打开的进程编号  244866760,内存地址， 写入结果ctypes.byref(date)
#整数4个字节


