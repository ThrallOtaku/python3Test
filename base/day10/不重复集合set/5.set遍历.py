myset={1,2,3,4,5,6}
for i  in myset: #遍历集合
    print(i)

#print(myset[0])#set没有索引
for  idx,iddata in enumerate(myset): #enumerate生成索引
    print(idx,iddata) #idx下表，iddata元素