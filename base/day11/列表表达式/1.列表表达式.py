
'''一般形式
mylist=[x+1  for x in range(1,100,2)]
print(mylist)


一般形式+判断
mylist=[x+1  for x in range(1,100,2)  if x<50]
print(mylist)

#生成列表嵌套列表
'''
'''
生成列表嵌套列表
mylist=[[x,x+1,x*x] for  x in range(10)  if x>5]
print(mylist)
'''

'''
mylist=[x+y  for  x  in range(10)  for y in range(10)] #嵌套循环
print(mylist)
'''

'''
mylist=[[x,y]  for  x  in range(10)  for y in range(10)] #嵌套循环
print(mylist)
'''

'''
mylist=[[x,y]  for  x  in range(10) if  x<5 for y in range(10)  if y<5] #嵌套循环
print(mylist)

mylist=[[x,y]  for  x  in [1,2,3,4]  for y in [6,7,8]  ] #嵌套循环
print(mylist)
'''

mylist=[ str([x,y])  for  x  in [1,2,3,4]  for y in [6,7,8]  ] #嵌套循环
print(mylist)