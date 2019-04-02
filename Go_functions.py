from random import choice

#File of useful Go game functions to be used in designing algorithms. If you create a basic function
#that may be useful to others please feel free to add it to this file.



def filter_half(moves, side):
# Takes in a list of legal_moves and a side (l or r) and returns a list of moves that are on
# that side of the board.
    new_moves = []
    if side == 'l':
        for i in moves:
            x, y = i
            if x < 10:
                new_moves.append(i)

        return new_moves

    if side == 'r':
        for i in moves:
            x, y = i
            if x > 10:
                new_moves.append(i)

        return new_moves

def get_middle(moves):
# Takes in a list of legal_moves and returns a list of moves that are on
# the middle line of the board.
    middle_line = []
    for i in moves:
        x, y = i
        if x == 10:
            middle_line.append(i)

    return middle_line

def random_placement(moves, game):
# Takes in a list of legal_moves and a go game object and returns a placement location.
# CURRENTLY MAKES THE PLACEMENT. MAY BE CHANGED LATER

    placement = choice(moves)
    game.do_move(placement)


    return placement

def get_star_point(moves):
# Takes in a list of legal_moves and return a move on a random star point

    star_points = [(3, 3), (3, 9), (3, 15), (9, 3), (9, 9), (9, 15),
                   (15, 3), (15, 9), (15, 15)]
    for i in star_points:
        if i not in moves:
            star_points.pop(star_points.index(i))
    placement = choice(star_points)

    return placement


def find_connection(moves, game, color):
# takes in a list of legal_moves and a Go game object. Returns
# a list of moves that are connected to other pieces.

    connected = []
    if color == 1:
        for i in moves:
            liberties = []
            x, y = i
            liberty_1 = (x + 1, y)
            liberties.append(liberty_1)
            liberty_2 = (x - 1, y)
            liberties.append(liberty_2)
            liberty_3 = (x, y + 1)
            liberties.append(liberty_3)
            liberty_4 = (x, y - 1)
            liberties.append(liberty_4)
            for l in liberties:
                x1, y1 = l
                if x1 < 19 and x1 > 0 and y1 < 19 and y1 > 0:
                    if game.board[x1, y1] == 1:
                        connected.append(i)
    else:
        for i in moves:
            liberties = []
            x, y = i
            liberty_1 = (x + 1, y)
            liberties.append(liberty_1)
            liberty_2 = (x - 1, y)
            liberties.append(liberty_2)
            liberty_3 = (x, y + 1)
            liberties.append(liberty_3)
            liberty_4 = (x, y - 1)
            liberties.append(liberty_4)
            for l in liberties:
                x1, y1 = l
                if x1 < 19 and x1 > 0 and y1 < 19 and y1 > 0:
                    if game.board[x1, y1] == -1:
                        connected.append(i)

    if len(connected) != 0:
        return connected
    else:
        return None