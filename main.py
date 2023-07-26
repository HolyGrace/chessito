from pygame import *
from board import board
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

# Variable COLOR to identify when the board must show "COLOR_BOARD1" or "COLOR_BOARD2"
    COLOR=0
# Creation of the table board
    # For clicle of the matrix
    for i in range(0, SCREEN_WIDTH, CELL_SPACE):
        for j in range(0, SCREEN_HEIGHT, CELL_SPACE):
            if COLOR % 2 == 0 :
                # Creation of the color cel 1
                pygame.draw.rect(screen, COLOR_BOARD1, [i, j, CELL_SPACE, CELL_SPACE])
            else:
                # Creation of the color cel 2
                pygame.draw.rect(screen, COLOR_BOARD2, [i, j, CELL_SPACE, CELL_SPACE])
            COLOR += 1
        COLOR += 1

    # Show the board
    screen.blit(wp, (0, 0))
    pygame.display.flip()


pygame.quit()