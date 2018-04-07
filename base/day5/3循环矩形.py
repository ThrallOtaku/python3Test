import turtle


#设定循环次数
#实现一个操作，常量
#常量修改变量

length=50 #初始
step=50  #每次加50
num=0   #循环10次，
while num<10:
    print(num)
    num+=1  #循环次数

    turtle.penup()
    turtle.goto(length*2, length)
    turtle.pendown()
    turtle.goto(length*2, -1 * length)
    turtle.goto(-1 * length*2, -1 * length)
    turtle.goto(-1 * length*2, length)
    turtle.goto(length*2, length)
    length+=step

else:
    print("out",num)
