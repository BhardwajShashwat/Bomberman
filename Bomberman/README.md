
								 	README FILE:
List of contents:

1. Requirements
2. How to play the game
3. Classes:
4. Bonus

1.Requirements:
  
  python3 for running the game.

2.How to play the game:

  You control bomberman (represented by the symbol 'B') as he takes on his foes in three different levels. Use 'w','a','s' and 'd' to move bomberman along the board. 

  Bomberman also has the ability to plant bombs at his location. This is triggered by pressing 'b'. Bombs are placed at the current location of bomberman but once the bomberman moves to a different square, the bomb acts like walls until they explode. The explosion occurs after 3 ticks and has a range of one unit in all four directions. The explosion can kill both the bomberman and his enemies. 

  Walls are represented by 'X' and cannot be destroyed by enemies or by the bomberman's bombs themselves. They act as 'borders' and are the key building blocks of all levels.

  Breakable bricks are just like walls but can be destroyed using bombs. They are represented by '#'

  Enemies are represented by 'E' and move along one axis-vertical or horizontal. These enemies move only in one direction, but turn around as soon as they touch a wall or a breakable brick. Bomberman dies on colliding with any of these enemies. When enemies are killed, the player gains 100 points.

  The game is more like a move based game and not a time based game since all movement in the game is triggered by the user pressing a button. Because of this a player gets a more 'static' experience where the game effectively 'pauses' after each command.

  Score is displayed below the screen.

  The player has only one life.

  Run the run.py file using python3 to play the game.(See bonus for multiple levels)

  Note: Enemy movement was not randomized on purpose even though it wasn't very difficult to implement since I felt that it would make the game extremely difficult and boring.

3. Classes:
	1.Level
	2.Object--> Person->Bomberman
	 			   |--->Bomb
		           |--->Horizontalenemy
		           |--->Verticalenemy


4. Bonus:
	1. Implemented colors for walls, breakable bricks, enemies, Bomberman, bombs and even the explosion.
	2. Implemented a timer for the bomb
	3. Implemented three levels:
		The three levels can be accessed by running run.py, run1.py, run2.py using python3 respectively.

		Note: First level is just meant to help players get the hang of the game and contains all the basic building blocks while the remaining two are properly designed levels from a gameplay perspective.

		           


