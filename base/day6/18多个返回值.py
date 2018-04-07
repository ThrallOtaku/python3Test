
def  getdata1():
    return 1

def  getdata2():
    return 1,2

def  getdata3():
    return 1,2,3


num1= getdata1()
print(num1)
num2,num3=getdata2()  #num2=1  num3=2
print(num2,num3)


def  getdata3():
    return 1,2,3
a,b,c=getdata3()
print(a,b,c)