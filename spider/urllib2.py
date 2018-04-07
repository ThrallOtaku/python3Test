import urllib.request as ur

response = ur.urlopen("http://www.baidu.com")
html = response.read()

print(html)
