'''
import  collections  #数据结构集合
queue=collections.deque([1,2,3,4,5])
print(queue)
queue.append(6)
print(queue)
queue.append(7)
print(queue)
print(queue.popleft()) #获取要弹出的屎的值，然后弹出
print(queue)
'''

from collections  import  deque#数据结构集合
queue=deque([1,2,3,4,5])
print(queue)
queue.append(6)
print(queue)
queue.append(7)
print(queue)
print(queue.popleft()) #获取要弹出的屎的值，然后弹出
print(queue)
