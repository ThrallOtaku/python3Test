#utf-8包含ACSII
#ASCII格式，没有中文，可以编译
#UTF-8格式编译中文
#UTF-8空间占用较大，
#python3默认字符串都是utf-8     unicode  (utf-8 ,unicode-8  unicode16)

print(u"hello world") #utf-8  python3默认就是u,可以加也可以不加

#r节约时间，不用输入转义字符,特殊处理,不能处理"
print(r"C:\Users\Tsinghua-yincheng\Desktop\tools")
print(r"C:\Users\Tsinghua-yincheng\Desktop\tools")
print("C:\\Users\\Tsinghua-yincheng\\Desktop\\tools")
print(r"""C:\Users\Tsinghua-yincheng\Desktop\tools""")