

print(int(True))  #1 ,true
print(int(False))  #0,false
print(bool(4))  #true
print(bool(1))   #true
print(bool(0))  #0为false ,非0true
print(bool(-1))
print("str",bool(""))  #字符串为空  flase
print("str",bool("1"))  #字符串为非空，true

if None:  #if语句自动转化bool类型   bool(none)=false
    print("hello python")
