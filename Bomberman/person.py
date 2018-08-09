from obj import *
from board import *

class Person(Object):
	def __init__(self,x,y):
		Object.__init__(self,x,y)

	def remove(self,board,x_remove,y_remove):
		board.board[x_remove][y_remove]=' '	

	def delete(self,board):
		pos=self.get_position()
		x=pos[0]
		y=pos[1]
		self.remove(board,x,y)

	#Checks what exists at particular coordinates on a keyboard.
	def checkspace(self,board,x,y):
		if board.board[x][y]==' ':
			return 1
		elif board.board[x][y]=='\033[1;45mX\033[1;m' or board.board[x][y]=='\033[1;47m#\033[1;m':
			return 2
		elif board.board[x][y]=='1' or board.board[x][y]=='2' or board.board[x][y]=='3' or board.board[x][y]=='4' or board.board[x][y]=='5':
			return 2
		elif board.board[x][y]=='\033[1;34mB\033[1;m':
			return 5
		elif board.board[x][y]=='\033[1;31mE\033[1;m':
			return 7
		elif board.board[x][y]=='\033[1;35me\033[1;m':
			return 6
		else:
			return 3



