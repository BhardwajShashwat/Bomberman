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
	Level1.board[i][1]=' '
	Level1.board[i][Level1.length-2]=' '

for i in range(1,Level1.length-1):
	Level1.board[1][i]=' '
	Level1.board[2][i]=' '
	Level1.board[Level1.breadth-2][i]=' '
	Level1.board[Level1.breadth-3][i]=' '

for i in range(4,Level1.breadth-4):
	Level1.board[i][3]=' '
	Level1.board[i][Level1.length-4]=' '

for i in range(4,Level1.length-4):
	Level1.board[4][i]=' '
	Level1.board[5][i]=' '
	Level1.board[Level1.breadth-5][i]=' '
	Level1.board[Level1.breadth-6][i]=' '

for i in range(7,Level1.breadth-7):
	Level1.board[i][5]=' '
	Level1.board[i][Level1.length-6]=' '

for i in range(6,Level1.length-6):
	Level1.board[7][i]=' '
	Level1.board[8][i]=' '
	Level1.board[Level1.breadth-8][i]=' '
	Level1.board[Level1.breadth-9][i]=' '

Bman=bomberman(1,1,Level1,"alive")

Hman1=horizontalenemy(20,Level1.length-2,Level1,'a',"alive")
Hflag1=0

Hman2=horizontalenemy(20,3,Level1,'d',"alive")
Hflag2=0

Hman3=horizontalenemy(20,Level1.length-6,Level1,'a',"alive")
Hflag3=0

Level1.board[20][Level1.length-3]='\033[1;47m#\033[1;m'
Level1.board[21][Level1.length-3]='\033[1;47m#\033[1;m'
Level1.board[20][4]='\033[1;47m#\033[1;m'
Level1.board[21][4]='\033[1;47m#\033[1;m'
Level1.lprint()

score=0
maxscore=300

#runs the level
while True:	
	print("\n\nScore:",end=' ')
	print(score,end='\n\n')
	Level1.printkey()
	char = getch()
	if char == 'q' or Bman.bomberman_status()=="dead" or score==maxscore:
		break
	Bman.move(Level1,char)

	if Hman1.horizontal_status()=="alive":
		Hman1.hmove(Level1)
	elif Hflag1==0:
		score=score+100
		Hflag1=1

	if Hman2.horizontal_status()=="alive":
		Hman2.hmove(Level1)
	elif Hflag2==0:
		score=score+100
		Hflag2=1

	if Hman3.horizontal_status()=="alive":
		Hman3.hmove(Level1)
	elif Hflag3==0:
		score=score+100
		Hflag3=1

	Level1.lprint()