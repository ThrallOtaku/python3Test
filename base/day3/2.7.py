import  turtle

min=input("请输入分数")
min=eval(min)
#print("天",min//60//24)
#print("年",min//60//24//365)
days=min//(60*24)
year=days//365
days=days%365
min=min%(60*24)
print(year,"年",days,"天",min,"分钟")
turstr=str(year)+"年"+str(days)+"天"+str(min)+"分数"
turtle.write(turstr)
turtle.done()