from PyQt5 import QtWidgets  # 通用窗口类
import sys


class firstWindow(QtWidgets.QWidget):
    # 类的初始化方法
    # 类中的函数必须要有self,表示该类本身的属性
    def __init__(self):
        super(firstWindow, self).__init__()


def newWindows():
    app = QtWidgets.QApplication(sys.argv)
    # 生成一个实例对象
    windows = firstWindow()
    windows.show()
    sys.exit(app.exec_())


# main 方法入口。如果不写这个，默认执行整个文件
if __name__ == "__main__":
    newWindows()
