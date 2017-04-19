import sys
from PyQt4 import QtGui, QtCore
from gui.win.main import Ui_win_main


class MyWindowClass(QtGui.QMainWindow, Ui_win_main):
    veces = 0

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)


app = QtGui.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
# MyWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
MyWindow.show()
app.exec_()
