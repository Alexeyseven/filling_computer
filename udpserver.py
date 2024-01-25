import socket
import struct
import os


sectors = [20, 120, 400, 800, 900]

visu_trigger = False

messages = {20 : b'0',
			120 : b'1',
			400 : b'2',
			800 : b'3',
			900 : b'4'}
 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('192.168.1.241', 10001))
s.settimeout(5)
 
while True:
	try:
		mes = s.recvfrom(2)
		addr = mes[1]
		mes = mes[0]
		encoder = struct.unpack('<H', mes)[0]
		if encoder == 1 and visu_trigger == False:
			os.system('start cmd /k python pygame_example.py')
			visu_trigger = True
		if encoder in sectors:
			print(encoder)
			s.sendto(messages[encoder], ('192.168.1.5', 10000))
	except socket.timeout:
		pass		
	