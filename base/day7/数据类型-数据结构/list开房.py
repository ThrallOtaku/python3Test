
import codecs  #编码
file=codecs.open("Z:\\F\\第一阶段视频\\20170531\\day6\\kaifangX.txt","rb","gbk","ignore")
listname=file.readlines() #多行,返回list
print(type(listname)) #打印类型
print(len(listname))#求行数
while True:
    name=input("输入要查询的负心人")
    i=0
    for  line  in listname: #挨个搜索
        if  line.find(name)!=-1:
            i+=1
            print(line)
    print("一共"+str(i)+"条")





