set1={1,2,3,4}
set2={1,2,7,8}
for  data in set1:
    print("------",data)
print(type(set1))
print(set1-set2) #set1有set2没有的  差集，
print(set2-set1)#set2有set1没有的
print(set1 | set2) #并集，
print(set1  & set2) #交集
print(set1 ^ set2) #set1,set2并集-交集 ，set1,set各自独有在一起
