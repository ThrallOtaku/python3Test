def go():
    print(1)
    yield 10 #执行print1,返回10，next
    print(2)
    yield 20#执行print2,返回20，next
    print(3)
    yield 30#执行print3,返回30，next
#go()  不带yield
go()
