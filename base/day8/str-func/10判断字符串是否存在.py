mystr="孙播	陈慧	申凌瑞	 陈慧  李佳奇	吴东	牛兴杰	"
print(mystr.index("陈慧")) #index查找字符串是否存在，存在返回第一个下标，不存在，异常错误
print(mystr.rindex("陈慧")) #rindex查找，返回最后一个的下表
print(mystr.index("陈慧",7,10)) #第二个开始，第三个结束