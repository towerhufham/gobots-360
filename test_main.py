from go import *
from visualize import animate_game, draw_game
from Test_strategyV1 import HighLow_Bot
from Test_strategyV2 import Connection_Bot
from RandomBot import RandomBot
from Test_strategyV3 import Combination_Bot
# Plays Go with two random bots. Outputs the winner of the game when run.

def play_game(player1, player2, game, debug=False):
    player1.set_color(BLACK)
    player2.set_color(WHITE)
    while True:
        move1 = player1.do_move(game)
        if move1 is None and move2 is None:
            break
        move2 = player2.do_move(game)
        if move1 is None and move2 is None:
            break

    winner = game.get_winner()
    if winner == 1:
        print('Black wins')
    else:
        print('White wins')
    #draw_game(game)
    animate_game(game,step_through=False)

def main():
    game = GameState()
    player1 = Combination_Bot()
    player2 = Connection_Bot()
    play_game(player1, player2, game)

if __name__ == '__main__':
    main()