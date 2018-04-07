mystr="hello python2 hello python3"
print(mystr.capitalize())#第一个字符转化为大写
print(mystr)
#mystr.title()


mystr="8888"
for  i  in range(6,40,2):
    for j  in range((40-i)//2,0,-1):
        print(" ",end="")
    print(mystr.center(i,'*'))


'''
center(width, fillchar)
返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
'''

mystr="hello python2 hello python3"
print(mystr.count('python')) #判断字符串出现的次数
print(mystr.count('python',10)) #判断字符串出现的次数,从10个到最后
print(mystr.count('python',10,15)) #判断字符串出现的次数,从10个到15个