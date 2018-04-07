from win32com.client import constants
import os
import win32com.client
import pythoncom

speaker = win32com.client.Dispatch("SAPI.SPVOICE")


class SpeechRecognition:
    def __init__(self, wordsToAdd):
        self.speaker = win32com.client.Dispatch("SAPI.SpVoice")
        self.listener = win32com.client.Dispatch("SAPI.SpSharedRecognizer")
        self.context = self.listener.CreateRecoContext()
        self.grammar = self.context.CreateGrammar()
        self.grammar.DictationSetState(0)
        self.wordsRule = self.grammar.Rules.Add("wordsRule", constants.SRATopLevel + constants.SRADynamic, 0)
        self.wordsRule.Clear()
        [self.wordsRule.InitialState.AddWordTransition(None, word) for word in wordsToAdd]
        self.grammar.Rules.Commit()
        self.grammar.CmdSetRuleState("wordsRule", 1)
        self.grammar.Rules.Commit()
        self.eventHandler = ContextEvents(self.context)
        self.say("Started successfully")
    def say(self, phrase):
        self.speaker.Speak(phrase)
class ContextEvents(win32com.client.getevents("SAPI.SpSharedRecoContext")):
    def OnRecognition(self, StreamNumber, StreamPosition, RecognitionType, Result):
        newResult = win32com.client.Dispatch(Result)
        print("小伙子你在说 ", newResult.PhraseInfo.GetText())
        speechstr=newResult.PhraseInfo.GetText()
        if  speechstr=="赵大海":
            speaker.Speak("赵大海，你愿意抱着凤姐，面朝大海，春暖花开")
        elif  speechstr=="你好":
            speaker.Speak("好你妹")
        elif  speechstr=="国庆快乐":
            speaker.Speak("国庆快乐，快乐的要死")
        elif  speechstr=="新年快乐":
            speaker.Speak("新年happy")
        elif  speechstr=="赵琳":
            speaker.Speak("来自唐山的大美女，")
        elif  speechstr=="王涛":
            speaker.Speak("你的波涛涌用")
        elif  speechstr=="彭彪":
            speaker.Speak("彭彪你身上很多彪子吗")
        elif  speechstr=="马剑":
            speaker.Speak("马剑为什么你不学刀枪非要学剑")
        elif  speechstr=="孟勋":
            speaker.Speak("孟勋，你要建立不世的功勋么")
        elif  speechstr=="徐振涛":
            speaker.Speak("涛哥，你的波涛汹涌")
        elif  speechstr=="陈小平":
            speaker.Speak("小平，你好，为啥你不姓徐")
        else:
            pass

if __name__ == '__main__':

    speaker.Speak("语音识别开启")
    wordsToAdd = ["赵大海",
                  "你好",
                  "国庆快乐",
                  "新年快乐",
                  "王涛",
                  "赵琳",
                  "彭彪",
                  "马剑",
                  "孟勋"  ,
                   "徐振涛",
                  "陈小平"]
    speechReco = SpeechRecognition(wordsToAdd)
    while True:
        pythoncom.PumpWaitingMessages()