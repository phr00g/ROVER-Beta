from classes import *
from locations import *
from methods import *
import random

import pygame
import time
import threading
from lang import *




def pygo():
    pygame.init()
    clock = pygame.time.Clock()

    # Set the dimensions of the window
    window_width = 475
    window_height = 535
    tile_size = 50
    space_size = 10

    # Define colors
    WHITE = (247, 255, 247)
    RED = (255, 107, 107)
    BLUE = (78, 205, 196)
    BLACK = (102, 78, 76)

    # Create a Pygame window
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("ROVER Map Grid")
    clock = pygame.time.Clock()
    running = True
    window.fill(BLACK)

    blink_interval = 2.0  # 1 second interval for blinking
    is_blinking = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for x in range(len(map_array)):
            for y in range(len(map_array[0])):
                tile = map_array[x][y]
                rect = pygame.Rect(x * (tile_size + space_size), y * (tile_size + space_size), tile_size, tile_size)

                if tile == me.location:
                    current_time = time.time()
                    if current_time % blink_interval < blink_interval / 2:
                        pygame.draw.rect(window, RED, rect)
                    else:
                        pygame.draw.rect(window, BLUE, rect)
                else:
                    pygame.draw.rect(window, WHITE, rect)

        pygame.display.update()
        clock.tick(60)
    

pygothread = threading.Thread(target=pygo)
pygothread.daemon = True
pygothread.start()