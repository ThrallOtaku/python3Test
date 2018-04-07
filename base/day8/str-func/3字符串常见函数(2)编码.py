#bytes
#10
#_  _  _  _   _   _   _  _  byte 2^8=256     2^7=128,其中一个用于表示正负

b=bytes(1) #byte转化为二进制编码，1个字节
print(b) #\x16进制   2^4=16  8位  1个字节B
#1GB =1024MB =1024*1024KB =1024*1024*1024B*8位

'''
#utf-8
a=bytes("你abc","utf-8") #不同的编码大小不一样内容不一样
print(a)
a=bytes("你好中国abc","gbk")
print(a)
'''

#utf-8两个字符表示汉字，一个字符汉字结束，3个字符
print(bytes("我","utf-8"))
print(bytes("我的","utf-8"))
print(bytes("我的喔","utf-8"))

#GBK两个字符表示汉字，没有结束
print(bytes("我","gbk"))
print(bytes("我的","gbk"))
print(bytes("我的喔","gbk"))







