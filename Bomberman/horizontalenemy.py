from person import *
from board import *

class horizontalenemy(Person):
	def __init__(self,x,y,board,toggle,status):
		Person.__init__(self,x,y)
		board.board[x][y]='\033[1;31mE\033[1;m'
		self.toggle=toggle
		self.status=status

	def hadd(self,board,x_man,y_man):
		board.board[x_man][y_man]='\033[1;31mE\033[1;m'

	def horizontal_status(self):
		return self.status

	#checks if enemy is dead
	def horizontal_dead(self,board):
		pos=self.get_position()
		x_man=pos[0]
		y_man=pos[1]
		if not board.board[x_man][y_man]=='\033[1;31mE\033[1;m':
				self.status="dead"
				self.delete(board)

	#handles enemy movement
	def hmove(self,board):
		pos=self.get_position()
		x_man=pos[0]
		y_man=pos[1]
		self.horizontal_dead(board)
		if self.horizontal_status()=="dead":
			return
		if self.toggle=='a':
			if self.checkspace(board,x_man-1,y_man)==1:
				self.remove(board,x_man,y_man)
				self.hadd(board,x_man-1,y_man)
				self.set_position(x_man-1,y_man)

			elif self.checkspace(board,x_man-1,y_man)==5:
				self.remove(board,x_man,y_man)
				self.hadd(board,x_man-1,y_man)
				self.set_position(x_man-1,y_man)

			elif self.checkspace(board,x_man-1,y_man)==3:
				flag=1

			elif self.checkspace(board,x_man-1,y_man)==6:
				self.status="dead"
				self.delete(board)


			elif self.checkspace(board,x_man-1,y_man)==2:
				self.toggle='d'
				self.remove(board,x_man,y_man)
				self.hadd(board,x_man+1,y_man)
				self.set_position(x_man+1,y_man)

		if self.toggle=='d':
			if self.checkspace(board,x_man+1,y_man)==1:
				self.remove(board,x_man,y_man)
				self.hadd(board,x_man+1,y_man)
				self.set_position(x_man+1,y_man)

			elif self.checkspace(board,x_man+1,y_man)==5:
				self.remove(board,x_man,y_man)
				self.hadd(board,x_man+1,y_man)
				self.set_position(x_man+1,y_man)

			elif self.checkspace(board,x_man+1,y_man)==6:
				self.status="dead"
				self.delete(board)

			elif self.checkspace(board,x_man+1,y_man)==3:
				flag=1

			elif self.checkspace(board,x_man+1,y_man)==2:
				self.toggle='a'
				self.remove(board,x_man,y_man)
				self.hadd(board,x_man-1,y_man)
				self.set_position(x_man-1,y_man)

	