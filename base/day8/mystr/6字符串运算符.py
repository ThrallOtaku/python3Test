mystr1="calc"
mystr2="notepad"
print(mystr1+mystr2)#字符串加法
print(mystr1*4) #4个字符串串联,字符串只有整数乘法
print(mystr2[4])  #截取一个字符，编号为4,实际第五个
print(mystr2[2:3]) #字符串
print('c'  in 'calc')  #false
print('X'  not in  'calc') #true  判断一个字符在或者不在
print('calc'  in   'mycalc')  #判断一个字符串是否被最后一个字符串包含
print('calc' not in   'mycalc')

print("12345\n12345")  #\r\n  \n都起到换行作用，
print(format("1","10s"),"12") #对齐作用
print(format("12","10s"),"123")
print(format("123","10s"),"1234")
print(format("1234","10s"),"12345")


