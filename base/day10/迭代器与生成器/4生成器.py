mylist=(x  for x  in range(100000000)) #生成器,[]返回list,（）返回生成器
print(type(mylist)) #class 'generator'
print(next(mylist))
print(next(mylist))
print(next(mylist))
print(next(mylist))
print(next(mylist))
print(next(mylist))
print(next(mylist))