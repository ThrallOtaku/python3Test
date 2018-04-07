'''


import pickle
mylist=[[1,2,3,4,5,6,7],["abc","xyz","hello"]]
file=open(r"C:\Users\Tsinghua-yincheng\Desktop\list.bin","wb")
pickle.dump(mylist,file) #保存list到文件
file.close()


import pickle
mylist=[]
file=open(r"C:\Users\Tsinghua-yincheng\Desktop\list.bin","rb")
mylist=pickle.load(file) #读取文件到list
print(mylist)


'''