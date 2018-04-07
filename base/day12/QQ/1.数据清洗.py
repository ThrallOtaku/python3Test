import codecs
filepath=r"Z:\F\第一阶段视频\20170424\vedio\大数据相关数据\1E~001.txt"
file=codecs.open(filepath,"rb","gbk","ignore")#按照指定编码
mylist=file.readlines()#返回一个list,读取到内存
savegoodfilepath=r"C:\Users\Tsinghua-yincheng\Desktop\day12down\QQGood.txt"
savebadfilepath=r"C:\Users\Tsinghua-yincheng\Desktop\day12down\QQbad.txt"
filegood=open(savegoodfilepath,"wb")
filebad=open(savebadfilepath,"wb")
for  line  in  mylist:

    if  len(line)>35  or  len(line)<15:
        filebad.write(line.encode("utf-8"))
    else:
        QQlist = line.split('----')
        if  len(QQlist)==2:
            filegood.write(line.encode("utf-8"))
        else:
            filebad.write(line.encode("utf-8"))

filebad.close()
filegood.close()


