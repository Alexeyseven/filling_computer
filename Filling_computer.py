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
s.listen(3)

os.system('start cmd /k python encoder.py')
conn1, addr1 = s.accept()

os.system('start cmd /k python valve_1_2_3.py')
conn2, addr2 = s.accept()

os.system('start cmd /k python valve_4_5_6.py')
conn3, addr3 = s.accept()


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
          [conn3, 'valve_6']]


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
