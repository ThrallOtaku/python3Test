mydata=(1,2,3,4,5,6)
mydata2=5,6,7,8
print(mydata[-1])
print(mydata[:]) #全部
print(mydata[3:]) #3-最后
print(mydata[:-2]) #默认从左到-2,不包含-2
print(mydata+mydata2) #拼接
print(mydata2*4) #复制4次
#del mydata2 #内存清除，无法再调用
print(mydata2)
print(len(mydata2))#长度
print(5  in  mydata2) #存在
print(10 not in mydata2) #判断不存在
for data in mydata2: #副本
    print(data)