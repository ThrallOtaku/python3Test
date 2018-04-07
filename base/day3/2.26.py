import  turtle

R=input("请输入圆形半径")
R=eval(R)
turtle.circle(R)
turtle.penup()
turtle.goto(0,R)
turtle.pendown()
turtle.write("0,"+str(R))


turtle.done()