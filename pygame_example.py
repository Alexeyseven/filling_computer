import pygame
import math
import time


RES = WIDTH, HEIGHT = 400, 400
H_WIDTH, H_HEIGHT = WIDTH // 2, HEIGHT // 2
RADIUS = H_HEIGHT - 50

pygame.init()
surface = pygame.display.set_mode(RES)
clock60 = dict(zip(range(360), range(0, 360, 1)))

i = 1
j = 0


def get_clock_pos(clock_dict, clock_hand):
    x = H_WIDTH + RADIUS * math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = H_HEIGHT + RADIUS * math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    return x, y


def diapason_transpole(max_vis, min_vis, max_rob, min_rob, coordinate):
   return((max_rob-min_rob)*(coordinate-min_vis)/(max_vis-min_vis)+min_rob)


pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
font_1 = pygame.font.SysFont('Comic Sans MS', 14)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    surface.fill([235, 235, 235])
    
    j = int(diapason_transpole(360, 0, 1024, 0, i))
    text = font.render(f'{str(j)}', True, (180, 0, 0))
    surface.blit(text, (20, 10))

    CO2 = font_1.render('CO2', True, (0, 0, 255))
    surface.blit(CO2, (220, 20))

    slow_filling = font_1.render('slow_filling', True, (0, 0, 255))
    surface.blit(slow_filling, (277, 50))

    fast_filling = font_1.render('fast_filling', True, (0, 0, 255))
    surface.blit(fast_filling, (287, 327))

    press_reset = font_1.render('press_reset', True, (0, 0, 255))
    surface.blit(press_reset, (2, 170))

    start_pos = font_1.render('start_pos', True, (0, 0, 255))
    surface.blit(start_pos, (20, 70))
    
    pygame.draw.circle(surface, pygame.Color('darkslategray'), (H_WIDTH, H_HEIGHT), RADIUS)
    pygame.draw.line(surface, pygame.Color('magenta'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, i), 4)

    pygame.draw.line(surface, pygame.Color('green'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, 7), 2)
    pygame.draw.line(surface, pygame.Color('orange'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, 42), 2)
    pygame.draw.line(surface, pygame.Color('red'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, 140), 2)
    pygame.draw.line(surface, pygame.Color('blue'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, 281), 2)
    pygame.draw.line(surface, pygame.Color('gray'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, 316), 2)
    
    i += 1
    if i == 360:
        i = 0
    time.sleep(0.02747)
    
    pygame.display.flip()
    
