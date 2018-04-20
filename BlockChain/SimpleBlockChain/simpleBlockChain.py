import hashlib
import datetime


class DaDaBlockCoin:
    def __init__(self,
                 index,  # 索引
                 timeStamp,  # 时间戳
                 data,  # 交易数据
                 lastHash):
        self.index = index
        self.timeStamp = timeStamp
        self.data = data
        self.lastHash = lastHash
        self.selfHash = self.hash_DaDaBlockCoin()

    # 产生加密串,产生一个串就是产生一个币
    def hash_DaDaBlockCoin(self):
        # sha = hashlib.sha256()
        # sha = hashlib.sha512()
        sha = hashlib.md5()
        datastr = str(self.index) + str(self.timeStamp) + str(self.data) + str(self.lastHash)
        sha.update(datastr.encode("utf-8"))
        return sha.hexdigest()


def create_first_DadaBlock():  # 创造一个创世区块
    return DaDaBlockCoin(0, datetime.datetime.now(), "TAOTAO COIN", "00001")


def create_money_DadaBlock(last_block):  # 区块链的其他块  last_block 上一个区块
    this_index = last_block.index + 1
    this_timestamp = datetime.datetime.now()
    this_data="taotao coin"+str(this_index) #模拟交易数据
    last_hash =last_block.selfHash
    return DaDaBlockCoin(this_index,
                         this_timestamp,
                         this_data,
                         last_hash)

DaDaBlockCoins=[create_first_DadaBlock()] #区块链链表
nums=100
head_block=DaDaBlockCoins[0]
print("创世区块taotao币来啦")
print(head_block.index, head_block.data, head_block.timeStamp, head_block.lastHash, head_block.selfHash)

for i in range(nums):
    dadaBlock_add=create_money_DadaBlock(head_block)  #根据第一个区块创造下一个区块
    DaDaBlockCoins.append(dadaBlock_add)     #区块加入链
    head_block=dadaBlock_add
    print(dadaBlock_add.index,dadaBlock_add.data,dadaBlock_add.timeStamp,dadaBlock_add.lastHash,dadaBlock_add.selfHash)

