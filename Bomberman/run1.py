from board import *
from obj import *
from person import *
from bomberman import *
from verticalenemy import *
from bomb import *
from horizontalenemy import *
import sys, termios, tty, os, time
 
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
#creates the level
Level1=Level()
Level1.fill()
for i in range(1,Level1.breadth-1):
	Level1.board[i][10]=' '
	Level1.board[i][11]=' '
	Level1.board[i][12]=' '

for i in range(1,Level1.length-1):
	Level1.board[7][i]=' '
	Level1.board[8][i]=' '
	Level1.board[14][i]=' '
	Level1.board[15][i]=' '
	Level1.board[21][i]=' '
	Level1.board[22][i]=' '
	Level1.board[28][i]=' '
	Level1.board[29][i]=' '
	Level1.board[35][i]=' '
	Level1.board[36][i]=' '

Bman=bomberman(2,11,Level1,"alive")
Vman1=verticalenemy(7,2,Level1,'w',"alive")
Vflag1=0

Vman2=verticalenemy(14,2,Level1,'w',"alive")
Vflag2=0

Vman3=verticalenemy(21,2,Level1,'w',"alive")
Vflag3=0

Vman4=verticalenemy(28,2,Level1,'w',"alive")
Vflag4=0

Vman5=verticalenemy(35,2,Level1,'w',"alive")
Vflag5=0

Level1.lprint()

score=0
maxscore=500

#Runs the level
while True:	
	print("\n\nScore:",end=' ')
	print(score,end='\n\n')
	Level1.printkey()
	char = getch()
	if char == 'q' or Bman.bomberman_status()=="dead" or score==maxscore:
		break
	Bman.move(Level1,char)
	if Vman1.vertical_status()=="alive":
		Vman1.vmove(Level1)
	elif Vflag1==0:
		score=score+100
		Vflag1=1

	if Vman2.vertical_status()=="alive":
		Vman2.vmove(Level1)
	elif Vflag2==0:
		score=score+100
		Vflag2=1

	if Vman3.vertical_status()=="alive":
		Vman3.vmove(Level1)
	elif Vflag3==0:
		score=score+100
		Vflag3=1

	if Vman4.vertical_status()=="alive":
		Vman4.vmove(Level1)
	elif Vflag4==0:
		score=score+100
		Vflag4=1

	if Vman5.vertical_status()=="alive":
		Vman5.vmove(Level1)
	elif Vflag5==0:
		score=score+100
		Vflag5=1	
	Level1.lprint()

