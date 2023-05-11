
from MinMax_implemetation import *

WIDTH = 800
HIGHT = 700
BLACK = (0, 0, 0)

def get_font(size):
    return pygame.font.SysFont('comicsans', size)

ROW_COUNT = 6
COLUMN_COUNT = 7

pygame.init()  # initialize Pygame modules, including the font module

screen = pygame.display.set_mode((WIDTH, HIGHT))
pygame.display.set_caption("Connect-4")

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




def play_ai():
    board = create_board()
    print_board(board)
    game_over = False
    player1=0
    player2=0

    pygame.init()

    SQUARESIZE = 100

    width = COLUMN_COUNT * SQUARESIZE
    height = (ROW_COUNT + 1) * SQUARESIZE

    size = (width, height)

    RADIUS = int(SQUARESIZE / 2 - 5)

    screen = pygame.display.set_mode(size)
    draw_board(board)
    pygame.display.update()

    myfont = pygame.font.SysFont("monospace", 75)

    turn = random.randint(PLAYER, AI)

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                posx = event.pos[0]
                draw_points(1, player1, (0, 0), RED)
                draw_points(2, player2, (600, 0), YELLOW)
                if turn == PLAYER:
                    pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)

            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                # print(event.pos)
                # Ask for Player 1 Input
                if turn == PLAYER:
                    posx = event.pos[0]
                    col = int(math.floor(posx / SQUARESIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, PLAYER_PIECE)

                        if winning_move(board, PLAYER_PIECE):

                            player1 += 10
                            if player1 == 20:
                                player1 = 0
                                player2 = 0
                                label = myfont.render("Player 1 wins!!", 1, RED)
                                screen.blit(label, (40, 10))
                                pygame.display.update()
                                pygame.time.wait(3000)
                                return

                            else:
                                reset_board(board)

                        turn += 1
                        turn = turn % 2

                        print_board(board)
                        draw_board(board)

        # # Ask for Player 2 Input
        if turn == AI and not game_over:

            # col = random.randint(0, COLUMN_COUNT-1)
            # col = pick_best_move(board, AI_PIECE)
            pygame.time.wait(300)
            col, minimax_score = minimax(board, 3, -math.inf, math.inf, True)

            if is_valid_location(board, col):
                # pygame.time.wait(500)
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, AI_PIECE)

                if winning_move(board, AI_PIECE):

                    player2 += 10
                    if player2 == 20:
                        player1 = 0
                        player2 = 0
                        label = myfont.render("Player 2 wins!!", 1, YELLOW)
                        screen.blit(label, (40, 10))
                        pygame.display.update()
                        pygame.time.wait(3000)
                        return
                    else:
                        reset_board(board)

                print_board(board)
                draw_board(board)

                turn += 1
                turn = turn % 2


def reset_board(board):
    # Set all cells to 0
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT):
            board[r][c] = 0


def draw_points(n, points,pos,color):
    PROV = get_font(20).render(f'player{n}={points}', 1, color)
    screen.blit(PROV, pos)
