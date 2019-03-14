import graphics


CELL_SIZE = 32
MARGIN = CELL_SIZE//2

def draw(game):
	#currently hardcoded to 19x19 boards
	#it draws the board both rotated and flipped (somehow)
	#that doesn't change the anything about the score or game geometry, so it should be fine
	win = graphics.GraphWin("Go results", 19 * CELL_SIZE, 19 * CELL_SIZE)
	win.setBackground('goldenrod')
	bg = graphics.Rectangle(graphics.Point(0, 0), graphics.Point(19*CELL_SIZE, 19*CELL_SIZE))
	bg.setFill(graphics.color_rgb(247, 164, 64))

	
	for y in range(19):
		for x in range(19):
			if game.board[x][y] != 0:
			
				cx = (CELL_SIZE*x) + MARGIN
				cy = (CELL_SIZE*y) + MARGIN
				stone = graphics.Circle(graphics.Point(cx, cy), 16)
				
				if game.board[x][y] == -1:
					stone.setFill("white")
				elif game.board[x][y] == 1:
					stone.setFill("black")
				else:
					print("idk man")
					
				stone.draw(win)



	win.getMouse()