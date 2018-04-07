import  win32com.client#系统客户端包
speaker=win32com.client.Dispatch("SAPI.SPVOICE")#系统接口
num=0
while num<7:
    print("while",num)
    speaker.Speak("吴东的女神有"+str(num)+"个备胎")
    num += 1
else:
    print("else",num)
    speaker.Speak("吴东的女神有" + str(num) + "个备胎，够了，忙不过来")
