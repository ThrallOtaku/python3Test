# 区块

import datetime  # 时间
import hashlib  # 加密解密
#import Message  # 导入交易信息模块


class MoneyBlock:
    def __init__(self, *args):  # 区块链多个交易记录，可变参数
        self.moneymessage = []  # 交易记录集合
        self.timestamp = None  # 确认时间
        self.pre_hash = None  # 前面的区块的地址
        self.hash = None  # 当前哈希
        if args:  # 参数不空
            for arg in args:
                self.add_message(arg)  # 不断加入多个消息记录

    def add_message(self, message):  # 追加交易记录
        # 第一个消息
        # 2,3,4,5,6--多个消息
        if len(self.moneymessage) > 0:
            message.link(self.moneymessage[-1])  # 链接交易记录，第一个不链接
        self.moneymessage.append(message)  # 加入交易记录列表
        message.seal()  # 密封
        message.validate()  # 校验

    def _hash_block(self):  # 哈希保存最后一个加入的记录
        sha = hashlib.sha512()
        sha.update((str(self.pre_hash) +
                    str(self.timestamp) +
                    str(self.moneymessage[-1].hash)).encode("utf-8"))  # 转化2进制
        return sha.hexdigest()

    def link(self, moneyblock):
        self.pre_hash = moneyblock.hash  # 链接上一个区块

    def seal(self):  # 数据密封,防止修改
        self.timestamp = datetime.datetime.now()  # 获取当前时间
        self.hash = self._hash_block()  # 保存最后一次交易记录的哈希

    def validate(self):  # 区块的数据校验
        length = 0
        for i, msg in enumerate(self.moneymessage):
            if msg.validate() == "数据正常":  # 每一个交易记录校验一下,
                length += 1
            if i > 0 and msg.prev_hash != self.moneymessage[i - 1].hash:
                print("无效block,交易记录修改在 第{}条记录".format(i))
                return
        if len(self.moneymessage) != length:
            print("NO")
        else:
            print("OK")

    def __repr__(self):  # 字符串显示区块
        return "MoneyBlock: hash:{} prehash:{},len:{},time:{}".format(
            self.hash, self.pre_hash, len(self.moneymessage), self.timestamp
        )


'''
m1=Message.MoneyMessage("yincheng pay  baidu 100a")
m2=Message.MoneyMessage("yincheng pay  baidu 1000b")
m3=Message.MoneyMessage("yincheng pay  baidu 10000c")
yin=MoneyBlock(m1,m2,m3) #一次加入三条记录
yin.seal()#数据密封


m4=Message.MoneyMessage("yincheng pay  baidu 100000d")
#yin.moneymessage.append(m4) #插入
yin.moneymessage[-2]=m4 #修改

yin.validate() #校验
print(yin)
'''
