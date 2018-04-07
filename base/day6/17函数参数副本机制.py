
#数字,字符串当作参数传递给函数，原来的数字，字符串不会改变。

'''
def changenum(num):
    num=100
    print("change",num)
    print("change",id(num))


num=10
changenum(num)
print(num)
print(id(num))
'''


def  changedata(str):
    str="calc"
    print("change",str,id(str))


mystr="12345"
changedata(mystr)
print(mystr,id(mystr))
