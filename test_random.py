from go import *
import csv
#from visualize import animate_game, draw_game
from RandomBot import RandomBot
from Test_strategyV1 import RandomBot2
# Plays Go with two random bots. Outputs the winner of the game when run.

def play_game(player1, player2, game, debug=False):
    player1.set_color(BLACK)
    player2.set_color(WHITE)
    while True:
        move1 = player1.do_move(game)
        if move1 is None:
            move2 = player2.do_move(game)
            if move2 is None:
                break

        move2 = player2.do_move(game)
        if move1 is None and move2 is None:
            break

    winner = game.get_winner()
    if winner == 1:
        return('black')
    else:
        return('white')
    #draw_game(game)
    #animate_game(game)

def main():

    wht_total = 0
    blk_total = 0
    count = 100
    while count > 0:
        game = GameState()
        player1 = RandomBot2()
        player2 = RandomBot()
        winner = play_game(player1, player2, game)
        print(winner)
        if winner == 'black':
            blk_total +=1
        else:
            wht_total +=1
        count -=1
    print('Black: '+str(blk_total))
    print('White: '+str(wht_total))


if __name__ == '__main__':
    main()