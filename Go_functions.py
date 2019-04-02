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