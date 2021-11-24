import socket

HOST = "172.21.32.1"  #colocar o host (e.g., localhost)
PORT = 8080  #colocar o port

cnt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cnt.connect((HOST, PORT))


msg = cnt.send("O pé do Zé tem chulé".encode('utf-8'))

cnt.close()