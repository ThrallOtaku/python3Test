
def  show(num1,num2,num3):
    print(num1,num2,num3)
show(1,2,3) #位置参数，从左往右
show(num3=10,num2=20,num1=30) #名称参数，可以乱序，指定名称
print("hello",end="") #名称参数