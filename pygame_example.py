import pygame
import math
import time
import socket
import os


RES = WIDTH, HEIGHT = 400, 400
H_WIDTH, H_HEIGHT = WIDTH // 2, HEIGHT // 2
RADIUS = H_HEIGHT - 50

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
    if i == 0:
        conn1.send(b'valve_1_start_pos')
    if i == 2:
        conn1.send(b'valve_2_start_pos')    
    if i == 5:
        conn1.send(b'valve_1_CO2')
    if i == 7:
        conn1.send(b'valve_2_CO2')
    if i == 9:
        conn1.send(b'valve_1_slow_filling')
    if i == 17:
        conn1.send(b'valve_2_slow_filling')
    if i == 19:
        conn1.send(b'valve_1_fast_filling')
    if i == 37:
        conn1.send(b'valve_2_fast_filling')
    if i == 39:
        conn1.send(b'valve_1_press_reset')
    if i == 87:
        conn1.send(b'valve_2_press_reset')    
    if i == 95:
        conn1.send(b'valve_1_start_pos')
    if i == 97:
        conn1.send(b'valve_2_start_pos')

    text = font.render(f'{str(i)}', True, (180, 0, 0))
    surface.blit(text, (20, 10))
    
    pygame.draw.circle(surface, pygame.Color('darkslategray'), (H_WIDTH, H_HEIGHT), RADIUS)
    pygame.draw.line(surface, pygame.Color('magenta'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, i), 4)
    
    pygame.display.flip()
