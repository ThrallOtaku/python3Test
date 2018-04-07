# 区块链存储的交易信息

import datetime  # 时间
import hashlib  # 加密解密


class MoneyMessage:
    def __init__(self, data):  # 交易数据
        self.hash = None  # 自身-包含了地址的哈希与数据的哈希，
        self.prev_hash = None  # 上一个信息的哈希
        self.timestamp = datetime.datetime.now()  # 时间
        self.size = len(data.encode("utf-8"))  # 数据长度
        self.data = data  # 数据初始化
        self.payload_hash = self._payload_hash()  # 当前的哈希

    def _payload_hash(self):  # 对于数据，时间进行取得哈希
        sha = hashlib.sha256()
        sha.update((str(self.timestamp) + str(self.data)).encode("utf-8"))  # 转化2进制
        return sha.hexdigest()  # 哈希值

    def _hash_message(self):  # 数据哈希，上一个地址哈希，避免纂改
        sha = hashlib.sha256()
        sha.update((str(self.payload_hash) + str(self.prev_hash)).encode("utf-8"))  # 转化2进制
        return sha.hexdigest()  # 哈希值

    def seal(self):  # 数据密封,防止修改
        self.hash = self._hash_message()  # 实现密封

    def link(self, message):  # 链接多个交易消息
        self.prev_hash = message.hash  # 链接上一个

    def validate(self):  # 检查消息的有效性
        if self.payload_hash != self._payload_hash():  # 校验哈希值
            return "数据与日期已经被修改"
        if self.hash != self._hash_message():  # 校验哈希的数据与哈希链的正常
            return "哈希链被修改,不正常"
        return "数据正常"

    def __repr__(self):  # 类型打印字符串
        return "MoneyMessag:,hash{},prev_hash:{},-----data:{}". \
            format(self.hash, self.prev_hash, self.data)


'''

m1=MoneyMessage("yincheng pay  baidu 100")
m2=MoneyMessage("yincheng pay  baidu 1000")
m3=MoneyMessage("yincheng pay  baidu 10000")
m1.seal()#密封
m2.link(m1)
m2.seal()
m3.link(m2)
m3.seal()


#m2.data="你妹" #纂改数据
m2.prev_hash="----------------" #修改哈希链

print(m1)
print(m2)
print(m3)

print(m1.validate())
print(m2.validate())
print(m3.validate())
'''
