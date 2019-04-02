from random import choice

class HighLow_Bot:
    def __init__(self, move_count=0):
        self.color = None
        self.move_count = move_count
        sides = ['l','r']
        self.L_R = choice(sides)

    def set_color(self, c):
        self.color = c

    def do_move(self, game):
        moves = game.get_legal_moves()
        if len(moves) != 0:
            left_half = self.filter_half(moves)
            middle_line = self.get_middle(moves)
            if len(middle_line) != 0:
                placement = choice(middle_line)
                game.do_move(placement)
                return placement
            else:
                if len(left_half)!= 0:
                    placement = choice(left_half)
                    game.do_move(placement)
                    return placement
                else:
                    placement = choice(moves)
                    game.do_move(placement)
                    return placement

        else:
            return None
    def filter_half(self, moves):
        new_moves = []
        if self.L_R == 'l':
            for i in moves:
                x,y = i
                if x<10:
                    new_moves.append(i)
            return new_moves

        if self.L_R == 'r':
            for i in moves:
                x,y = i
                if x>10:
                    new_moves.append(i)
            return new_moves

    def get_middle(self,moves):
        middle_line = []
        for i in moves:
            x,y = i
            if x == 10:
                middle_line.append(i)
        return middle_line