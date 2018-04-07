import codecs
'''
第一步
import codecs
filepath=r"Z:\F\第一阶段视频\20170424\vedio\大数据相关数据\dangdangwang.txt"

file=codecs.open(filepath,"rb",encoding="gbk",errors="ignore")
for  line  in  file:#硬盘模式
    print(line)
'''
def  loaddata():
    filepath = r"Z:\F\第一阶段视频\20170424\vedio\大数据相关数据\csdn.txt"
    file = codecs.open(filepath, "rb", encoding="gbk", errors="ignore")
    global datalist #引用全局
    datalist=file.readlines() #读取文件到list
    file.close()
def  search(namestr):
    savefilepath="Z:\\F\\第一阶段视频\\20170424\\vedio\\大数据相关数据\\data\\"+namestr+".txt"
    savefile=open(savefilepath,"wb")
    numbers=0
    for  line  in datalist:
        if line.find(namestr)!=-1:
            print(line,end="") #显示数据
            numbers +=1
            savefile.write(line.encode("utf-8"))#写入
    savefile.write(("数量"+str(numbers)).encode("utf-8"))
    savefile.close()


#list=["山东"，“广东”]
datalist=[]
print("load  file start")
loaddata()
print("load  file end")
while True:
    searchname=input("要查询的数据")
    search(searchname)