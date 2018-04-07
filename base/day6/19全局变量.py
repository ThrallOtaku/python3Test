

num=10 #全局变量

def go():
    num=3 #局部变量，函数内部
    print(num,id(num))

go()
print(num,id(num))
