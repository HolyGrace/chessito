from pygame import *
from board import *
import pygame
import math

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

COLOR_BOARD1 = (0, 0, 0)
COLOR_BOARD2 = (255, 255, 255)

CELL_SPACE = int(SCREEN_WIDTH/8)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load chess pieces
wp = pygame.image.load('src\pieces\white_pawn.png')

# Resize pieces
wp = pygame.transform.scale(wp , (CELL_SPACE, CELL_SPACE))
           
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # Recolector of the mouse click information
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            x, y = mouse.get_pos()
            print(x, y)
            SCEL_X, SCEL_Y = math.trunc(x/CELL_SPACE), math.trunc(y/CELL_SPACE)
            print(SCEL_X, SCEL_Y)


    display_board(screen, SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SPACE, COLOR_BOARD1, COLOR_BOARD2)
    # Show the board
    screen.blit(wp, (0, 0))
    pygame.display.flip()


pygame.quit()