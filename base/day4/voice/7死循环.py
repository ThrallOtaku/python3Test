import  os

while True:
    cmd=input("指令")
    if  cmd=="记事本":
        os.system("notepad")
    elif  cmd=="计算器":
        os.system("calc")
    else:
        print("其他指令有待输入")