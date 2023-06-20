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

    letters = ['a', 'b', 'c', 'd', 'e', 'f','g','h','i']
    # Define the numbers to display
    numbers = list(range(1, 9))


    # Font settings
    font_size = 24
    vertical_gap = 36
    horizontal_gap = 36
    pygame.font.init()
    font = pygame.font.SysFont(None, font_size)


    # Set the dimensions of the window
    window_width = 550
    window_height = 600
    tile_size = 50
    space_size = 10

    # Define colors
    WHITE = (204, 201, 220)
    RED = (251, 54, 64)
    BLUE = (0, 121, 145)
    BLACK = (0, 0, 0)
    GREEN = (32, 191, 85)

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


            total_height = (len(letters) * font.get_height()) + ((len(letters) - 1) * vertical_gap)
            # Calculate the total width of the numbers row
            total_width = (len(numbers) * font_size) + ((len(numbers) - 1) * horizontal_gap)

            start_y = (window_height - total_height) // 2 - 10
            start_x = (window_width - total_width) // 2 + 15

            # Render and display the letters
            for idx, letter in enumerate(letters):
                text = font.render(letter, True, pygame.Color(WHITE))
                #first arg is x loc of column of letters
                text_rect = text.get_rect(center=(window_width // 15, start_y + (idx * (font_size + vertical_gap))))
                window.blit(text, text_rect)


            #render and display numbers
            for idx, number in enumerate(numbers):
                text = font.render(str(number), True, pygame.Color(WHITE))
                text_rect = text.get_rect(topleft=(start_x + (idx * (font_size + horizontal_gap)), window_height // 22))
                window.blit(text, text_rect)





            

            




        
        #for xi in length of row in map array
        for x in range(len(map_array)):
            #for y in length of col in map array
            for y in range(len(map_array[0])):
                tile = map_array[x][y]
                #add to first arg to move entire grid to right and second to move entire grid left?
                rect = pygame.Rect(x * (tile_size + space_size) + 50, y * (tile_size + space_size) + 50, tile_size, tile_size)

                if tile == me.location:
                    current_time = time.time()
                    if current_time % blink_interval < blink_interval / 2:
                        pygame.draw.rect(window, RED, rect)
                    else:
                        pygame.draw.rect(window, BLUE, rect)
                elif tile.success == True:
                    pygame.draw.rect(window, GREEN, rect)
                else:
                    pygame.draw.rect(window, WHITE, rect)

        pygame.display.update()
        clock.tick(60)
    

pygothread = threading.Thread(target=pygo)
pygothread.daemon = True
pygothread.start()