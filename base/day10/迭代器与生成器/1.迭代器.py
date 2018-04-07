mylist={1:2,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1}
'''
it=iter(mylist) #it迭代器，it索引为0，list,tuple，集合,字典
print(next(it))
print(next(it))
print(next(it))
'''
it=iter(mylist) #类型自动记录索引
for   i  in it:
    print(i,mylist[i])

