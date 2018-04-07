

       #生成一个列表，x从0-10循环，每个元素的x*x
mylist=[x*x  for x  in range(10)]
print(mylist)
mylist=[x*x  for x  in range(10) if  x>5] #if  x>5筛选
print(mylist)
print(type(mylist))