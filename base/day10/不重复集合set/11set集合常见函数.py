myset1={1,2,3,4}
myset2={1,2,3,4,5}
print(len(myset1))#求长度
print(myset1.issuperset(myset2))#myset1是否包含myset2
print(myset1.issubset(myset2)) #myset1是否被myset2包含
print(myset2.issuperset(myset1))#myset1是否包含myset2
print(myset2.issubset(myset1))