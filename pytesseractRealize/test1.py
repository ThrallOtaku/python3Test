from PIL import Image
import pytesseract

# 上面都是导包，只需要下面这一行就能实现图片文字识别

text = pytesseract.image_to_string(Image.open('baiwan.png'),lang='chi_sim')
#text = pytesseract.image_to_string(Image.open('xiaolin.png'),lang='eng')
print(text)
