'''
mylistnew=mylist
mylist[3]=10000
print(id(mylistnew),id(mylist))
print(mylist)
print(mylistnew) #浅复制
'''
mylist=[1,2,3,4,5]
mylistnew=mylist.copy()
print(id(mylist),id(mylistnew))
mylist[3]=10000

print(mylist)
print(mylistnew)
