'''
myset={1,2,3,4,5,6}
myset.add(8) #插入数据
myset.add(1)#去重
print(myset)



myset=set("abcdefg")
myset.update("abcdxyz")#update打碎字符串，插入
print(myset)

'''

myset={1,2,3,4,5,6}
myset.update([1,2,8,9]) #单个整数不可以,list,tuple,字符串
print(myset)


