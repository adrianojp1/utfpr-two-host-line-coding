from PyQt5 import QtCore, QtWidgets
import pyqtgraph as pg


class GraphicalUserInterface(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.tabelaValores = QtWidgets.QTableWidget(self.centralwidget)
        header = self.tabelaValores.horizontalHeader()
        header.setResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setStretchLastSection(True)
        self.tabelaValores.setGeometry(QtCore.QRect(40, 90, 711, 113))
        self.tabelaValores.setMaximumSize(QtCore.QSize(711, 16777215))
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
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(310, 10, 200, 31))
        self.label_1.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_1.setObjectName("label")
        self.grafico = pg.PlotWidget(self.centralwidget)
        self.grafico.setGeometry(QtCore.QRect(40, 270, 711, 241))
        self.grafico.setObjectName("grafico")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 230, 50, 31))
        self.label_2.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_2.setObjectName("label_3")
        self.comm_buttom = QtWidgets.QPushButton(self.centralwidget)
        self.comm_buttom.setGeometry(QtCore.QRect(670, 210, 80, 21))
        self.comm_buttom.setObjectName("botaoEnvio")
        self.setCentralWidget(self.centralwidget)

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
        self.comm_buttom.setText(_translate("MainWindow", self.button_label))
        self.comm_buttom.clicked.connect(self.buttom_action)

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

        signal_levels = [int(level) for level in (signal.split(','))]
        a = list(range(len(signal_levels)))
        self.grafico.clear()
        self.grafico.plot(a, signal_levels, pen=None, symbol='o')
