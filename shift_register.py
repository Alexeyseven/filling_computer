import pygame
import math
import time
import socket
import os
from register import register


RES = WIDTH, HEIGHT = 400, 400
H_WIDTH, H_HEIGHT = WIDTH // 2, HEIGHT // 2
RADIUS = H_HEIGHT - 50

pygame.init()
surface = pygame.display.set_mode(RES)

clock60 = dict(zip(range(360), range(0, 360, 1)))

encoder = 0

s = socket.socket()
s.bind(('192.168.1.241', 2000))
s.listen(3)

os.system('start cmd /k python encoder.py')

conn3, addr3 = s.accept()


def get_clock_pos(clock_dict, clock_hand):
    x = H_WIDTH + RADIUS * math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = H_HEIGHT + RADIUS * math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    return x, y


def shift_register():
    for i in register:
        if encoder == i[1]:
            i[0] = True
        if i[0] == True:
            i[2] += 1
            if i[2] == 360:
                i[2] = 0


pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    data = conn3.recv(70)
    surface.fill([235, 235, 235])

    shift_register()

    if data == b'1':
        encoder += 1

    text1 = font.render(f'{str(register[0][2])}', True, (180, 0, 0))
    text2 = font.render(f'{str(register[1][2])}', True, (180, 0, 0))
    text3 = font.render(f'{str(register[2][2])}', True, (180, 0, 0))
    text4 = font.render(f'{str(register[3][2])}', True, (180, 0, 0))
    text5 = font.render(f'{str(register[4][2])}', True, (180, 0, 0))
    text6 = font.render(f'{str(register[5][2])}', True, (180, 0, 0))
    text7 = font.render(f'{str(register[6][2])}', True, (180, 0, 0))
    text8 = font.render(f'{str(register[7][2])}', True, (180, 0, 0))
    text9 = font.render(f'{str(register[8][2])}', True, (180, 0, 0))
    text10 = font.render(f'{str(register[9][2])}', True, (180, 0, 0))
    surface.blit(text1, (10, 10))
    surface.blit(text2, (10, 40))
    surface.blit(text3, (10, 70))
    surface.blit(text4, (10, 100))
    surface.blit(text5, (10, 130))
    surface.blit(text6, (10, 160))
    surface.blit(text7, (10, 190))
    surface.blit(text8, (10, 220))
    surface.blit(text9, (10, 250))
    surface.blit(text10, (10, 270))
    
    pygame.draw.circle(surface, pygame.Color('darkslategray'), (H_WIDTH, H_HEIGHT), RADIUS)
    pygame.draw.line(surface, pygame.Color('green'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, 0), 2)
    pygame.draw.line(surface, pygame.Color('green'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, 10), 2)
    pygame.draw.line(surface, pygame.Color('green'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, 20), 2)
    pygame.draw.line(surface, pygame.Color('magenta'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, register[0][2]), 4)
    
    pygame.display.flip()