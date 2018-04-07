import  win32com.client#系统客户端包
speaker=win32com.client.Dispatch("SAPI.SPVOICE")#系统接口
for  i  in  range(10):
    speaker.Speak("我是凤姐，我爱死了申凌睿")