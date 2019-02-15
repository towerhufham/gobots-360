from go import *
from random import choice
from draw_board import draw

def random_move(game):
	moves = game.get_legal_moves()
	game.do_move(choice(moves))

game = GameState()
for i in range(50):
	random_move(game)
	random_move(game)
print(game.board)
print(game.get_winner())
draw(game)