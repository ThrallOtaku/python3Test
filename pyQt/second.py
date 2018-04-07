from PyQt5 import QtWidgets
from first import firstWindow

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    new =firstWindow()
    new.show()
    sys.exit(app.exec_())
