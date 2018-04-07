name=input("please input  name")
age= eval(input("please input age"))
tall=eval(input("please  input  tall"))
star=input("please input star")
pos=input("please input pos")
# 陈梦奇，北京,年龄，身高，星座，
if pos!="北京":
    print("地址不符合，淘汰")
else:
    if age <=40:
        print("年龄不和，淘汰")
    else:
        if tall<=170:
            print("身高不行，淘汰")
        else:
            if star!="天蝎座":
                print("星座不符合，淘汰")
            else:
                print("符合要求",name)
#层次对齐。程序错误

