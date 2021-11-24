import socket
import threading

HOST = socket.gethostbyname(socket.gethostname()) #colocar o host 
PORT = 8080 #colocar um port acima de 1000

print(HOST)

svr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
svr.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
svr.bind((HOST, PORT))


svr.listen(5)

con, adr = svr.accept()  
msg = con.recv(1024)
print(msg.decode('utf-8'))

con.close()

