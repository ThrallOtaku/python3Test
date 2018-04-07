mylist=[   [   [1,2],[3,4]  ],
           [   [5,6],[7,8]  ],
           [    [9,10],[11,12]  ]]

#print(mylist[0]) #列表第一个元素
#print(mylist[0][0]) #列表第一个元素的第一个元素
#print(mylist[0][0][0]) #列表第一个元素的第一个元素的第一个元素

for  i  in range(len(mylist)):
    #print(mylist[i])
    for j in range(len(mylist[i])):
        #print(mylist[i][j])
        for k  in range(len(mylist[i][j])):
            print(mylist[i][j][k])mylist1=[1,2,3,4,5,6]


'''
for  data1  in mylist:
    #print(data1)
    for data2 in data1:
        #print(data2)
        for data3 in data2:
            print(data3)

'''

