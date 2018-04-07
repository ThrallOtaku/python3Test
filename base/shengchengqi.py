# coding:utf-8
# 生成器语法

mylist = [12, 32, 23, 423, 323, 23]
myiter = iter(mylist)

print(next(myiter))
print(next(myiter))
print(next(myiter))

for item in mylist:
    print(item)


# 生成器
def go():
    print("11")
    yield 1
    print("22")
    yield 2
    print("33")
    yield 3
    print("44")
    yield 4
    print("55")
    yield 5
    print("66")
    yield 6
    print("77")
    yield 7
    print("88")


T = go()
print(type(T))
print("return=", next(T))
print("return=", next(T))
print("return=", next(T))
