from string import Template #string文件导入Template
print(type(Template))
mystr=Template("hi,$name  你是  $baby")
print(mystr.substitute(name="何丰成",baby="lovely babay"))