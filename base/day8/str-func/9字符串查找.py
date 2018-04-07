mystr="孙播	陈慧	申凌瑞	 陈慧  李佳奇	吴东	牛兴杰	"
#print(mystr.find("陈慧")) #find返回第一个  ,从头部
print(mystr.rfind("陈慧")) #rfind返回最后一个
print(mystr.rfind("陈慧",6))
print(mystr.rfind("陈慧",6,11))

'''
Python rfind() 返回字符串最后一次出现的位置，如果没有匹配项则返回-1。
语法
rfind()方法语法：
str.rfind(str, beg=0 end=len(string))
参数
• str -- 查找的字符串
• beg -- 开始查找的位置，默认为0
end -- 结束查找位置，默认为字符串的长度。
'''


'''
#print(mystr.find("陈慧1	"))#找到返回第一个匹配的下标，找不到返回-1
print(mystr.find("陈慧",4)) #第一个参数要查找字符串，第二个起始，第三个结束
print(mystr.find("李佳奇",4,9))#
find()方法语法：
str.find(str, beg=0, end=len(string))
参数
• str -- 指定检索的字符串
• beg -- 开始索引，默认为0。
• end -- 结束索引，默认为字符串的长度。
返回值
如果包含子字符串返回开始的索引值，否则返回-1。

'''