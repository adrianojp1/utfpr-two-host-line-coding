import socket
import threading


class Communication(object):
    _buffer = []
    HOST = "localhost"
    PORT = 3000

    @staticmethod
    def start():
        threading.Thread(target=Communication.listen).start()

    @staticmethod
    def listen():
        while True:
            svr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            svr.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            svr.bind((Communication.HOST, Communication.PORT))

            svr.listen(5)

            con, adr = svr.accept()
            data = con.recv(10*1024*1024)

            Communication._buffer.append(data)
            print(data.decode('utf-8'))
            con.close()

    @staticmethod
    def receive():
        def getData():
            return Communication._buffer.pop(0).decode("utf-8")

        if Communication._buffer:
            return ''.join([x for x in list(getData())])
        return []

    @staticmethod
    def send(data):
        skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        skt.connect((Communication.HOST, Communication.PORT))

        skt.send(bytes(data.encode('utf-8')))
        skt.close()
