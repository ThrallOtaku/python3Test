'''
name1
name2
name3


----
----
----
'''

mylist =[1,2,3,4,5,6,7]
print(len(mylist)) #列表，容纳多个数据
mylist.append(8)  #增加数据
print(len(mylist)) #列表，容纳多个数据
for  data  in mylist:  #循环遍历列表
    print("------",data)
for  i  in range(len(mylist)): #下标循环
    print("------", mylist[i])


print(mylist)
print(mylist[1:7])#索引截取,与字符串，正索引，负索引
print(mylist[4:-1])
print(mylist[:]) #全部,不包含最后一个索引
print(mylist[:4]) #默认不输入开头
print(mylist[4:]) #默认不输入结尾
print(mylist*2)#乘法复制两次
print(mylist+mylist[4:6])# +列表相叠加，  
