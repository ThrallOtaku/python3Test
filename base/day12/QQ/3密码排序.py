filepath=r"C:\Users\Tsinghua-yincheng\Desktop\day12down\QQgoodpass.txt"
file=open(filepath,"rb")
mylist=file.readlines() #读取所有
mylist.sort()#排序
file.close()

print("sort ")
savefilepath=r"C:\Users\Tsinghua-yincheng\Desktop\day12down\QQgoodpasssort.txt"
savefile=open(savefilepath,"wb")
for  line in  mylist:
    savefile.write(line)
savefile.close()
print("save ")
