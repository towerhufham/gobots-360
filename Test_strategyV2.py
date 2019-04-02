from random import choice

class Connection_Bot:
    def __init__(self, move_count=0):
        self.color = None
        self.move_count = move_count
        sides = ['l','r']
        self.L_R = choice(sides)
        self.star_points = [(3,3),(3,9),(3,15),(9,3),(9,9),(9,15),(15,3),(15,9),(15,15)]
        self.start_flag = 0
    def set_color(self, c):
        self.color = c

    def do_move(self, game):
        moves = game.get_legal_moves()
        if len(moves) != 0:
            for move in moves:
                if game.is_suicide == True:
                    moves.pop(moves.index(move))
            if self.start_flag == 0:
                placement = self.get_start_point(moves)
                self.start_flag = 1
                game.do_move(placement)
                self.move_count +=1
                return placement

            else:
                placement = self.find_connection(moves,game)
                if placement != None and self.move_count % 20 != 0:
                    game.do_move(placement)
                    self.move_count+=1
                    return placement
                else:
                    placement = self.random_placement(moves, game)
                    return placement

        else:
            return None
    def random_placement(self,moves, game):
        placement = choice(moves)
        game.do_move(placement)
        self.move_count += 1
        return placement

    def get_start_point(self,moves):

        for i in self.star_points:
            if i not in moves:
                self.star_points.pop(self.star_points.index(i))
        placement = choice(self.star_points)

        return placement

    def find_connection(self,moves,game):
        connected = []
        if self.color == 1:
         for i in moves:
            liberties = []
            x,y = i
            liberty_1 = (x+1,y)
            liberties.append(liberty_1)
            liberty_2 = (x-1,y)
            liberties.append(liberty_2)
            liberty_3 = (x,y+1)
            liberties.append(liberty_3)
            liberty_4 = (x,y-1)
            liberties.append(liberty_4)
            for l in liberties:
                x1,y1 = l
                if x1 < 19 and x1>0 and y1 < 19 and y1>0:
                    if game.board[x1,y1] == 1:
                            connected.append(i)
        else:
         for i in moves:
            liberties = []
            x,y = i
            liberty_1 = (x+1,y)
            liberties.append(liberty_1)
            liberty_2 = (x-1,y)
            liberties.append(liberty_2)
            liberty_3 = (x,y+1)
            liberties.append(liberty_3)
            liberty_4 = (x,y-1)
            liberties.append(liberty_4)
            for l in liberties:
                x1,y1 = l
                if x1 < 19 and x1>0 and y1 < 19 and y1>0:
                    if game.board[x1,y1] == -1:
                            connected.append(i)

        if len(connected) != 0:
            placement = choice(connected)
            return placement
        else:
            return None




