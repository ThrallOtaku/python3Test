QQlist=[5,6,7,8,9,10,11,"小垃圾"]

filepath=r"C:\Users\Tsinghua-yincheng\Desktop\day12down\QQgood.txt"
file=open(filepath,"rb")
mylist=file.readlines()
file.close()

# "C:\Users\Tsinghua-yincheng\Desktop\day12down\QQdata\5位QQ.txt

filelist=[]
for  i  in QQlist:
    QQfilepath="C:\\Users\\Tsinghua-yincheng\\Desktop\\day12down\\QQdata\\"+str(i)+"位QQ.txt"
    QQfile = open(QQfilepath, "wb")
    filelist.append(QQfile)


for  line  in  mylist:
    bakline=line
    line=line.decode("utf-8")
    linelist=line.split("----")
    length=len(linelist[0] )#取账号的长度
    if length==5:
        filelist[0].write(bakline)
    elif length==6:
        filelist[1].write(bakline)
    elif length == 7:
        filelist[2].write(bakline)
    elif length == 8:
        filelist[3].write(bakline)
    elif length == 9:
        filelist[4].write(bakline)
    elif length == 10:
        filelist[5].write(bakline)
    elif length == 11:
        filelist[6].write(bakline)
    else:
        filelist[7].write(bakline)

for  QQfile  in filelist:
    QQfile.close()