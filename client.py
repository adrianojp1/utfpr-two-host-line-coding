import socket

HOST = ''  #colocar o host (e.g., localhost)
PORT = ''  #colocar o port

cnt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cnt.connect((HOST, PORT))
#recebe 1024 bytes
msg = cnt.recv(1024)
cnt.close()