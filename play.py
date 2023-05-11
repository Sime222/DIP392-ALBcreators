from board import *
import numpy as np
import pygame
import math

board = create_board()
print_board(board)
game_over = False
turn = 0

# initalize pygame
pygame.init()

# define our screen size
SQUARESIZE = 100

# define width and height of board
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE / 2 - 5)

screen = pygame.display.set_mode(size)
# Calling function draw_board again
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)

def get_font(size):
    return pygame.font.SysFont('comicsans', size)




BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()


def play():
    player1=0
    player2=0
    board = create_board()
    print_board(board)
    game_over = False
    turn = 0

    #initalize pygame
    pygame.init()

    #define our screen size
    SQUARESIZE = 100

    #define width and height of board
    width = COLUMN_COUNT * SQUARESIZE
    height = (ROW_COUNT+1) * SQUARESIZE

    size = (width, height)

    RADIUS = int(SQUARESIZE/2 - 5)

    screen = pygame.display.set_mode(size)
    #Calling function draw_board again
    draw_board(board)
    pygame.display.update()

    myfont = pygame.font.SysFont("monospace", 75)



    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.MOUSEMOTION:

                pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
                posx = event.pos[0]
                draw_points(1, player1, (0, 0),RED)
                draw_points(2, player2, (600, 0),YELLOW)
                if turn == 0:
                    pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
                else:
                    pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
                print(event.pos)
                # Ask for Player 1 Input
                if turn == 0:
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 1)

                        if winning_move(board, 1)==True:
                            player1+=10
                            if player1==20:
                                player1 = 0
                                player2 = 0
                                label = myfont.render("Player 1 wins!!", 1, RED)
                                screen.blit(label, (40,10))
                                pygame.display.update()
                                pygame.time.wait(3000)
                                return
                            elif board_full(board):

                                player1 += 5
                                player2 += 5

                                reset_board(board)
                            else:
                                reset_board(board)



                # # Ask for Player 2 Input
                else:
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 2)

                        if winning_move(board, 2):
                            player2+=10
                            if player2 ==20:
                                player1=0
                                player2=0
                                label = myfont.render("Player 2 wins!!", 1, YELLOW)
                                screen.blit(label, (40,10))
                                pygame.display.update()
                                pygame.time.wait(3000)
                                return
                            elif board_full(board):

                                player1 += 5
                                player2 += 5

                                reset_board(board)
                            else:
                                reset_board(board)




                print_board(board)
                draw_board(board)




                turn += 1
                turn = turn % 2
                pygame.display.update()







def draw_points(n, points,pos,color):
    PROV = get_font(20).render(f'player{n}={points}', 1, color)
    screen.blit(PROV, pos)




def reset_board(board):
    # Set all cells to 0
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT):
            board[r][c] = 0





def board_full(board):
    for row in board:
        if 0 in row:
            return False
    return True
