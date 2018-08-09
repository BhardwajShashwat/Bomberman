class Level():
	def __init__(self):
		self.length=24
		self.breadth=44
		self.board=[[' ' for i in range(self.length)] for j in range(self.breadth)]

	#creates a box around the level which serves as an outer boundary.
	def constructlevel(self):
		board=[[' ' for i in range(self.length)] for j in range(self.breadth)]	
		for j in range(0,2):
			for i in range(self.length):
				board[j][i]='\033[1;45mX\033[1;m'

		for j in range(self.breadth-2,self.breadth):
			for i in range(self.length):
				board[j][i]='\033[1;45mX\033[1;m'		

		for i in range(0,2):
			for j in range(self.breadth):
				board[j][i]='\033[1;45mX\033[1;m'

		for i in range(self.length-2,self.length):
			for j in range(self.breadth):
				board[j][i]='\033[1;45mX\033[1;m'

		self.board=board

	#prints the array
	def lprint(self):
		for i in range(self.length):
			print('\t\t\t\t',end='')
			for j in range(self.breadth):
				print(self.board[j][i],end='')
			print('\n',end='')

	#prints the key for the game.
	def printkey(self):
		print("\n\n\nB:",end='')
		print("Bomberman\n",end='\n') 
		print("E:",end='')
		print("Enemy\n",end='\n')
		print("e:",end='')
		print("Explosion\n",end='\n')
		print("X:",end='')
		print("Wall\n",end='\n')
		print("#:",end='')
		print("Breakable walls\n",end='\n')

	#Fills the level with walls completely. Useful for creating levels from scratch.	
	def fill(self):
		for i in range(self.length):
			for j in range(self.breadth):
					self.board[j][i]='\033[1;45mX\033[1;m'