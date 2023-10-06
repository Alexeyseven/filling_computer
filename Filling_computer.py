import pygame
import math
import socket
import os
from init import register, sectors


RES = WIDTH, HEIGHT = 400, 400
H_WIDTH, H_HEIGHT = WIDTH // 2, HEIGHT // 2
RADIUS = H_HEIGHT - 50

pygame.init()
surface = pygame.display.set_mode(RES)

clock60 = dict(zip(range(360), range(0, 360, 1)))

encoder = 0
enum = 0

s = socket.socket()
s.bind(('192.168.1.241', 2000))
s.listen(10)

os.system('start cmd /k python encoder.py')
conn1, addr1 = s.accept()

os.system('start cmd /k python valve_1_2_3.py')
conn2, addr2 = s.accept()

os.system('start cmd /k python valve_4_5_6.py')
conn3, addr3 = s.accept()

os.system('start cmd /k python valve_7_8_9.py')
conn4, addr4 = s.accept()

os.system('start cmd /k python valve_10_11_12.py')
conn5, addr5 = s.accept()

os.system('start cmd /k python valve_13_14_15.py')
conn6, addr6 = s.accept()

os.system('start cmd /k python valve_16_17_18.py')
conn7, addr7 = s.accept()

os.system('start cmd /k python valve_19_20_21.py')
conn8, addr8 = s.accept()

os.system('start cmd /k python valve_22_23_24.py')
conn9, addr9 = s.accept()

os.system('start cmd /k python valve_25_26_27.py')
conn10, addr10 = s.accept()

os.system('start cmd /k python valve_28_29_30.py')
conn11, addr11 = s.accept()

os.system('start cmd /k python valve_31_32_33.py')
conn12, addr12 = s.accept()

os.system('start cmd /k python valve_34_35_36.py')
conn13, addr13 = s.accept()

os.system('start cmd /k python valve_37_38_39.py')
conn14, addr14 = s.accept()


def get_clock_pos(clock_dict, clock_hand):
    x = H_WIDTH + RADIUS * math.cos(
        math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = H_HEIGHT + RADIUS * math.sin(
        math.radians(clock_dict[clock_hand]) - math.pi / 2)
    return x, y


def shift_register():
    for i in register:
        if encoder == i[1]:
            i[0] = True
        if i[0] is True:
            i[2] += 1
            if i[2] == 360:
                i[2] = 0


def send_data(i, conn, valve):
    if i in sectors.keys():
        conn.send(str.encode(f'{valve}'+'_'+f'{sectors[i]}'))                


pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

valves = [[conn2, 'valve_1'],
          [conn2, 'valve_2'],
          [conn2, 'valve_3'],
          [conn3, 'valve_4'],
          [conn3, 'valve_5'],
          [conn3, 'valve_6'],
          [conn4, 'valve_7'],
          [conn4, 'valve_8'],
          [conn4, 'valve_9'],
          [conn5, 'valve_10'],
          [conn5, 'valve_11'],
          [conn5, 'valve_12'],
          [conn6, 'valve_13'],
          [conn6, 'valve_14'],
          [conn6, 'valve_15'],
          [conn7, 'valve_16'],
          [conn7, 'valve_17'],
          [conn7, 'valve_18'],
          [conn8, 'valve_19'],
          [conn8, 'valve_20'],
          [conn8, 'valve_21'],
          [conn9, 'valve_22'],
          [conn9, 'valve_23'],
          [conn9, 'valve_24'],
          [conn10, 'valve_25'],
          [conn10, 'valve_26'],
          [conn10, 'valve_27'],
          [conn11, 'valve_28'],
          [conn11, 'valve_29'],
          [conn11, 'valve_30'],
          [conn12, 'valve_31'],
          [conn12, 'valve_32'],
          [conn12, 'valve_33'],
          [conn13, 'valve_34'],
          [conn13, 'valve_35'],
          [conn13, 'valve_36'],
          [conn14, 'valve_37'],
          [conn14, 'valve_38'],
          [conn14, 'valve_39']]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    data = conn1.recv(70)
    surface.fill([235, 235, 235])

    shift_register()

    if data == b'1':
        encoder += 1

    for j in valves:
        send_data(register[enum][2], j[0], j[1]) 
        enum += 1  

    enum = 0    
    
    pygame.draw.circle(surface, pygame.Color('darkslategray'), (H_WIDTH, H_HEIGHT), RADIUS)
    pygame.draw.line(surface, pygame.Color('black'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, 0), 4)

    for i in sectors.keys():
        pygame.draw.line(surface, pygame.Color('green'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, i), 4)

    for i in range(4):
        pygame.draw.line(surface, pygame.Color('magenta'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, register[i][2]), 2)

    pygame.display.flip()
