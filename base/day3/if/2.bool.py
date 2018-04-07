import os

cmd = input("cmd")
isrun = (cmd == "notepad")  # cmd=="notepad" 逻辑表达式，返回真，返回假
print(isrun)
if isrun:
    os.system("notepad")
