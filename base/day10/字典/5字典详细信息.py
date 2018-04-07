mydict1={"abcdefg":10,"123456":136}
mydict2={"asdsa":100}
mydict1.update(mydict2)#字典拼接
mydict1.setdefault("123456",None) #不存在，添加默认，存在没动静
print(mydict1.items())
print(mydict1.keys())
print(mydict1.values())