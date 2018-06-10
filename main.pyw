from UI.mainwindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


if '__main__' == __name__:
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
