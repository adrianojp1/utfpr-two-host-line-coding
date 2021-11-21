# This Python file uses the following encoding: utf-8
import sys
from PyQt5 import QtWidgets
from PySide2.QtWidgets import QApplication
from graphicInterfaceService import graphicInterfaceService

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = graphicInterfaceService()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
