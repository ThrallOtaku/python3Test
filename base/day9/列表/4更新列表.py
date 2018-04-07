mylist=[1,2,3,4,5,6]
for  i  in range(len(mylist)): #修改列表必须索引
    if  mylist[i]==3:  #修改列表 ，mylist[i]是原本
        mylist[i]=9999


for   data in mylist: #修改失败,读取不修改用这个
    if data==2: #data是副本
        data=2222
        print(data)

mylist.append(1234) #增加
print(mylist)