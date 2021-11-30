#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from encode import binary_decode, decrypt, mlt3_line_decode

from gui import GraphicalUserInterface
from communication import Communication as conn


class Receiver(GraphicalUserInterface):
    def __init__(self):
        self.windows_title = "Receiver"
        self.table_header_label = "Dados recebidos"
        self.main_label = "Receiver - Equipe Minecraft"
        self.button_label = "Ouvir"
        self.buttom_action = self.receive_and_update

        super().__init__()

        conn.start()

    def receive_and_update(self):
        data = conn.receive()
        if (data):
            signal = data
            binary = mlt3_line_decode(signal)
            encrypted = binary_decode(binary)
            msg = decrypt(encrypted)

            self.update_gui(msg, binary, signal)


def main():
    app = QtWidgets.QApplication(sys.argv)
    Receiver()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
