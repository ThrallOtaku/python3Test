import  win32com.client#系统客户端包
speaker=win32com.client.Dispatch("SAPI.SPVOICE")#系统接口


i=0
while i<5:
    print(i)
    speaker.Speak("我是凤姐，我爱死了申凌睿,这是第"+str(i+1)+"次")
    i+=1
else:
    speaker.Speak("凤姐说，小申，老娘喊的口凑干了。你还不从了老娘")
    print("go",i)