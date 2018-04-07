for  i  in range(100,120):
    for  j  in range(1,i):# j  .100-j
        isdataj = True
        if j < 0:
            isdataj = False
        elif j == 0 or j == 1:
            isdataj= False
        elif j == 2 or j== 3:
            isdataj= True
        else:
             # 假定是质数，判断10
            for i in range(2, j):  # 判断2-9，
                if j % i == 0:  # 有一个整除判定不是，跳出循环
                    isdataj = False
                    break

        isdata100j = True
        if 100-j < 0:
            isdata100j = False
        elif 100-j == 0 or 100-j == 1:
            isdata100j = False
        elif 100-j == 2 or 100-j == 3:
            isdata100j = True
        else:
            # 假定是质数，判断10
            for i in range(2, 100-j):  # 判断2-9，
                if (100-j) % i == 0:  # 有一个整除判定不是，跳出循环
                    isdata100j = False
                    break

        if  isdataj and  isdata100j:
            print(j,100-j)




#7=2+2+3
#9=3+3+3
