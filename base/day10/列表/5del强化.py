'''
num=10
del  num #内存回收，变量不存在
print(num)
'''
mylist=[1,2,3,4,5,6]
for  i  in range(len(mylist)): #修改列表必须索引
    if  mylist[i]==3:  #修改列表 ，mylist[i]是原本
        del mylist[i]#删除一个元素，索引会变小，继续循环越界
        break #终止循环
print(mylist)

for   data in mylist: #修改失败,读取不修改用这个
    if data==2: #data是副本
        del data #对于删除列表无效
print(mylist)
