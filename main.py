from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtWidgets, QtGui
import sys


def window():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setGeometry(200, 200, 500, 200)
    window.setWindowTitle("โปรแกรมคำนวณหวย")
    window.setMinimumSize(500, 200)
    window.setMaximumSize(800, 500)
    window.setWindowIcon(QtGui.QIcon("C:\\Users\\SamitPCGenius\\Downloads\\YouTube_23392.png"))
    window.show()
    sys.exit(app.exec_())

window()