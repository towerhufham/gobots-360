from go import *
from visualize import animate_game, draw_game
from HighLowBot import HighLow_Bot
from RandomBot import RandomBot
from Test_strategyV3 import Combination_Bot
from LifeDeathBot import LifeDeathBot
from Connection_Separation import ConnectionBot
# Plays Go with two random bots. Outputs the winner of the game when run.

def play_game(player1, player2, game, debug=False):
    player1.set_color(BLACK)
    player2.set_color(WHITE)
    play1_last = 0
    play2_last = 0
    while True:
        move1 = player1.do_move(game)
        move2 = player2.do_move(game)
        if move1 is None and play1_last is None:
            break
        play1_last = move1

        if move2 is None and play2_last is None:
            break

        play2_last = move2

    winner = game.get_winner()
    if winner == 1:
        print('Black wins')
    else:
        print('White wins')
    #draw_game(game)
    animate_game(game, step_through=False)

def main():
    game = GameState()
    player1 = RandomBot()
    player2 = ConnectionBot()
    play_game(player1, player2, game)

if __name__ == '__main__':
    main()
