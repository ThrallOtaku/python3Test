mycmd="notepad"
print(mycmd[3])
print(mycmd[1:3])#字符串截取，1-3不包含3
print(mycmd[3:-1])
print(mycmd[-3:-1])#正索引从0开始，负索引-1开始
print(mycmd[:]) #全部
print(mycmd[:5]) #从一个到索引为5，不包含索引为5
print(mycmd[3:])#包含最后一个，
print(mycmd*3) #字符串拷贝三次