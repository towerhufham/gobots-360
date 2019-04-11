from Go_functions import *


class ConnectionBot:

    def __init__(self, move_count=0):
        self.color = None
        self.move_count = move_count
        self.star_points = [(3, 3), (3, 9), (3, 15), (9, 3), (9, 9), (9, 15), (15, 3), (15, 9), (15, 15)]
        self.start_flag = 0  # flag used to determine if the first piece has already been placed
        self.separation_flag = -1  # flag used by the algorithm to determine if it should be in sep or conn mode

    def set_color(self, c):
        # sets the color of the player
        self.color = c

    def do_move(self, game):
        # updates the game object with the chosen move
        # calls the helper function self.get_move to get the placement
        placement = self.get_move(game)
        self.move_count += 1  # updates the move count
        game.do_move(placement)

    def get_move(self, game):
        # Helper function for get move. Checks several flags to determine
        # the flow of the program. returns a placement

        raw_moves = game.get_legal_moves()
        moves = self.remove_eyes(raw_moves, game)

        if len(moves) != 0:
            if self.start_flag == 0:
                placement = self.do_start(moves)
                return placement
            else:
                placement = self.execute_strategy(moves, game)
                return placement
        else:
            return None

    def execute_strategy(self, moves, game):
        # runs connections and separation and returns either a move connected
        # to the player or a moved connected to the opponent's pieces.

        connections = find_connection(moves, game, self.color)
        if connections is not None and self.separation_flag == -1:
            placement = choice(connections)
            if self.move_count % 5 == 0:  # check to see number of connecting placements has been reached
                self.separation_flag *= -1  # flips flag to indicate separation placements should occur.
            return placement
        else:
            placement = self.separation(moves, game)
            if self.move_count % 10 == 0:  # check to see number of separation placements has been reached
                self.separation_flag *= -1  # flips flag to indicate connection placements should occur.
            return placement

    def remove_eyes(self, moves, game):
        # Removes all the positions that are eyes from legal_moves and return an eye free list of moves
        new_moves = moves
        for move in new_moves:
            if game.is_eye(move, self.color) is True:
                new_moves.pop(new_moves.index(move))
        return new_moves

    def do_start(self, moves):
        # calls helper function to find a start point then flips the start flag
            placement = self.get_start_point(moves)
            self.start_flag = 1
            return placement

    def separation(self, moves, game):
        # calls helper function find_connection() to find all the placements that are connected to the
        # opponents pieces. If there are no possible placements that are connected to the opponents pieces then
        # find_connection is called again to find all possible placements that connected to the player's pieces.
        # if there are no pieces connected to the player's pieces then a placement is chosen randomly
        if self.color == 1:  # check to identify player color
            opponent_color = -1
        else:
            opponent_color = 1

        opponent_connections = find_connection(moves, game, opponent_color)

        if opponent_connections is None:  # check to see if there are placements connected to opponent
            connections = find_connection(moves, game, self.color)
            if connections is None:  # check to see if there are placements connect to the player
                placement = choice(moves)  # random placement if check fails
            else:
                placement = choice(connections)
        else:
            placement = choice(opponent_connections)
        return placement

    def get_start_point(self, moves):
        # iterates through the list of star points and removes any that are not open then picks one randomly
        # and returns that placement.

        for i in self.star_points:
            if i not in moves:
                self.star_points.pop(self.star_points.index(i))
        placement = choice(self.star_points)
        return placement
