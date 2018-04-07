import  turtle
import math

#turtle.penup()
turtle.goto(200,100) #200,100
#turtle.pendown()
turtle.goto(200,-100)
turtle.goto(-200,-100)
turtle.goto(-200,100)
turtle.goto(200,100)



x,y=eval(input("input  pos  x,y"))
turtle.penup()
turtle.goto(x,y)
turtle.pendown()
turtle.dot(26,"red")
x=abs(x)
y=abs(y)

if x<200 and y<100:
    print("矩形内部")
elif x==200  and  y<=100:
    print("矩形高度边上")
elif y==100 and  x<=200:
    print("矩形宽度边上")
else:
    print("矩形外部")








turtle.done()