import time
file=open(r"C:\Users\Tsinghua-yincheng\Desktop\day11\hcq2.txt","w")
mystr="hello python"
file.write(mystr) #mystr自动编码,ASCII,
file.flush()#刷新，实时写入
time.sleep(30)
file.close()