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
            high_moves = self.pref_high(moves)
            low_moves = self.pref_low(moves)
            if len(high_moves) != 0 and self.move_count % 2 == 0:   ## counts moves to switch between high/low
                placement = choice(high_moves)                      ## starts with high moves, plays high on even
                self.move_count+=1
                game.do_move(placement)
                return placement
            else:
                if len(low_moves)!= 0:                              ## plays low on odd
                    placement = choice(low_moves)
                    self.move_count+=1
                    game.do_move(placement)
                    return placement
                else:
                    middle_moves = self.get_middle(moves)
                    my_half = self.filter_half(moves)
                    if len(middle_moves) != 0:                     ## if preferred high/low moves are gone, goes middle
                        placement = choice(middle_moves)
                        game.do_move(placement)
                    else:
                        if len(my_half) != 0:                      ## tries to fill in its own half if middle not avail
                            placement = choice(my_half)
                            game.do_move(placement)
                        else:
                            placement = choice(moves)              ## doesn't care when no preferred choices are avail
                            game.do_move(placement)
                    return placement
        else:
            return None

    def filter_half(self, moves):                    ## gets left and right half
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

    def get_middle(self,moves):             ## gets middle line
        middle_line = []
        for i in moves:
            x,y = i
            if x == 10:
                middle_line.append(i)
        return middle_line

    def pref_low(self, moves):
        lows = []
        if self.L_R == 'l':                     ## returns bottom half of board between x=0, x=3, y=9
            for i in moves:                     ## and x=4, x=15, y=3
                x,y = i
                if x<4:                 ## and x=15, x=18, y=9
                    lows.append(i)
                if 3 < x < 10:
                    if 0 <= y < 4 or 15 <= y < 19:
                        lows.append(i)
            return lows

        if self.L_R == 'r':                     ## returns top half of board between x=0, x=3, y=10
            for i in moves:                     ## and x=4, x=15, y=15
                x,y = i
                if 8 < x < 16:                 ## and x=15, x=18, y=10
                    if 0 <= y < 4 or 15 <= y < 19:
                        lows.append(i)
                if x>15:
                    lows.append(i)
            return lows

    def pref_high(self, moves):         ## returns center block between x=6, x=12, y=12
        highs = []
        for i in moves:
            x,y = i
            if x<13 or x>5:
                if 6 <= y < 13:
                    highs.append(i)
            return highs
