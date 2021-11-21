#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from graphicInterfaceService import graphicInterfaceService


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = graphicInterfaceService()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
