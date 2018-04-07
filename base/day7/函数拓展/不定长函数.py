#print(1)
#print(1,2)
#print(1,2,3)
#print(1,2,3,4)

def add(num1,num2):
    return num1+num2


def newadd(*num): #*num代表一个序列，装多个
    lastnum=0
    for  data in  num:#data  轮询每一个插入的数据
        lastnum+=data
    print(lastnum)
newadd(1)
newadd(1,2)
newadd(1,2,3)
newadd(1,2,3,4)
