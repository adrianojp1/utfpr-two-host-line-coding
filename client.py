#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from encode import binary_encode, encrypt, mlt3_line_encode

from gui import GraphicalUserInterface
from communication import Communication as conn


class Sender(GraphicalUserInterface):
    def __init__(self):
        self.windows_title = "Sender"
        self.table_header_label = "Dados enviados"
        self.main_label = "Sender - Equipe Minecraft"
        self.button_label = "Enviar"
        self.buttom_action = self.send_and_update

        super().__init__()

    def send_and_update(self):
        msg = self.tabelaValores.item(0, 0).text()
        encrypted = encrypt(msg)
        binary = binary_encode(encrypted)
        signal = mlt3_line_encode(binary)

        self.update_gui(msg, binary, signal)
        conn.send(signal)


def main():
    app = QtWidgets.QApplication(sys.argv)
    Sender()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
