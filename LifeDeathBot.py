from random import choice

class LifeDeathBot:
    def __init__(self):
        self.color = None
        self.currentHome = None
        self.piecesLeft = None
        self.eyes = []

    def set_color(self, c):
        self.color = c

    def getBlockPieces(self, home, board):
        #blocks are unkillable structures made with as few stones as possible
        #they are shaped like this:
        # axaxa
        # x x x
        # axaxa
        #x's are where stones MUST go
        #up to one "a" may be omitted
        #the middle x is the "home"
        #TODO: implement a's
        allpieces = [
            (-2,-1), (-1, -1), (0, -1), (1, -1), (2, -1), #top row
            (-2, 0), (0, 0), (2, 0), #middle row
            (-2, 1), (-1, 1), (0, 1), (1, 1), (2, 1) #bottom row
        ]
        #if any of those spaces are already filled, skip them
        pieces = []
        hx, hy = home
        for p in allpieces:
            x, y = p
            if board[hx+x][hy+y] == 0:
                pieces.append(p)
        return pieces

    def chooseNextPiece(self):
        p = choice(self.piecesLeft)
        self.piecesLeft.remove(p)
        rx, ry = p
        hx, hy = self.currentHome
        return (hx+rx, hy+ry)

    def isValidHome(self, home, board):
        #if there are no enemy in the size of the block, it is valid
        #TODO: make this include "a" stuff
        hx, hy = home
        #make sure all points in board
        if hx - 2 < 0 or hx + 2 > 18 or hy - 1 < 0 or hy + 1 > 18:
            return False
        #make sure eyes aren't filled
        if board[hx-1][hy] != 0 or board[hx+1][hy] != 0:
            return False
        #make sure there are no enemy stones within the bounds
        #(+1's to make inclusive)
        for y in range(-1, 1+1):
            for x in range(-2, 2+1):
                stone = board[x+hx][y+hy]
                if stone != 0 and stone != self.color:
                    return False
        return True

    def findNewHome(self, moves, board):
        #the name of this function makes me feel sad :(
        #try 20 times to find a home, if not go to default behavior
        for i in range(20):
            home = choice(moves)
            if self.isValidHome(home, board):
                return home
        return None

    def setNewHome(self, home, board):
        self.currentHome = home
        self.piecesLeft = self.getBlockPieces(home, board)
        hx, hy = home
        self.eyes.append((hx-1, hy))
        self.eyes.append((hx+1, hy))

    def doRandomMove(self, game, moves):
        placement = choice(moves)
        game.do_move(placement)
        return placement

    def do_move(self, game):
        #Turn Flow:
        #If currently working on "block":
        #   If current block is not threatened:
        #       Determine where to put next piece in block
        #   If current block is threatened:
        #       Make new block
        #If not working on block:
        #   Choose random point within bounds to start

        # import pdb;pdb.set_trace()

        moves = game.get_legal_moves()
        #remove eyes because they never need to be filled in
        for e in self.eyes:
            if e in moves:
                moves.remove(e)
        #if there's nothing to do, pass
        if len(moves) < 1:
            return None
        #first, if we have a home and it isn't valid anymore, forget it
        if self.currentHome is not None:
            if not self.isValidHome(self.currentHome, game.board):
                self.currentHome = None
                self.piecesLeft = None
        #if we have no home, try to find one
        if self.currentHome is None or len(self.piecesLeft) <= 0 :
            newhome = self.findNewHome(moves, game.board)
            if newhome is None:
                #fallback to random moves
                return self.doRandomMove(game, moves)
            else:
                self.setNewHome(newhome, game.board)
        #if we have pieces left...
        if len(self.piecesLeft) > 0:
            placement = self.chooseNextPiece()
            game.do_move(placement)
            return placement
        #if not, that means we're doing random placement (because it gets checked earlier)
        else:
            #fallback to random moves
            return self.doRandomMove(game, moves)
