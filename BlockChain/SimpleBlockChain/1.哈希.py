import hashlib #加密模块

#sha=hashlib.sha256() #加密算法，sha256
#sha=hashlib.md5() #加密算法，md5
sha=hashlib.sha512()
sha.update("000000".encode("utf-8"))#转化2进制
print(sha.hexdigest())#哈希值

#8bb0cf6eb9b17d0f7d22b456f121257dc1254e1f01665370476383ea776df414  1234567
#07ba38d7a9affba269a613da6d99a7ffa4d128ce38f5e24ee5a7383b796b58b2  1234568
#91b4d142823f7d20c5f08df69122de43f35f057a988d9619f6d3138485c9a203  000000
#20fdf64da3cd2c78ec3c033d2ac628bacf701711fa99435ee37bef0304800dc5  0000000
#哈希算法
#  15   125   135  %10=5    数据加工抽象->