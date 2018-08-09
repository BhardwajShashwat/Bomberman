class Object():
	def __init__(self,x,y):
		self.x=x
		self.y=y

	
	def get_position(self):
		pos=[self.x,self.y]
		return pos


	def set_position(self,x,y):
		self.x=x
		self.y=y
