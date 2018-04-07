import os
'''
cmd=input("cmd")
while(cmd!="退出"):
    if cmd=="记事本":
        os.system("notepad")
    elif cmd=="进程":
        os.system("tasklist")
    else:
        os.system("echo  other")
    cmd=input("cmd")
'''
while True:
    cmd = input("cmd")
    if cmd=="记事本":
        os.system("notepad")
    elif cmd=="进程":
        os.system("tasklist")
    elif cmd=="推出":
        break
    else:
        os.system("echo  other")


