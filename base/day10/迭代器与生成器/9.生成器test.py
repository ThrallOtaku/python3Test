'''
def  go():
    print(1)
    yield  10
    print(11)
    yield 101
    print(12)
    yield 102

print(type(go)) #函数
print(type(go())) #生成器
X=go()
print(next(X))
print(next(X))
print(next(X))
'''

def  go():
    for i  in range(1,101,2):
        yield  i

print(type(go))
print(type(go()))
X=go()
print(next(X))
print(next(X))
print(next(X))
