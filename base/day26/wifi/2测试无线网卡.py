import logging
import platform

import pywifi

pywifi.set_loglevel(logging.INFO)

def go_interfaces():

    wifi = pywifi.PyWiFi() #创建wifi对象

    assert wifi.interfaces() #抓取网卡接口

    if platform.system().lower() == 'windows': #判断平台
        print(wifi.interfaces()[0].name())
        assert wifi.interfaces()[0].name() ==\
            'Intel(R) Dual Band Wireless-AC 3160'

go_interfaces()