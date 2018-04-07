
'''
def  createlist():
    mylist=[x for x  in  range(10000)]
    return  mylist
print(createlist())
'''

def createlist():
    for i  in range(100):
        print(i)
        yield  i

X=createlist()
print(type(X))
next(X)
next(X)
next(X)
next(X)


