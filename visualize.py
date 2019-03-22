from turtle import *
from time import sleep

window = Screen()
window.setup(640, 640)
window.setworldcoordinates(0, 616, 616, 0)
window.bgcolor("#dcb35c")
t = Turtle()
t.hideturtle()
# t.speed(0)

def draw_board():
    # horizontal lines
    t.seth(0)
    for i in range(20):
        t.penup()
        t.setx(16)
        t.sety(i*32+16)
        t.pendown()
        t.forward(576)

    # vertical lines
    t.seth(90)
    for i in range(20):
        t.penup()
        t.setx(i*32+16)
        t.sety(16)
        t.pendown()
        t.forward(576)

    # star points
    draw_starpoint(3, 3)
    draw_starpoint(3, 9)
    draw_starpoint(3, 15)
    draw_starpoint(9, 3)
    draw_starpoint(9, 9)
    draw_starpoint(9, 15)
    draw_starpoint(15, 3)
    draw_starpoint(15, 9)
    draw_starpoint(15, 15)

def draw_starpoint(x, y):
    t.penup()
    t.setx(x*32+16)
    t.sety(y*32+16)
    t.pendown()
    t.dot(6)

def draw_stone(x, y, color):
    t.penup()
    t.setx(x*32+16)
    t.sety(y*32+16)
    t.pendown()
    if color == -1:
        t.dot(32, "#ffffff")
    elif color == +1:
        t.dot(32, "#000000")

def remove_stone(x, y):
    #write over stone shape with background color
    t.penup()
    t.setx(x * 32 + 16)
    t.sety(y * 32 + 16)
    t.pendown()
    t.dot(33, "#dcb35c")
    #redraw grid segment
    #vertical line
    t.penup()
    t.setx(x * 32 - 1)
    t.sety(y * 32 + 16)
    t.seth(0)
    t.pendown()
    t.forward(33)
    #horizontal line
    t.penup()
    t.setx(x * 32 + 16)
    t.sety(y * 32 - 1)
    t.seth(90)
    t.pendown()
    t.forward(33)

def draw_state(board):
    draw_board()
    for y in range(19):
        for x in range(19):
            state = board[x][y]
            if state != 0:
                draw_stone(x, y, state)

def draw_game(game):
    window.tracer(0,0)
    draw_state(game.board)
    window.update()
    window.exitonclick()

def update_state(board, previousboard):
    for y in range(19):
        for x in range(19):

            if board[x][y] != previousboard[x][y]:
                #remove stone
                if board[x][y] == 0:
                    remove_stone(x, y)
                else:
                    # draw new stone
                    draw_stone(x, y, board[x][y])


def animate_game(game, delay=False):
    window.tracer(0, 0)
    firstboard = True
    previousboard = None
    for board in game.boardhistory:
        if firstboard:
            draw_state(board)
            firstboard = False
        else:
            update_state(board, previousboard)
        previousboard = board
        window.update()
        if delay is not False:
            sleep(delay)
    window.exitonclick()
