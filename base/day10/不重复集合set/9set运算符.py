set1={1,2,3,4,5}
set2={1,2,7,8,9}
set3={1,2,3,4,5}
set4={1,2,3,4,5,6}
'''
print(set3.difference(set4)) # difference差异
print(set4.difference(set3))
print( 1  in  set3) #仅仅用于单个元素，不用于集合之间关系
print( 10  not  in  set3)
print(set1-set2) #set1有，set2没有
print(set2-set1) #set2有，set1没有
print(set1 & set2) #set1,set2共有
print(set1 | set2) #包含set1,set2,没有重复
print(set1 ^ set2)#并集-交集-，特色文化遗产
print(set1 == set3)  #==,!=相等
'''

