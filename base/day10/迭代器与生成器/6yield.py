
#函数一次性执行完
'''
def go():
    print(1)
    print(2)
    print(3)

go()
'''
def goX():
    print(1)
    print(2)
    print(3)
def go():
    print(1)
    yield 10 #执行print1,返回10，next
    print(2)
    yield 20#执行print2,返回20，next
    print(3)
    yield 30#执行print3,返回30，next


#print(type(goX))
#print(type(goX()))
#print(type(go))
#print(type(go())) #加上yield的函数返回值，是一个生成器
X=go()
print(type(X))
print(next(X))
print(next(X))
print(next(X))



