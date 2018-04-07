import random
startnum=random.randint(1,10000)#随机数
num=eval(input("请输入一个数字"))
while  num!=startnum:   #while()条件，跳出循环的表达式取反
    if num>startnum:
        print("big")
    else:
        print("small")
    num=eval(input("再次输入"))
else:
    print("right")
    print(num,startnum)