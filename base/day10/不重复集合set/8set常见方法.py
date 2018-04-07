myset={1,2,3,4,5,6}
#myset.remove(14)删除，不存在报错
#myset.discard(14)#删除，不存在不报错
print(myset)
print(myset.pop()) #弹出1，
print(myset.pop()) #弹出1，
print(myset)#2，3，4，5，6
myset.clear() #清空
myset.copy()#深复制