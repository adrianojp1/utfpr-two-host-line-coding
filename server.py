import socket
import sys
import threading
from PyQt5 import QtCore, QtWidgets
import pyqtgraph as pg
from encode import binary_decode, decrypt, encrypt, binary_encode, mlt3_line_decode, mlt3_line_encode

#HOST = socket.gethostbyname(socket.gethostname()) #colocar o host 
HOST = "25.0.9.210"
PORT = 3000 #colocar um port acima de 1000

class graphicInterfaceService(object):
    _buffer = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabelaValores = QtWidgets.QTableWidget(self.centralwidget)
        self.tabelaValores.setGeometry(QtCore.QRect(40, 90, 711, 111))
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
        self.label.setGeometry(QtCore.QRect(360, 10, 81, 31))
        self.label.setTextFormat(QtCore.Qt.MarkdownText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 50, 91, 31))
        self.label_2.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_2.setObjectName("label_2")
        #grafico = QtWidgets.QGraphicsView(self.centralwidget)
        self.grafico = pg.PlotWidget(self.centralwidget)
        self.grafico.setGeometry(QtCore.QRect(40, 270, 711, 241))
        self.grafico.setObjectName("grafico")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 230, 41, 31))
        self.label_3.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_3.setObjectName("label_3")
        self.botaoEnvio = QtWidgets.QPushButton(self.centralwidget)
        self.botaoEnvio.setGeometry(QtCore.QRect(670, 210, 80, 21))
        self.botaoEnvio.setObjectName("botaoEnvio")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        threading.Thread(target=graphicInterfaceService.listen).start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Trabalho de comunicacao de dados - Equipe Minecraft", "Receiver"))
        item = self.tabelaValores.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mensagem escrita"))
        item = self.tabelaValores.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Mensagem binário"))
        item = self.tabelaValores.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mensagem algoritmo"))
        item = self.tabelaValores.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Valores"))
        self.label.setText(_translate("MainWindow", "Equipe Minecraft"))
        self.label_2.setText(_translate("MainWindow", "Tabela de valores"))
        self.label_3.setText(_translate("MainWindow", "Gráfico"))
        self.botaoEnvio.setText(_translate("MainWindow", "Ouvir"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.botaoEnvio.clicked.connect(self.button_clicked)

    def button_clicked(self):
        msg = self.receive()
        len_msg = len(msg)
        if (len_msg > 0):
            signal = [int(level) for level in msg.split(',')]
            a = list(range(len(signal)))
            self.grafico.plot(a, signal, pen=None, symbol='o')

            binary = mlt3_line_decode(signal)
            encrypted = binary_decode(binary)
            msg = decrypt(encrypted)

            signal_str = ','.join([str(bit) for bit in signal])
            bin_str = ''.join([str(bit) for bit in binary])

            self.set_algorithm_msg(signal_str)
            self.set_binary_msg(bin_str)
            self.set_text_msg(msg)

    def receive(self):
        if self.hasData():
            return ''.join([x for x in list(self.getData())])
        return []

    def hasData(self):
        return True if self._buffer else False

    def getData(self):
        return self._buffer.pop(0).decode("utf-8")

    def set_text_msg(self, value):
        self.tabelaValores.setItem(0, 0, QtWidgets.QTableWidgetItem(value))

    def set_binary_msg(self, value):
        self.tabelaValores.setItem(1, 0, QtWidgets.QTableWidgetItem(value))

    def set_algorithm_msg(self, value):
        self.tabelaValores.setItem(2, 0, QtWidgets.QTableWidgetItem(value))
 
    @staticmethod
    def listen():
        while True:
            svr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            svr.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            svr.bind((HOST, PORT))

            svr.listen(5)

            con, adr = svr.accept() 
            data = con.recv(10*1024*1024)
            
            graphicInterfaceService._buffer.append(data)
            #Para testar. Setar na janela da interface quando estiver correto.
            print(data.decode('utf-8'))
            con.close()

def start_svr():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = graphicInterfaceService()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

start_svr()
