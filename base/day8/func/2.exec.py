import os
#mystr='os.system("notepad")' #文本当作语句执行
mystr="os.system(\"notepad\") " #转义字符，  字符串中\" 等价于"
exec (mystr)