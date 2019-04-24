from FinalGameGenerator import GameGenerator
from Connection_Separation import ConnectionBot
from LifeDeathBot import LifeDeathBot
from RandomBot import RandomBot

Tester = GameGenerator(LifeDeathBot(),ConnectionBot())
Tester.run_games()