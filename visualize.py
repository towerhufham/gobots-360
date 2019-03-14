from turtle import *

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


def draw_game(game):
    t._tracer(0, 0)

    draw_board()
    for y in range(19):
        for x in range(19):
            state = game.board[x][y]
            if state != 0:
                draw_stone(x, y, state)

    t._update()
    window.exitonclick()

# if __name__ == "__main__":
#     draw_game(None)