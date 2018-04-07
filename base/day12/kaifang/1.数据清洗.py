import codecs
filepath=r"Z:\F\第一阶段视频\20170424\vedio\大数据相关数据\kaifangX.txt"
file=codecs.open(filepath,"rb","gbk","ignore")#按照指定编码
mylist=file.readlines()#返回一个list,读取到内存
file.close()

savegoodfilepath=r"C:\Users\Tsinghua-yincheng\Desktop\day12down\kaifangGood18.txt"
savebadfilepath=r"C:\Users\Tsinghua-yincheng\Desktop\day12down\kaifangbad.txt"
filegood=open(savegoodfilepath,"wb")
filebad=open(savebadfilepath,"wb")
for  line  in  mylist:
    linelist=line.split(",")
    if  len(linelist)>=2:
        if len(linelist[1])==18:
            #good
            filegood.write(line.encode("utf-8"))
            pass
        else:
            #bad
            filebad.write(line.encode("utf-8"))
            pass
    else:
        #bad
        filebad.write(line.encode("utf-8"))
        pass


filebad.close()
filegood.close()

