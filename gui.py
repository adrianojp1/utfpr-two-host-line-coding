from PyQt5 import QtCore, QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavToolbar


class GraphicalUserInterface(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setObjectName("MainWindow")
        self.resize(800, 500)
        
        self.tabelaValores = QtWidgets.QTableWidget()
        header = self.tabelaValores.horizontalHeader()
        header.setStretchLastSection(True)
        self.tabelaValores.setGeometry(QtCore.QRect(40, 90, 711, 113))
        self.tabelaValores.setMaximumHeight(113)
        self.tabelaValores.setObjectName("tabelaValores")
        self.tabelaValores.setColumnCount(1)
        self.tabelaValores.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaValores.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaValores.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaValores.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaValores.setHorizontalHeaderItem(0, item)

        self.label_1 = QtWidgets.QLabel()
        self.label_1.setGeometry(QtCore.QRect(310, 10, 200, 31))
        self.label_1.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_1.setObjectName("label_1")

        self.label_2 = QtWidgets.QLabel()
        self.label_2.setGeometry(QtCore.QRect(370, 230, 50, 31))
        self.label_2.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_2.setObjectName("label_3")

        self.conn_buttom = QtWidgets.QPushButton()
        self.conn_buttom.setGeometry(QtCore.QRect(670, 210, 80, 21))
        self.conn_buttom.setObjectName("botaoEnvio")

        xpixels = 600
        ypixels = 150
        dpi = 72.
        xinch = xpixels / dpi
        yinch = ypixels / dpi
        self.figure = Figure(figsize=(xinch, yinch))
        self.figure.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0, wspace=0)
        self.canvas = FigureCanvas(self.figure)
        self.addToolBar(NavToolbar(self.canvas, self))
        self.ax = self.figure.add_subplot(111)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label_1)
        layout.addWidget(self.tabelaValores)
        layout.addWidget(self.conn_buttom)
        layout.addWidget(self.label_2)
        layout.addWidget(self.canvas)
        centralWidget = QtWidgets.QWidget(self)
        centralWidget.setLayout(layout)
        
        self.setCentralWidget(centralWidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate(
            "Trabalho de comunicacao de dados - Equipe Minecraft", self.windows_title))
        item = self.tabelaValores.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mensagem escrita"))
        item = self.tabelaValores.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Mensagem binária"))
        item = self.tabelaValores.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mensagem algoritmo"))
        item = self.tabelaValores.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", self.table_header_label))
        self.label_1.setText(_translate("MainWindow", self.main_label))
        self.label_2.setText(_translate("MainWindow", "Gráfico"))
        self.conn_buttom.setText(_translate("MainWindow", self.button_label))
        self.conn_buttom.clicked.connect(self.buttom_action)

    def update_gui(self, msg, binary, signal):
        self.update_msg(msg)
        self.update_bin(binary)
        self.update_signal(signal)

    def update_msg(self, msg):
        self.tabelaValores.setItem(0, 0, QtWidgets.QTableWidgetItem(msg))

    def update_bin(self, binary):
        bin_str = ''.join([str(bit) for bit in binary])
        self.tabelaValores.setItem(1, 0, QtWidgets.QTableWidgetItem(bin_str))

    def update_signal(self, signal):
        self.tabelaValores.setItem(2, 0, QtWidgets.QTableWidgetItem(signal))

        self.ax.clear()
        if (signal):
            signal_levels = [int(level) for level in (signal.split(','))]
            signal_levels.append(signal_levels[-1])
            self._plot(range(0, len(signal_levels)), signal_levels)
        self.canvas.draw()

    def _plot(self, x, y):
        self.ax.plot(x, y, drawstyle='steps-post')
        self.ax.set_xticks(x)
        self.ax.set_yticks(range(-2, 3))
        self.ax.grid()