from person import *
from board import *

class bomb(Person):
	def __init__(self,x,y,board):
		Person.__init__(self,x,y)	
		self.tic=0;

	#Handles ticking and explosion of the bomb.
	def tick(self,board):
		if not self.tick==-1:
			self.tic+=1
			pos=self.get_position()
			x=pos[0]
			y=pos[1]
			if self.tic==2:
				board.board[x][y]='3'
			if self.tic==3:
				board.board[x][y]='2'	
			if self.tic==4:
				board.board[x][y]='1'
				if not board.board[x-1][y]=='\033[1;45mX\033[1;m':
					board.board[x-1][y]='\033[1;35me\033[1;m'

				if not board.board[x][y-1]=='\033[1;45mX\033[1;m':
					board.board[x][y-1]='\033[1;35me\033[1;m'

				if not board.board[x+1][y]=='\033[1;45mX\033[1;m':
					board.board[x+1][y]='\033[1;35me\033[1;m'

				if not board.board[x][y+1]=='\033[1;45mX\033[1;m':
					board.board[x][y+1]='\033[1;35me\033[1;m'

			elif self.tic==5:
				board.board[x][y]='5'
				if not board.board[x-1][y]=='\033[1;45mX\033[1;m':
					board.board[x-1][y]=' '

				if not board.board[x][y-1]=='\033[1;45mX\033[1;m':
					board.board[x][y-1]=' '

				if not board.board[x+1][y]=='\033[1;45mX\033[1;m':
					board.board[x+1][y]=' '

				if not board.board[x][y+1]=='\033[1;45mX\033[1;m':
					board.board[x][y+1]=' '	
				board.board[x][y]=' '
				self.tic=-1

	#gives the time for which the bomb has been ticking.
	def get_tic(self):
		return self.tic			




