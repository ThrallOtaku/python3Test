def add(num1=1,num2=2):
    return num1+num2
print(add())   #，没有默认参数的情况下，调用函数无比正确传递参数
               #有默认值，可以不传
print(add(3)) #传递参数，从左往右填充
print(add(3,9)) #传递参数覆盖默认参数