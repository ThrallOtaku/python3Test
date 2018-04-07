#mydict={}
#print(type(mydict))
        #key不可以重复，10属于次数
mydict={"abcdefg":10,"123456":36,"123456":136}
print(mydict)
print(mydict["abcdefg"]) #根据key取出value

#循环字典两种风格
print("---------------------------------")
for  key  in  mydict.items():#每一个key-value映射
    print(key)
print("---------------------------------")
for key in mydict:  #遍历每一个key
    print(key,mydict[key])
print("---------------------------------")
for key in mydict.keys():  #遍历每一个key
    print(key,mydict[key])
print("---------------------------------")
for  value in mydict.values():
    print(value)