from person import *
from board import *

class verticalenemy(Person):
	def __init__(self,x,y,board,toggle,status):
		Person.__init__(self,x,y)
		board.board[x][y]='\033[1;31mE\033[1;m'
		self.toggle=toggle
		self.status=status

	def vadd(self,board,x_man,y_man):
		board.board[x_man][y_man]='\033[1;31mE\033[1;m'

	def vertical_status(self):
		return self.status


	#check if enmy is dead.
	def vertical_dead(self,board):
		pos=self.get_position()
		x_man=pos[0]
		y_man=pos[1]
		if not board.board[x_man][y_man]=='\033[1;31mE\033[1;m':
				self.status="dead"
				self.delete(board)

	#moves vertical enemy around the board
	def vmove(self,board):
		pos=self.get_position()
		x_man=pos[0]
		y_man=pos[1]
		self.vertical_dead(board)
		if self.vertical_status()=="dead":
			return
		if self.toggle=='w':
			if self.checkspace(board,x_man,y_man-1)==1:
				self.remove(board,x_man,y_man)
				self.vadd(board,x_man,y_man-1)
				self.set_position(x_man,y_man-1)

			elif self.checkspace(board,x_man,y_man-1)==6:
				self.status="dead"
				self.delete(board)

			elif self.checkspace(board,x_man,y_man-1)==5:
				self.remove(board,x_man,y_man)
				self.vadd(board,x_man,y_man-1)
				self.set_position(x_man,y_man-1)

			elif self.checkspace(board,x_man,y_man-1)==3:
				flag=1

			elif self.checkspace(board,x_man,y_man-1)==2:
				self.toggle='s'
				self.remove(board,x_man,y_man)
				self.vadd(board,x_man,y_man+1)
				self.set_position(x_man,y_man+1)

		if self.toggle=='s':
			if self.checkspace(board,x_man,y_man+1)==1:
				self.remove(board,x_man,y_man)
				self.vadd(board,x_man,y_man+1)
				self.set_position(x_man,y_man+1)

			elif self.checkspace(board,x_man,y_man+1)==5:
				self.remove(board,x_man,y_man)
				self.vadd(board,x_man,y_man+1)
				self.set_position(x_man,y_man+1)

			elif self.checkspace(board,x_man,y_man+1)==3:
				flag=1

			elif self.checkspace(board,x_man,y_man+1)==6:
				self.status="dead"
				self.delete(board)

			elif self.checkspace(board,x_man,y_man+1)==2:
				self.toggle='w'
				self.remove(board,x_man,y_man)
				self.vadd(board,x_man,y_man-1)
				self.set_position(x_man,y_man-1)

		