print(b'\xce\xd2\xb5\xc4\xe0\xb8')
print(b'\xce\xd2\xb5\xc4\xe0\xb8'.decode("gbk"))
print(b'\xce\xd2\xb5\xc4\xe0\xb8'.decode("gbk"))
#decode,将二进制转化为字符串，制定编码格式
print("你好中国".encode("utf-8"))
print(b'\xe4\xbd\xa0\xe5\xa5\xbd\xe4\xb8\xad\xe5\x9b\xbd'.decode("utf-8"))
#decode,encode ，编码一致，乱码或者代码出错
print(type("hello".encode("utf-8"))) #字符串编码为二进制编码
print(type(b'\xce\xd2\xb5\xc4\xe0\xb8'.decode("utf-8"))) #二进制转化为字符串