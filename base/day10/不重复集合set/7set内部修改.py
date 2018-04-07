myset={1,2,3,4,5,6}
for i  in myset: #遍历集合，修改副本，无法修改原本
    i=i+1
    print(i)
print(myset)

#print(myset[0])#set没有索引
for  idx,iddata in enumerate(myset): #enumerate生成索引
    iddata+=1
    print(idx,iddata) #idx下表，iddata元素
print(myset)
#myset操作单个元素，修改需要转化为list