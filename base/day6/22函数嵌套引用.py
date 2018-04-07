'''
#函数可以包含函数
#内层函数testin num覆盖外层  test  num，不同的变量，地址不一样

def  Test():
    num=10
    def Testin():
        num=100
        print("test in",num,id(num))

    Testin()
    print("test",num,id(num))

Test()


'''
#函数可以包含函数
#内层函数testin num覆盖外层  test  num，不同的变量，地址不一样


def  Test():
    num=10 #函数内部都是局部变量
    def Testin():
        nonlocal num #内层testin，直接操作外层Test，
        num=1000 #没有noloacal解释为新建一个变量，否则解释为重新赋值
        print("test in",num,id(num))

    Testin()
    print("test",num,id(num))

Test()
