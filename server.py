import socket
import struct

HOST = '' #colocar o host (e.g., localhost)
PORT = '' #colocar o port

svr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
svr.bind((HOST, PORT))
svr.listen(5)

while True:
	c, addr = svr.accept() 
	#caso precise do tamanho da mensagem
	#svr.send(struct.pack('i', len(msg))) 
	svr.send("Mensagem codificada") 

c.close()

