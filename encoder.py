import socket
import time

s = socket.socket()
s.connect(('192.168.1.241', 2000))
i = 0


while True:
    s.send(str.encode(f'{1}'))
    time.sleep(0.08)
