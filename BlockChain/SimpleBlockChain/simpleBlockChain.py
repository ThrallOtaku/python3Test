import hashlib
import datetime


class TTBlockCoin:
    def __init__(self,
                 index,  # 索引
                 timeStamp,  # 时间戳
                 data,  # 交易数据
                 lastHash):  # 上一个块的hash值
        self.index = index
        self.timeStamp = timeStamp
        self.data = data
        self.lastHash = lastHash
        self.selfHash = self.hash_TTBlockCoin()

    # 产生加密串,产生一个加密串就是产生一个币
    def hash_TTBlockCoin(self):
        # sha = hashlib.sha256()
        # sha = hashlib.sha512()
        sha = hashlib.md5()
        datastr = str(self.index) + str(self.timeStamp) + str(self.data) + str(self.lastHash)
        sha.update(datastr.encode("utf-8"))
        return sha.hexdigest()


def create_first_TTBlock():  # 创造一个创世区块
    return TTBlockCoin(0, datetime.datetime.now(), "TT COIN", "tt001")


def create_money_TTBlock(last_block):  # 区块链的其他块  last_block 上一个区块
    this_index = last_block.index + 1
    this_timestamp = datetime.datetime.now()
    this_data = "taotao coin" + str(this_index)  # 模拟交易数据
    last_hash = last_block.selfHash    #lastHash =上一个block的selfHash
    return TTBlockCoin(this_index,
                         this_timestamp,
                         this_data,
                         last_hash)


TTBlockCoins = [create_first_TTBlock()]  # 区块链链表
nums = 100
head_block = TTBlockCoins[0]
print("创世区块TT币来啦")
print(head_block.index, head_block.data, head_block.timeStamp,
      head_block.lastHash, head_block.selfHash)
for i in range(nums):
    ttBlock_another = create_money_TTBlock(head_block)  # 根据第一个区块创造下一个区块
    TTBlockCoins.append(ttBlock_another)  # 区块加入链
    head_block = ttBlock_another
    print(ttBlock_another.index, ttBlock_another.data,
          ttBlock_another.timeStamp, ttBlock_another.lastHash,
          ttBlock_another.selfHash)
