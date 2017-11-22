import sys
import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
	name = "Stinky Shoe Clicker",
	options={"build_exe": {"packages": ["pygame"], 
							"include_files": ["blueBG.jpg", "stinkyBG.jpg",
							"mudBG.jpg", "fume1.png", "fume2.png", "gameOver.jpg",
							"mood1.png", "mood2.png", "mood3.png", "mood4.png",
							"mood5.png", "mood6.png", "mood7.png", "mud.png",
							"MyPRNG.py", "napkin.png", "napkinButton.png",
							"napkinButtonDisabled.png", "README.txt", "sneaker.png",
							"song.mp3", "spraycan.png", "spraycanButton.png",
							"spraycanButtonDisabled.png", "titleScreen.jpg",
							"x2Multiplier1.png", "x2Multiplier1Disabled.png"]}},
	executables = executables
	
	) 
