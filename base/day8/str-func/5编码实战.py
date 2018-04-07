
mystr="hello python"
mystrc="hello 中国"
print(mystr.encode("utf-8"))
print(mystrc.encode("utf-8"))#encode返回二进制，用于写入文本
print(b'hello python'.decode("utf-8"))   #将二进制转化为文本
print(b'hello \xe4\xb8\xad\xe5\x9b\xbd'.decode("utf-8"))
print(b'hello python'.decode("gbk"))

#英文的东西，任何编码无所谓， GBK，UTF-8对于英文编码
#汉字注意编码的格式，不同的编码结果不一样，同样的二进制，换一种编码一般解析出错
