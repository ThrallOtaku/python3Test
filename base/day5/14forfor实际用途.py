import turtle

for  i  in  range(0,300,100):

    for j  in  range(0,400,100):
        turtle.goto(j,i)
        turtle.pendown()#跳过第一次
        turtle.write(str(i)+","+str(j))
    turtle.penup()

turtle.done()