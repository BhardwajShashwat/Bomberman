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

#constructs the level
Level1=Level()
Level1.constructlevel()
Level1.board[9][9]='\033[1;47m#\033[1;m'
Bman=bomberman(2,2,Level1,"alive")	
Vman=verticalenemy(15,15,Level1,'w',"alive")
Vflag=0
Hman=horizontalenemy(17,17,Level1,'a',"alive")
Hflag=0
Level1.lprint()

score=0
maxscore=200
#Runs the level
while True:	
	print("\n\n\nScore:",end=' ')
	print(score,end='\n\n')
	Level1.printkey()
	char = getch()
	if char == 'q' or Bman.bomberman_status()=="dead" or score==maxscore:
		break
	Bman.move(Level1,char)
	if Vman.vertical_status()=="alive":
		Vman.vmove(Level1)
	elif Vflag==0:
		score=score+100
		Vflag=1

	if Hman.horizontal_status()=="alive":
		Hman.hmove(Level1)
	elif Hflag==0:
		score=score+100
		Hflag=1	
	Level1.lprint()








