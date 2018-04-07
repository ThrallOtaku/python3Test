import win32com.client  # 系统客户端包

speaker = win32com.client.Dispatch("SAPI.SPVOICE")  # 系统接口

# while,规则，与if一样，会对表达式进行转换
# True,继续循环，fallse退出循环
# True  1,2,-1," ", True 1.234
# false   0,"",None ,False
while None:
    speaker.Speak("我是凤姐，我爱死了申凌睿")

'''
speaker.Speak("我是凤姐，我爱死了申凌睿")
speaker.Speak("我是凤姐，我爱死了申凌睿")
speaker.Speak("我是凤姐，我爱死了申凌睿")
speaker.Speak("我是凤姐，我爱死了申凌睿")
speaker.Speak("我是凤姐，我爱死了申凌睿")
speaker.Speak("我是凤姐，我爱死了申凌睿")
'''
