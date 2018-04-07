# 程序从这里执行
import Message
import Block
import BlockChain

print("game  start")
m1 = Message.MoneyMessage("yincheng pay  baidu 100a")
m2 = Message.MoneyMessage("yincheng pay  baidu 1000b")
m3 = Message.MoneyMessage("yincheng pay  baidu 10000c")
yin1 = Block.MoneyBlock(m1, m2, m3)  # 一次加入三条记录
yin1.seal()  # 数据密封
# yin1.moneymessage[0]=m3  #纂改
m4 = Message.MoneyMessage("yincheng pay  baidu 100ab")
m5 = Message.MoneyMessage("yincheng pay  baidu 1000bc")
m6 = Message.MoneyMessage("yincheng pay  baidu 10000cd")
yin2 = Block.MoneyBlock(m4, m5, m6)  # 一次加入三条记录
yin2.seal()  # 数据密封

m7 = Message.MoneyMessage("yincheng pay  baidu 100abc")
m8 = Message.MoneyMessage("yincheng pay  baidu 1000bcd")
m9 = Message.MoneyMessage("yincheng pay  baidu 10000cde")
yin3 = Block.MoneyBlock(m7, m8, m9)
yin3.seal()  # 数据密封

mydada = BlockChain.DaDaMoneyBlockChain()
mydada.add_block(yin1)
mydada.add_block(yin2)
mydada.add_block(yin3)
mydada.validate()
