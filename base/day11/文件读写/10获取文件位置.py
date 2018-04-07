file=open(r"C:\Users\Tsinghua-yincheng\Desktop\hcq.txt","r")
print(file.tell()) #0
mystr=file.readline() #读取英文，遇到换行符
print(mystr)
print(len(mystr))#15
print(file.tell()) #15+'\n'  获取文件指针的位置，
file.close()