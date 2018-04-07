
filepath=r"C:\Users\Tsinghua-yincheng\Desktop\day12down\QQgood.txt"
file=open(filepath,"rb")

savefilepath=r"C:\Users\Tsinghua-yincheng\Desktop\day12down\QQgoodpass.txt"
savefile=open(savefilepath,"wb")
print("start")
for  line in  file: #遍历数据的每一行
    #print(line)#字符串
    linstr=line.decode("utf-8","ignore") #解码
    mylist=linstr.split("----")
    savefile.write((mylist[1]).encode("utf-8"))
print("end")
savefile.close()
file.close()