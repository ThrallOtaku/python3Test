score=input("高考分数")
score=eval(score)

if  score>750  and score<0:
    print("error")
elif score>300  and  score<=400:
    print("大专")
elif score>400  and  score<=500:
    print("三本")
elif score> 500 and  score<=550:
    print("二本")
elif score >550 and  score<=580:
    print("1本")
elif score>580  and  score<=600:
    print("211")
elif  score>600  and  score<=700:  #不顺序，误差，
    print("985")
elif  score>700:
    print("清北")
else:
    print("山东蓝翔")


'''
if  score>750  and score<0:
    print("error")
elif  score>700:
    print("清北")
elif score>600: #隐含条件score <=700
    print("985")
elif score>580:
    print("211")
elif score >550:
    print("1本")
elif score> 500:
    print("二本")
elif score>400:
    print("三本")
elif score>300:
    print("大专")
else:
    print("山东蓝翔")

'''











'''
if  score>750:
    print("输入错误")
else:
    if score<0:
        print("输入错误")
    else:
        if score>=700 and  score<=750:
            print("清北")
        else:
            if score>=600 and  score<700:
                print("985")
            else:
                if  score >=580  and  score<600:
                    print("211")
                else:
                    if score>=550  and score<580:
                        print("一本")
                    else:
                        if score >=500 and score <550:
                            print("二本")
                        else:
                            if score<500 and  score >=450:
                                print("三本")
                            else:
                                if score >=300 and score<450:
                                    print("大专")
                                else:
                                    print("学历到此为止。蓝翔欢迎你")

'''

