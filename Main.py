from go import *
from visualize import animate_game, draw_game
from RandomBot import RandomBot
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
    animate_game(game)

def main():
    game = GameState()
    player1 = RandomBot()
    player2 = RandomBot()
    play_game(player1, player2, game)

if __name__ == '__main__':
    main()
