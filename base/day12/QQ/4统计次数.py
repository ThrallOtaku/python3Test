filepath=r"C:\Users\Tsinghua-yincheng\Desktop\day12down\QQgoodpasssort.txt"
file=open(filepath,"rb")
mylist=file.readlines() #读取所有
length=len(mylist)
file.close()

print("read ")
savefilepath=r"C:\Users\Tsinghua-yincheng\Desktop\day12down\QQgoodpasssorttimes.txt"
savefile=open(savefilepath,"wb")

i=0
while i<length-1:
    times=1
    passwordstr=mylist[i]
    while i+1<=length-1  and mylist[i].decode("utf-8")==mylist[i+1].decode("utf-8"):
        times+=1
        i+=1
    #print(times, passwordstr)
    savefile.write((str(times)+" "+passwordstr.decode("utf-8")).encode("utf-8"))


    i+=1


savefile.close()
print("save ")
