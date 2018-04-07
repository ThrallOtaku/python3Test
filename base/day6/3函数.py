import  random
#没有参数，没有返回值
def  go():
    print("hello word  hello  python")

#有参数，没有返回值
def goprint (num):
    print("python",num)

#没有参数，有返回值
def getdata():
    return random.randint(0,100) #返回一个数据

#有输入，输出
def  add(num1,num2):
    return num1+num2


num=add(1,2)  #
print(num)



'''

for i  in range(10):
    goprint(i)#()调用函数
    num=getdata()
    print(num)
'''



