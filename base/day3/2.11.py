lastmoney=input("请输入最终的RMB")
monthrate=input("请输入月利率")
years=input("输入年限")
lastmoney=eval(lastmoney)#转化数值
monthrate=eval(monthrate)
years=eval(years)
beginmoney=   lastmoney/(1+monthrate)**(years*12)
print(beginmoney)
