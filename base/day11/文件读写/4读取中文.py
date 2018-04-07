file=open(r"C:\Users\Tsinghua-yincheng\Desktop\day11\newchina.txt","rb")
mystr=file.read() #读取二进制，
print(type(mystr))
print(mystr.decode("utf-8")) #二进制文本
file.close()