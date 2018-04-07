import time  #时间
timedata=time.time()
timedata=int(timedata)#取整数,多少秒
print(timedata%60)#小时
print(timedata/3600)#小时
print(timedata/3600/24)#天
print(timedata/3600/24/365)#年