
#def 定义函数 ，getmax函数名称,num1,num2参数，输入的数据
def  getmax(num1,num2):  #num1,num2形式参数
    #5-8 line   函数体
    if num1<num2:
        return num2  #函数的输出
    else:
        return num1

num=getmax(100,199)  #num被赋值为返回值，实际参数，
print(num)