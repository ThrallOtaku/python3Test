filepath=r"Z:\F\第一阶段视频\20170424\vedio\大数据相关数据\QQ.txt"
file= open(filepath,"rb")
for  line in  file:#file每一行数据集合，
    print(line)
file.close()