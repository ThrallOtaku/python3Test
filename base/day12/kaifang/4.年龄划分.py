import codecs
filepath=r"C:\Users\Tsinghua-yincheng\Desktop\day12down\kaifangGood18.txt"
file=codecs.open(filepath,"rb","utf-8","ignore")#按照指定编码
mylist=file.readlines()#返回一个list,读取到内存
file.close()
print("load")


#C:\Users\Tsinghua-yincheng\Desktop\day12down\age\1993.txt
area=[x  for x in range(1900,2018)]
areafilelist=[]
length=len(area)#长度
for  data in area:
    kffilepath="C:\\Users\\Tsinghua-yincheng\\Desktop\\day12down\\age\\"+str(data)+".txt"
    kffile=open(  kffilepath,"wb")
    areafilelist.append(kffile)

for  line  in  mylist:
    linelist=line.split(",") #字符串切割
    chstr=linelist[1][6:10] #取出4个字符
    for  i  in range(length):
        if  str(area[i])==chstr:
            areafilelist[i].write(line.encode("utf-8"))
            break




print("over")
for  kffile in areafilelist:#关闭文件
    kffile.close()