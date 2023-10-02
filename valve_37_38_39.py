import socket


s = socket.socket()
s.connect(('192.168.1.241', 2000))


while True:
    data = s.recv(1024) 
    print(data)
