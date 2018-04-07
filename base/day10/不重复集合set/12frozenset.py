fz=frozenset([1,2,3,4,5])
print(fz)
print(type(fz))
#fz.remove(4)
for i  in fz: #遍历集合
    print(i)

#print(myset[0])#set没有索引
for  idx,iddata in enumerate(fz): #enumerate生成索引
    print(idx,iddata) #idx下表，iddata元素
