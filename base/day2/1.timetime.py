import  time  #时间
mytimes=time.time()
print(mytimes)
#mytimes=100000
print("自从1970现在过去了",int(mytimes),"秒")
seconds= int(mytimes)%60  #秒
hours=int(mytimes)//3600  #过去了多少小时
mins=  int(mytimes)%3600     #(int(mytimes)-int(mytimes)//3600*3600)#剩余的秒数
mins= (mins-seconds) //60
days=hours//24
hours=hours%24

months=days//30
days=days%30

year=months//12
months=months%12

print("自从1970现在过去了",
      year,"年",
        months,"月",
      days,"天",
      hours,"小时",
      mins,"分",
      seconds,"秒")
#100%9=100-100//9*9=1
#3600+1550秒 =5150秒
#1小时   50秒
#5150-50-3600  /60=

#3959
#3959%60=59
#3959//3600=1
#(3959-1*3600-59)  /60

