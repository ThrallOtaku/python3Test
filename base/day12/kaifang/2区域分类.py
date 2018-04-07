import codecs
filepath=r"C:\Users\Tsinghua-yincheng\Desktop\day12down\kaifangGood18.txt"
file=codecs.open(filepath,"rb","utf-8","ignore")#按照指定编码
mylist=file.readlines()#返回一个list,读取到内存
file.close()
print("load")
#C:\Users\Tsinghua-yincheng\Desktop\day12down\地区\华北.txt
area=[[1,"华北"],[ 2,"东北" ],[3,"华东"],[4,"中南"],[5,"西南"],[6,"西北"]]
areafilelist=[]
length=len(area)#长度
for  data in area:
    kffilepath="C:\\Users\\Tsinghua-yincheng\\Desktop\\day12down\\地区\\"+data[1]+".txt"
    kffile=open(  kffilepath,"wb")
    areafilelist.append(kffile)

for  line  in  mylist:
    linelist=line.split(",") #字符串切割
    chstr=linelist[1][0] #取出一个字符
    for  i  in range(length):
        if  str(area[i][0])==chstr:
            areafilelist[i].write(line.encode("utf-8"))
            break


print("over")

for  kffile in areafilelist:#关闭文件
    kffile.close()
