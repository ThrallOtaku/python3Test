year=eval(input("year"))
month=eval(input("month"))
if  month==1:
    print(31)
elif  month==2:
    if  year%4==0  and    year%100!=0 : #1996,2012
        print(29)
    elif  year%4==0  and  year%400==0  and  year%100==0:
        print(29)
    else:
        print(28)
elif  month==3:
    print(31)
elif  month==4:
    print(30)
elif  month==5:
    print(31)
elif  month==6:
    print(30)
elif  month==7:
    print(31)
elif  month==8:
    print(31)
elif  month==9:
    print(30)
elif  month==10:
    print(31)
elif  month==11:
    print(30)
elif  month==12:
    print(31)
else :
    print("脑子进水")