num1=3
num2=3
print(id(num1),id(num2))
if  num1 is  num2:
    print("同一个地址")


#num1=4
if  num1 is  num2:  #is
    print("同一个地址")
else:
    print("不是同一个地址")


if  num1 is not  num2:  #is   not  不是同一个地址
    print("不是同一个地址")
else:
    print("是同一个地址")
