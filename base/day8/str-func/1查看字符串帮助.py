#print(dir(""))
mylist=dir("") #dir返回是一个列表list
print(type(""))
print(mylist)  #[]包含了所有的函数，属性
for  i  in  mylist: #遍历打印
    print(i)
    print(help("str."+i))
    #print(help("\"\"."+i))
for i  in range(len(mylist)): #下标打印
    print(mylist[i])
    print(help("str."+mylist[i]))
