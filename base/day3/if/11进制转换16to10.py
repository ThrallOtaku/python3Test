num=input("input  16  hex")
if  num=="a"  or  num=="A":
    print(10)
elif  num=="b"  or  num=="B":
    print(11)
elif  num=="c"  or  num=="C":
    print(12)
elif  num=="d"  or  num=="D":
    print(13)
elif  num=="e"  or  num=="E":
    print(14)
elif  num=="f"  or  num=="F":
    print(15)
elif  eval(num)>=0  or  eval(num)<=9:
    print(eval(num))
else:
    print("error")

