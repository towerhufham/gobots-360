from random import choice

class RandomBot:
    def __init__(self):
        self.color = None

    def set_color(self, c):
        self.color = c

    def do_move(self, game):
        moves = game.get_legal_moves()
        if len(moves) > 0:
            placement = choice(moves)
            game.do_move(placement)
            return placement
        else:
            return None
