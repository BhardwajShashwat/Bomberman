from person import *
from board import *
from bomb import *

class bomberman(Person):
	def __init__(self,x,y,board,status):
		Person.__init__(self,x,y)
		self.status="alive"
		board.board[x][y]='\033[1;34mB\033[1;m'
		self.bomber=0
		self.bomb_check=0	

	def bomberman_status(self):
		return self.status

	def add(self,board,x_man,y_man):
		board.board[x_man][y_man]='\033[1;34mB\033[1;m'

	#Function to check if bomberman is alive after every frame.
	def bomberman_dead(self,board):
		pos=self.get_position()
		x_man=pos[0]
		y_man=pos[1]
		if not board.board[x_man][y_man]=='\033[1;34mB\033[1;m':
			if not board.board[x_man][y_man]=='1' or board.board[x_man][y_man]=='2' or board.board[x_man][y_man]=='3' or board.board[x_man][y_man]=='4' or board.board[x_man][y_man]=='5':
				self.status="dead"

	#Handles movement of bomberman based on input after every frame.
	def move(self,board,inp):
		pos=self.get_position()
		x_man=pos[0]
		y_man=pos[1]
		flag=0
		self.bomberman_dead(board)

		if inp=='w':
			if self.checkspace(board,x_man,y_man-1)==1:
				self.remove(board,x_man,y_man)
				self.add(board,x_man,y_man-1)
				self.set_position(x_man,y_man-1)

			elif self.checkspace(board,x_man,y_man-1)==6 or self.checkspace(board,x_man,y_man-1)==7:
				self.status="dead"
				self.remove(board,x_man,y_man)
			elif self.checkspace(board,x_man,y_man-1)==3:
				self.remove(board,x_man,y_man)
				flag=1

		if inp=='a':
			if self.checkspace(board,x_man-1,y_man)==1:
				self.remove(board,x_man,y_man)
				self.add(board,x_man-1,y_man)
				self.set_position(x_man-1,y_man)

			elif self.checkspace(board,x_man-1,y_man)==6 or self.checkspace(board,x_man-1,y_man)==7:
				self.status="dead"
				self.remove(board,x_man,y_man)

			elif self.checkspace(board,x_man-1,y_man)==3:
				self.remove(board,x_man,y_man)
				flag=1

		if inp=='s':
			if self.checkspace(board,x_man,y_man+1)==1:
				self.remove(board,x_man,y_man)
				self.add(board,x_man,y_man+1)
				self.set_position(x_man,y_man+1)

			elif self.checkspace(board,x_man,y_man+1)==6 or self.checkspace(board,x_man,y_man+1)==7:
				self.status="dead"
				self.remove(board,x_man,y_man)

			elif self.checkspace(board,x_man,y_man+1)==3:
				self.remove(board,x_man,y_man)
				flag=1

		if inp=='d':
			if self.checkspace(board,x_man+1,y_man)==1:
				self.remove(board,x_man,y_man)
				self.add(board,x_man+1,y_man)
				self.set_position(x_man+1,y_man)

			elif self.checkspace(board,x_man+1,y_man)==6 or self.checkspace(board,x_man+1,y_man)==7:
				self.status="dead"
				self.remove(board,x_man,y_man)

			elif self.checkspace(board,x_man+1,y_man)==3:
				self.remove(board,x_man,y_man)
				flag=1


		if inp=='b':
			#Sets the bomb as long as no other bomb is active.
			if self.bomb_check==0:		
				self.bomb=bomb(x_man,y_man,board)
				self.bomb_check=1

		#Makes the bomb 'tic',thus determining when it will explode.			
		if(self.bomb_check==1):
			self.bomb.tick(board)
			if self.bomb.get_tic()==-1:
				self.bomb_check=0

