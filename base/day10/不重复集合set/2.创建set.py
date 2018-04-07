set1=set()
set2=set([1,2,3,4,5])
set3=set((1,2,3,4,5,1))
set4=set({1:2,3:4})
set5=set("abcdefga")
set6={1,2,3,4,5,6}  #set默认标准
set7=set6 #直接赋值，默认浅复制，
set8=set(set7) #根据set初始化

print(type(set1),set1) #空集合
print(type(set2),set2)  #list全部转换过来
print(type(set3),set3) #tuple全部转化过来
print(type(set4),set4) #字典仅仅存储key
print(type(set5),set5) #字符串存储每一个字符
print(type(set6),set6) #tuple全部转化过来
print(type(set7),set7) #字典仅仅存储key
print(type(set8),set8) #字符串存储每一个字符