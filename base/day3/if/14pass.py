#pass
#pass  空语句，什么都不执行

import  os
cmd=input("输入指令")
if  cmd=="关机":
    os.system("shutdown -s -t  200")
else:
    print("我们不适合")
    pass #占坑
print("game over")

