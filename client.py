import socket
import sys
from PyQt5 import QtCore, QtWidgets
import pyqtgraph as pg
from encode import encrypt, binary_encode, mlt3_line_encode

HOST = "25.0.9.210"  #colocar o host (e.g., localhost)
PORT = 3000  #colocar o port

class graphicInterfaceService(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 10, 200, 31))
        self.label.setTextFormat(QtCore.Qt.MarkdownText)
        self.label.setObjectName("label")
        #grafico = QtWidgets.QGraphicsView(self.centralwidget)
        self.grafico = pg.PlotWidget(self.centralwidget)
        self.grafico.setGeometry(QtCore.QRect(40, 270, 711, 241))
        self.grafico.setObjectName("grafico")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 230, 50, 31))
        self.label_3.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_3.setObjectName("label_3")
        self.botaoEnvio = QtWidgets.QPushButton(self.centralwidget)
        self.botaoEnvio.setGeometry(QtCore.QRect(670, 210, 80, 21))
        self.botaoEnvio.setObjectName("botaoEnvio")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Trabalho de comunicacao de dados - Equipe Minecraft", "Sender"))
        item = self.tabelaValores.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mensagem escrita"))
        item = self.tabelaValores.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Mensagem binário"))
        item = self.tabelaValores.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mensagem algoritmo"))
        item = self.tabelaValores.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Dados enviados"))
        self.label.setText(_translate("MainWindow", "Sender - Equipe Minecraft"))
        self.label_3.setText(_translate("MainWindow", "Gráfico"))
        self.botaoEnvio.setText(_translate("MainWindow", "Enviar"))
        self.botaoEnvio.clicked.connect(self.button_clicked)

    def button_clicked(self):
        msg = self.tabelaValores.item(0, 0).text()
        encrypted = encrypt(msg)
        binary = binary_encode(encrypted)
        signal = mlt3_line_encode(binary)

        bin_str = ''.join([str(bit) for bit in binary])
        signal_str = ','.join([str(bit) for bit in signal])

        self.set_binary_msg(bin_str)
        self.set_algorithm_msg(signal_str)
        a = list(range(len(signal)))
        self.grafico.clear()
        self.grafico.plot(a, signal, pen=None, symbol='o')

        cnt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cnt.connect((HOST, PORT))

        print(signal_str)
        cnt.send(bytes(signal_str.encode('utf-8')))
        cnt.close()


    def set_binary_msg(self, value):
        self.tabelaValores.setItem(1, 0, QtWidgets.QTableWidgetItem(value))

    def set_algorithm_msg(self, value):
        self.tabelaValores.setItem(2, 0, QtWidgets.QTableWidgetItem(value))

def start_cnt():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = graphicInterfaceService()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

start_cnt()