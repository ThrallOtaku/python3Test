

#测试一个函数，执行时间
#函数当作一个参数，设计模块测试函数的时间

import time

def  getcosttime(go):
    starttime = time.time()
    go()
    endtime = time.time()
    print(endtime - starttime)

def go():
    lastnum=0
    for i  in range(1,100000000):
        lastnum+=i
    print(lastnum)

def come():
    lastnum=0.0
    for i in range(1, 100000000):
        lastnum += i
    print(lastnum)

getcosttime(go)
getcosttime(come)





