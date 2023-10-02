import socket
import time

s = socket.socket()
s.connect(('192.168.1.241', 2000))
i = 0


while True:
    if i == 360:
        i = 0
    s.send(str.encode(f'{i}'))
    i += 1
    time.sleep(0.08)
