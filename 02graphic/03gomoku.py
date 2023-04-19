import pygame
BOARD_SZE = 20
SQUARE_SIZE = 30
SQUARE_COLOR = (220, 220, 220)
SQUARE_HOVER_COLOR = (150, 150, 150)

board = []
for y in range(0, BOARD_SZE, 1):
    row = []
    for x in range(0, BOARD_SZE, 1):
        row.append(0)
    board.append(row)
print(board)

current_square = (-1, -1)



window  = pygame.display.set_mode((BOARD_SZE*SQUARE_SIZE,BOARD_SZE*SQUARE_SIZE))


def game_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEMOTION:
            on_mouse_motion(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            on_mouse_down()

def on_mouse_down():
    x, y = current_square
    board[y][x] = 2

def on_mouse_motion(event):
    global current_square
    mx,my = event.pos
    x = mx // SQUARE_SIZE
    y = my // SQUARE_SIZE
    current_square = x,y

def game_update():
    ...


def game_output():
    for y in range(0, BOARD_SZE, 1):
        for x in range(0, BOARD_SZE, 1):
            if current_square == (x, y):
                color = SQUARE_HOVER_COLOR
            else:
                color = SQUARE_COLOR
            pygame.draw.rect(window, color, (x *SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE-1, SQUARE_SIZE-1))
    pygame.display.flip()


while True:
    game_input()
    game_update()
    game_output()