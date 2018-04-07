import  time
'''
num=2.0
while  num!=0:  #浮点数误差,5.45
    num-=0.1
    print(num)
    time.sleep(0.5)
'''
#num-0 <=0.000001  -0.0000000000000000000000000638378239159465


num=2.0
while  num-0>0.000000001:  #浮点数误差,5.45,金融
    num-=0.1
    print(num)
    time.sleep(0.5)