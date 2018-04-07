mydict={"abcdefg":10,"123456":136}
print(mydict)

#print("123456"  in  mydict)#true
#print("123456" not  in  mydict) #false
#"123456":16
#"123456789":236
password="a123456"
times=16
if  password  in mydict: #存在
    mydict[password]+=times #叠加
else:
    mydict[password]=times #不存在新建

print(mydict)





