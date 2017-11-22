README.TXT



THE PROGRAM:
	Students:
		Adrial Armijo - adrial.armijo@gmail.com
		Ryan Hodgson - hodgson@csu.fullerton.edu	
		Zachary McEachern - zachmceachern@yahoo.com
	Class: CPSC 386 - Game Design and Production T/TH 8:30-9:45pm

INTRODUCTION: 
	PROJECT SCOPE- Stinky Shoe Clicker relies on the sprite image files, theme music mp3 file and MyPRNG.py for random number generation. 
	These files are all included in the folder.The "All Sprites" folder contains the history and collecion of previous or future use sprites. 
	Sprites currently in use are located outside of this folder.


	External Requirements: pygame, python3

BUILD INSTRUCTIONS- This game was built in a Linux environment on Ubuntu. The code was edited in Geany and then ran it through the terminal.
We used the following commands to install pygame: 
	
	1. sudo apt-get install python3-pip 
	
	2. sudo pip3 install pygame


To Run The Game:
	
1. Navigate to the game's location. For example, if the game is located on the desktop:

		cd Desktop/game
	
2. While in this directory, type the following command to run the game file.

		./main.py
	
3. Begin game and enjoy!~~ 



HOW TO PLAY-
	
1. On Start Screen, press Play to begin the game or Quit to exit.
	
2. Begin clicking on the shoe to generate points. Points automatically generate,
   but click to generate more points.
	
3. Strategically upgrade your points multiplier to generate increase your points.
 
   If you upgrade too soon, you might not be prepared for a Stinky or Muddy situation.
	
4. Continue to keep your shoe as happy and clean as possible!
	
5. Clicking can be tiresome, so take a pause at any time by pressing the Escape key. 


RULES-
1. Can only remove Mud with the Napkin
2. Can only remove stinky fumes with the Spraycan
3. Can only upgrade when you have enough points for the upgrade

FEATURES-
1. Title, Pause, and Game Over screens
2. Music
3. Animated cursors

KNOWN BUGS-
	
1. Game is difficult when RNG is not in your favor, it can be virtually impossible to play.
 
   We've adjusted how much points are decremented in the environments to help counter this.	

2. The instruction screen does not load and will cause the program to freeze.
