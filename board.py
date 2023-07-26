import numpy
import pygame
board = [['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR'],
         ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],
         [None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None],
         ['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],
         ['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR']]

def display_board(screen, SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SPACE, COLOR_BOARD1, COLOR_BOARD2):

    # Variable COLOR to identify when the board must show "COLOR_BOARD1" or "COLOR_BOARD2"
    COLOR = 0

    # Creation of the table board
    # For clicle of the matrix
    for i in range(0, SCREEN_WIDTH, CELL_SPACE):
        for j in range(0, SCREEN_HEIGHT, CELL_SPACE):
            if COLOR % 2 == 0:
                # Creation of the color cel 1
                pygame.draw.rect(screen, COLOR_BOARD2, [i, j, CELL_SPACE, CELL_SPACE])
            else:
                # Creation of the color cel 2
                pygame.draw.rect(screen, COLOR_BOARD1, [i, j, CELL_SPACE, CELL_SPACE])
            COLOR += 1
        COLOR += 1

def display_pieces(screen, CELL_SPACE):
    for i in range(8):
        for j in range(8):
            if board[i][j] != None:
                piece = board[i][j]
                owo = pygame.image.load(f'src\pieces\{piece}.png')
                uwu = pygame.transform.scale(owo , (CELL_SPACE, CELL_SPACE))
                screen.blit(uwu, (j*CELL_SPACE, i*CELL_SPACE))


