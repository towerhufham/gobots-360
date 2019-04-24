from go import *
from Connection_Separation import ConnectionBot
from LifeDeathBot import LifeDeathBot
from RandomBot import RandomBot
from Test_strategyV3 import Combination_Bot
from HighLowBot import HighLow_Bot
# Plays Go with two random bots. Outputs the winner of the game when run.
from time import time

class GameGenerator:

    def __init__(self, strategy1, strategy2):
        self.player1 = strategy1
        self.player2 = strategy2


    def play_game(self,game):

        self.player1.set_color(BLACK)
        self.player2.set_color(WHITE)
        play1_last = 0
        play2_last = 0
        while True:
            move1 = self.player1.do_move(game)
            move2 = self.player2.do_move(game)
            if move1 is None and play1_last is None:
                break
            play1_last = move1

            if move2 is None and play2_last is None:
                break

            play2_last = move2

        winner = game.get_winner()

        return winner

    def run_games(self):
        count = 2
        ply1_total = 0
        ply2_total = 0
        Results = {(self.player1.name()):0, self.player2.name():0}
        while count > 0:
            game = GameState()
            winner = self.play_game(game)
            print(winner)
            if winner == 1:
                ply1_total += 1
            else:
                ply2_total += 1
            count -= 1


        count = 2
        player_holder = self.player1

        self.player1 = self.player2
        self.player2 = player_holder

        while count > 0:
            game = GameState()
            winner = self.play_game(game)
            print(winner)
            if winner == 1:
                ply2_total += 1
            else:
                ply1_total += 1
            count -= 1

        Results[self.player1.name()] = ply2_total
        Results[self.player2.name()] = ply1_total

        print(Results)