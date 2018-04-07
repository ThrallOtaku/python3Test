import time
import os

'''
#每几秒操作一次
while True:
    time.sleep(5)
    os.system("notepad")
'''

num=0
while True:
    time.sleep(1)
    print("第"+str(num)+"秒")
    num+=1


    if num==10:
        os.system("start notepad")
    elif num==20:
        os.system("taskkill /f /im notepad.exe")
    else:
        pass

