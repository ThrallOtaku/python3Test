import turtle
'''
turtle.screensize(3024,2768)#屏幕
turtle.write("hello天朝",font=("华文琥珀",20,"normal"))#设定字体大小
turtle.showturtle()#显示
turtle.circle(100,steps=2000)
turtle.done()
'''

turtle.screensize(3024,2768)#屏幕
turtle.write("hello天朝",font=("华文琥珀",20,"normal"))#设定字体大小
turtle.showturtle()#显示


turtle.begin_fill()  #开始填充
turtle.circle(100,steps=5)
turtle.color("blue")  #变色
turtle.end_fill()#结束填充

turtle.reset()#重置

turtle.pensize(20)#画笔变粗
turtle.begin_fill()  #开始填充
turtle.circle(100,steps=4)
turtle.color("yellow")  #变色
turtle.end_fill()#结束填充
turtle.hideturtle()#隐藏箭头


turtle.done()
