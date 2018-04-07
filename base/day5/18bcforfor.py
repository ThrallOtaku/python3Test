'''
for  i  in  range(8):
    for j  in  range(10):
        print(j,end=" ")
        if j==5:
            break  #跳出j这个循环
    if i==5:
        break  #跳出i这个循环
    print("")
'''

for  i  in  range(8):
    if i == 5:#淘汰某一行
        continue
    for j  in  range(10):
        if j==5:  #淘汰某一列
            continue
        print(j, end=" ")

    print("")

