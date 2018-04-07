import random
data=random.randint(1,13)
change=random.randint(1,4)
if  change==1:
    print("红桃")
elif  change==2:
    print("黑桃")
elif change==3:
    print("方块")
else:
    print("梅花")


if  data==1:
    print("A")
elif  data==2:
    print("2")
elif data==3:
    print("3")
elif data==4:
    print("4")
elif data==5:
    print("5")
elif data==6:
    print("6")
elif data==7:
    print("7")
elif data==8:
    print("8")
elif data==9:
    print("9")
elif data==10:
    print("10")
elif data==11:
    print("J")
elif data==12:
    print("Q")
elif data==13:
    print("K")
else:
    print("error")