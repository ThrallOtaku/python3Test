#区块链

import datetime #时间
import hashlib  #加密解密
#import Block  #导入区块
class  DaDaMoneyBlockChain: #区块链表类
    def __init__(self):
        self.chain=[] #保存多个区块
    def add_block(self, block):
        if len(self.chain)>0:
            block.pre_hash=self.chain[-1].hash #区块链链接
        block.seal() #密封
        block.validate()#校验
        self.chain.append(block) #加入区块
    def validate(self):#校验
        for i,block  in enumerate(self.chain): #校验
            block.validate()


    def __repr__(self):
        return "达达币区块数量 {}".format( len(self.chain))