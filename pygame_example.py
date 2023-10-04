import pygame
import math
import time
import socket
import os


RES = WIDTH, HEIGHT = 400, 400
H_WIDTH, H_HEIGHT = WIDTH // 2, HEIGHT // 2
RADIUS = H_HEIGHT - 50

sectors = {0: 'start_pos',
           10: 'CO2',
           60: 'slow_filling',
           120: 'fast_filling',
           310: 'press_reset',
           340: 'start_pos'}

pygame.init()
surface = pygame.display.set_mode(RES)

clock60 = dict(zip(range(360), range(0, 360, 1)))

i = 0

s = socket.socket()
s.bind(('192.168.1.241', 2000))
s.listen(3)

os.system('start cmd /k python valve_1_2_3.py')
os.system('start cmd /k python encoder.py')

conn1, addr1 = s.accept()
conn3, addr3 = s.accept()

valves = [[0, conn1, 'valve_1'],
          [120, conn1, 'valve_2'],
          [240, conn1, 'valve_3']]


def send_data(i, conn, valve):
    if 360-i in sectors.keys():
        conn.send(str.encode(f'{valve}'+'_'+f'{sectors[360-i]}'))


def get_clock_pos(clock_dict, clock_hand):
    x = H_WIDTH + RADIUS * math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = H_HEIGHT + RADIUS * math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    return x, y


pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    data = conn3.recv(70)
    surface.fill([235, 235, 235])

    i = int(data.decode('cp1251'))

    for j in valves:
        send_data(360-i+j[0], j[1], j[2])

    text = font.render(f'{str(i)}', True, (180, 0, 0))
    surface.blit(text, (20, 10))
    
    pygame.draw.circle(surface, pygame.Color('darkslategray'), (H_WIDTH, H_HEIGHT), RADIUS)
    pygame.draw.line(surface, pygame.Color('magenta'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, i), 4)
    
    pygame.display.flip()
