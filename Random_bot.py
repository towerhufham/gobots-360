from go import *
from random import choice

class random_bot:

    def __init__(self,player):
        self.player = player

    def get_move(self, game):

        moves = game.get_legal_moves()
        print('')
        if len(moves) != 0:
            placement = choice(moves)
            game.do_move(placement)
            return placement
        else:
            return None

