def  add(num1,num2):
    return num1+num2

def  sub(num1,num2):
    return num1-num2

go1=add(1,2) #返回值
go2=add #函数类型的地址
print(type(go1),type(go2))


'''
go=add  #go的本质是一个地址，修改地址实现不同的行为，函数类型
print(id(go),id(add))
print(type(go),type(add))
print(go(5,3))
go=sub
print(id(go),id(sub))
print(type(go),type(sub))
print(go(5,3))

'''
