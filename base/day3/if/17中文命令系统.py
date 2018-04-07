import os
cmdstr=input("输入指令")
if  cmdstr=="记事本":
    os.system("notepad")
elif  cmdstr=="计算器":
    os.system("calc")
elif cmdstr=="进程":
    os.system("tasklist")
elif cmdstr=="IP地址":
    os.system("ipconfig")
elif cmdstr=="重启":
    os.system("shutdown -r -t 200")
elif cmdstr=="关机":
    os.system("shutdown -s -t 200")
else:
    print("其他指令，还没翻译")

