import random

#num1=random.randint(0,13)
#num2=random.randint(0,13) #生成0-100的随机数,包含0，包含100
num1=random.randrange(0,10)#0-9不包含10
num2=random.randrange(0,10)
print("小宝宝 %d +  %d "%(num1,num2))
num=input("baby  input")
num=eval(num)
if  num==num1+num2:
    print("小宝宝好聪明")

