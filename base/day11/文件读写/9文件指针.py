file=open(r"C:\Users\Tsinghua-yincheng\Desktop\hcq.txt","r")

#file.seek(16,0) #0文件调到从开头开始第十五个字符，一个换行符
mystr=file.readline() #读取英文，遇到换行符
print(mystr)
#file.seek(0,0) #跳转文件指针， 开头
file.seek(200,0) #io.UnsupportedOperation: can't do nonzero end-relative seeks
mystr=file.readline() #读取英文，遇到换行符
print(mystr)
#print(len(mystr)) 求长度
file.close()