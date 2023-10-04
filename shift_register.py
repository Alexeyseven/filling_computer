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
shift_j = False
j = 0
shift_k = False
k = 0

s = socket.socket()
s.bind(('192.168.1.241', 2000))
s.listen(3)

os.system('start cmd /k python encoder.py')

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

    if data == b'1':
        i += 1

    if i == 120:
        shift_j = True
    
    if i == 360:
        i = 0

    if shift_j:
        j += 1

    if j == 360:
        j = 0

    if i == 240:
        shift_k = True  

    if shift_k:
        k += 1      

    if k == 360:
        k = 0

    text1 = font.render(f'{str(i)}', True, (180, 0, 0))
    text2 = font.render(f'{str(j)}', True, (180, 0, 0))
    text3 = font.render(f'{str(k)}', True, (180, 0, 0))
    surface.blit(text1, (20, 10))
    surface.blit(text2, (340, 10))
    surface.blit(text3, (20, 340))
    
    pygame.draw.circle(surface, pygame.Color('darkslategray'), (H_WIDTH, H_HEIGHT), RADIUS)
    pygame.draw.line(surface, pygame.Color('green'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, 0), 2)
    pygame.draw.line(surface, pygame.Color('green'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, 120), 2)
    pygame.draw.line(surface, pygame.Color('green'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, 240), 2)
    pygame.draw.line(surface, pygame.Color('magenta'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, i), 4)
    pygame.draw.line(surface, pygame.Color('magenta'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, j), 4)
    pygame.draw.line(surface, pygame.Color('magenta'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, k), 4)
    
    pygame.display.flip()
