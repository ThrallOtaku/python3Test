import pywifi
from pywifi import const


def test_disconnect():  # 断开网络连接，

    wifi = pywifi.PyWiFi()

    iface = wifi.interfaces()[0]  # 第一个无限网卡
    iface.disconnect()

    assert iface.status() in \
           [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
