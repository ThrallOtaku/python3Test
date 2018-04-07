import codecs
filepath=r"C:\Users\Tsinghua-yincheng\Desktop\day12down\kaifangGood18.txt"
file=codecs.open(filepath,"rb","utf-8","ignore")#按照指定编码
mylist=file.readlines()#返回一个list,读取到内存
file.close()
print("load")


#C:\Users\Tsinghua-yincheng\Desktop\day12down\age\1993.txt
area=["01","02","03","04","05","06","07","08","09","10","11","12",
      "13","14","15","16","17","18","19","20","21",
      "22","23","24","25","26","27","28","29","30","31"]
areafilelist=[]
length=len(area)#长度
for  data in area:
    kffilepath="C:\\Users\\Tsinghua-yincheng\\Desktop\\day12down\\day\\"+str(data)+"日.txt"
    kffile=open(  kffilepath,"wb")
    areafilelist.append(kffile)

for  line  in  mylist:
    linelist=line.split(",") #字符串切割
    chstr=linelist[1][12:14] #取出4个字符
    for  i  in range(length):
        if  str(area[i])==chstr:
            areafilelist[i].write(line.encode("utf-8"))
            break




print("over")
for  kffile in areafilelist:#关闭文件
    kffile.close()