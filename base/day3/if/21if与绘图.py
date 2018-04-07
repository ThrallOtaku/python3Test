import turtle
R=100
x1,y1=eval(input("圆心"))
turtle.write(str(x1)+","+str(y1))
turtle.penup()
turtle.goto(x1,y1-R) #移动圆心
turtle.pendown()
turtle.circle(R)

x2,y2=eval(input("pos"))
turtle.penup()
turtle.goto(x2,y2) #移动到输入的位置
turtle.pendown()
turtle.dot(10,"red")#绘制点，颜色红色
turtle.goto(x1,y1)#连线
length= ((x1-x2)**2+(y1-y2)**2)**0.5
print(length)
if  length==R:
    print("圆上")
elif  length <R:
    print("圆内")
else:
    print("园外")



turtle.done()