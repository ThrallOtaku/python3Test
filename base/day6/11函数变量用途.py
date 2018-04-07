
def  add(num1,num2):
    return num1+num2

def  sub(num1,num2):
    return num1-num2

def  getmax(num1,num2):  #业务的逻辑
   return num1 if num1>num2 else num2

def  Test(go,num1,num2): #接口，不变的，业务核心代码
    return go(num1,num2)

print(Test(add,1,2))
print(Test(sub,1,2))
print(Test(getmax,1,2))