# 100-10000
#  4=2+2  6=3+3  8=3+5

#x +y=10000
#x 1-9999
#if  is(X)and is(1000-x)
def isit(num):
    if num<0:
        return False
    elif num==0 or num==1:
        return False
    elif num==2 or num==3:
        return True
    else:
        isdata=True  #假定是质数，判断10
        for  i  in range(2,num):  #判断2-9，
            if num%i==0:#有一个整除判定不是，跳出循环
                isdata=False
                break
        return  isdata


#print(isit(17))

#x+y=100
def  getall(num):
    for  i  in range(1,num):
        if isit(i) and isit(num-i):
            print(i,num-i)

for  i  in range(100,120):
    getall(i)

