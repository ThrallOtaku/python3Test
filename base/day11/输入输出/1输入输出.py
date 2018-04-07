mystr="hello python\n"  #repr可以观察转义字符
print(str(mystr)) #人可以可以看懂
print(repr(mystr))#计算机看懂

data=3/7
print(str(data)) #一般的数据，两者一样，
print(repr(data))

print(repr(str))
print(repr(int))
print(repr("1")) #repr可以处理任何类型，标识类型
print(repr(1))
print(str("1")) #str不可以区别类型，统一转换字符串
print(str(1))

print("1","2")
print("1".ljust(10),"2")#rjust(10)调整字符串的宽度  rjust,ljust对齐

for  x in range(100):
    print(repr(x).rjust(10),repr(x*x).rjust(10),repr(x*x*x).rjust(10))
