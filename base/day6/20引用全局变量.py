num=10 #全局变量，
def go():
    #global num  #加上以后， num=3 解释为引用外部的全局变量重复赋值，用的同一个
    num=3 #没有global解释为新建一个变量
    print(num,id(num))
go()
print(num,id(num))