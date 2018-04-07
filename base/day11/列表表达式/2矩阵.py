'''
矩阵
1  2   3    4   5   6  7
8  9  10   11  12  13 14
'''
mylist=[]
for  i  in range(8):
     mylist.append([i*10+j   for  j  in range(10)])

for  l  in mylist:#矩阵，列表的每一个元素都是列表
    print(type(l))
    print(l)


