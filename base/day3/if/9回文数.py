
num=eval(input("输入三位整数")) #100,999
if (num//100 >0  and  num//100<10):
    print("三位数")
    b=num//100  #百位
    c=num%10   #个位
    if b==c:
        print("是回文数")
    else:
        print("不是回文数")
else:
    print("不是三位数")