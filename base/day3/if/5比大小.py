a,b,c=eval(input("a,b,c"))
if a>b:
    pass   # a  (a,b)
    if a>c:
        print("max",a)
        if b>c:
            print(b,c)
        else:
            print(c,b)
    else:
        print("max", c)
        if b>a:
            print(b,a)
        else:
            print(a,b)
else:
    pass    # b  (a,b)
    if b > c:
        print("max", b)
        if c > a:
            print(c, a)
        else:
            print(a, c)
    else:
        print("max", c)
        if b > a:
            print(b, a)
        else:
            print(a, b)