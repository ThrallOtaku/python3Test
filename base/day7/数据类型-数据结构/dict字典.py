mydict={"abcdefg":10, "123456":2,"xyzhjk":3,"123456":10}
print(type(mydict))#dict是set的强化版 左边是key,不允许重复，右边value重复
print(mydict)
print(mydict["abcdefg"]) #根据key取出value
print(mydict.values()) #值，
for  key  in  mydict: #循环字典
    print(key,mydict[key])