mylist=[1,2,3,4,5,6]
#mylist是一个多个变量组成的集合，每个变量可以存储不同的地址不同类型的变量的地址

print(type(mylist))
print(id(mylist))
print(mylist)

mylist=[1,1.2,"abc",True]

print(id(mylist[0]))
print(id(mylist))

mylist[0]=100

print(id(mylist[0]))
print(id(mylist))


print(type(mylist))
print(mylist)