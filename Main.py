from go import *
from draw_board import draw
from Random_bot import random_bot
# Plays Go with two random bots. Outputs the winner of the game when run.
# Uncomment line 19 to see the board. Currently does not remove captured pieces
# so the board will look strange.


def play_game(player1, player2, game):
    while len(game.get_legal_moves())>0:
        move_p1 = player1.get_move(game)

        move_p2 = player2.get_move(game)

    winner = game.get_winner()
    if winner == 1:
        print('Player 1 wins')
    else:
        print('Player 2 wins')
    #draw(game)

def main():
    game = GameState()
    player1 = random_bot('player 1')
    player2 = random_bot('player 2')

    play_game(player1, player2, game)

if __name__ == '__main__':
    main()