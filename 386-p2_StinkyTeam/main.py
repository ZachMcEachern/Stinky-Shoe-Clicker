#!/usr/bin/env python3

#------------------------------
#      VERSION: v3.9          |
#------------------------------

# CPSC 386 Final Project
# Game: Stinky Shoe Clicker!
# Click the sneaker and generate points! Upgrade your clicker and watch
# out for mudslides. A filthy sneaker is a stinky sneaker, so clean it 
# up as needed! Get too dirty and you're in for a stinky time!

# Zachary McEachern - zachmceachern@yahoo.com
# Adrial Armijo - adrial.armijo@gmail.com
# Ryan Hodgson - hodgson@csu.fullerton.edu
# With art contributions from:
# 	***** Leslie Hernandez, CSUF Art Undergrad Student ******

import sys
import pygame
import time
from MyPRNG import MyPRNG

# initialize pygame
pygame.init()

##################### CONSTANTS #####################

# set title
title = "Stinky Shoe Clicker!"

# colors
backColor = 102, 153, 255 # light blue
white = 255, 255, 255
lightGreen = 0, 255, 0
lightRed = 255, 0, 0
green = 0, 200, 0
red = 200, 0, 0
brown = 179, 89, 0
gray = 192, 192, 192
black = 0, 0, 0
#####################################################

# GLOBALS #
RUNNING = 1 
PAUSED = 0
state = RUNNING
score = 1
scoreMultiplier = 1
upgradeCost = 500
clickValue = 10
hpoints = 4
chance = 1
mood = pygame.image.load("mood4.png")

# create instance of PRNG
myGen = MyPRNG()

# set width/height
size = width, height = 800, 600

# create the screen
screen = pygame.display.set_mode(size)

# set window title
pygame.display.set_caption(title)

# create clock object
clock = pygame.time.Clock()

# --------------------- Button ----------------------------

# ======================button() ==========================
# button is used for any clickable object in game.
# =========================================================

def button(msg, xPos, yPos, width, height, activeColor, inactiveColor, action):
	# object for getting mouse position
	mouse = pygame.mouse.get_pos()
	
	# object for getting mouse click
	click = pygame.mouse.get_pressed()

	# if you hover over first button, turn active color, else turn inactive color
	if xPos + width > mouse[0] > xPos and yPos + height > mouse[1] > yPos:
		pygame.draw.rect(screen, activeColor, (xPos, yPos, width, height))
		if click[0] == 1:
			if action == "play":
				gameLoop()
			elif action == "continue":
				return True
			elif action == "instructions":
				instructionMenu()
			else:
				sys.exit()
	else:
		pygame.draw.rect(screen, inactiveColor, (xPos, yPos, width, height))
		
	# font object for buttons
	buttonFont = pygame.font.Font(pygame.font.get_default_font(), 20)
		
	# button text
	buttonTextSurface = buttonFont.render(msg, True, white)
	buttonTextRect = buttonTextSurface.get_rect()
	buttonTextRect.center = ((xPos+(width/2)), (yPos+(height/2)))
	screen.blit(buttonTextSurface, buttonTextRect)

# ------------------------- Game Screens -----------------------

# ======================= menu() ==========================
# menu shows the initial start screen and gives the option
	# to play or quit. It is called by the main function
	# at the start of the program.
# =========================================================
def menu():
	### maybe make menu return value to main() ###
	
	# load titleScreen image
	titleScreen = pygame.image.load("titleScreen.jpg")
	# titleScreen rectangle
	titleScreenRect = titleScreen.get_rect()
	
	while 1:
		for event in pygame.event.get():
			#print(event)
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		
		# draw images onto screen
		screen.blit(titleScreen, titleScreenRect)
		
		# draw play and quit buttons, change colors when hovering
		button("Play", 350, 450, 100, 50, lightGreen, green, "play")
		button("Quit", 350, 515, 100, 50, lightRed, red, "quit")
		#new instruction screen
		button("Instructions", 475, 450, 175, 50, gray, black, "instructions") 
		# update screen
		pygame.display.update()
		clock.tick(15)

# ======================== text_objects() =========================
# creates a text object used for our instruction menu
# ===============================================================
def text_objects(text, font):
    paragraphSize = (xsize, ysize)
    fontSize = font.get_height()

    # create surface for the paragraph
    paragraphSurface = pygame.Surface(paragraphSize) 

    # make transparent paragraph surface
    paragraphSurface.fill((255, 255, 255))
    paragraphSurface.set_colorkey((255, 255, 255))

    # split the text into several lines
    splitLines = text.splitlines() 

    # get vertical offset 
    offSet = (paragraphSize[1] - len(splitLines) * (fontSize + 1)) // 2 

    # loop for each line in the paragraph
    for idx, line in enumerate(splitLines):
        currentTextline = font.render(line, False, (0, 0, 0))
        currentPostion = ((paragraphSize[0] - currentTextLine.get_width*() // 2,
							idx * fontSize + offset))
        paragraphSurface.blit(currentTextline, currentPostion)

    # draw onto the surface
    return paragraphSurface, paragraphSize

# ======================== paragraphText() =========================
# sets up the correct format for our instruction menu.
# ==================================================================
def paragraphText(text, font):
   paragraphSize = (600,500)
   fontSize = font.get_height()

   paragraphSurf = pygame.Surface(ParagraphSize)

   paragraphSurf.fill(WHITE)
   paragraphSurf.set_colorkey(WHITE)

   splitLines = text.splitlines()

   centreText = (ParagraphSize[1] - len(SplitLines)*(FontSize + 1)//2)

   for idx, line in enumerate(SplitLines):
       currentTextline = font.render(text, False, (0, 0, 0))
       currentPostion = (0, idx * FontSize + CentreText)
       paragraphSurf.blit(currentTextline, currentPostion)

   return paragraphSurf, paragraphSize

# ======================== instructionMenu() =========================
# handles the instructions that are given at the beginning of the game.
# ====================================================================		
def instructionMenu():
	### maybe make menu return value to main() ###
	
	# load titleScreen image
	titleScreen = pygame.image.load("stinkyBG.jpg")
	# titleScreen rectangle
	titleScreenRect = titleScreen.get_rect()
	
	# load instructions
	instructions = """HOW TO PLAY-
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
		3. Can only upgrade when you have enough points for the upgrade"""
	
	while 1:
		for event in pygame.event.get():
			#print(event)
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		
	# draw images onto screen
	screen.blit(titleScreen, titleScreenRect)
	instructionsFont = pygame.font.SysFont("monospace",15)
	textSurf, textRect = text_objects("Instructions", instructionsFont)
	textRect.center = ((screen_width/2),(screen_height/6))
	screen.blit(TextSurf, TextRect)
	paragraphText(paragraph, instructionsFont)

	intro = True
		
	# draw play and quit buttons, change colors when hovering
	button("Play", 350, 450, 100, 50, lightGreen, green, "play")
	button("Quit", 350, 515, 100, 50, lightRed, red, "quit")
		
	# update screen
	pygame.display.update()
	clock.tick(15)

# ======================= gameOver() ==========================
# gameOver shows after points hit 0. It is called by events
	# where points are decreased. The player then has the option
    # to continue or quit.
# =============================================================

def gameOver():
	# resets the values so you can continue from a new game if you die
	global RUNNING  
	global PAUSED
	global state
	global score 
	global scoreMultiplier 
	global upgradeCost 
	global clickValue
	global hpoints 
	global chance 
	global mood 


	RUNNING = 1 
	PAUSED = 0
	state = RUNNING
	score = 1
	scoreMultiplier = 1
	upgradeCost = 500
	clickValue = 10
	hpoints = 4
	chance = 1
	mood = pygame.image.load("mood4.png")

	# make mouse visible
	pygame.mouse.set_visible(True)
	# load gameOver image
	gameOver = pygame.image.load("gameOver.jpg")
	# gameOver rectangle
	gameOverRect = gameOver.get_rect()
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		
		# draw images onto screen
		screen.blit(gameOver, gameOverRect)

		# draw play and quit buttons, change colors when hovering
		button("Continue", 350, 450, 100, 50, lightGreen, green, "play")
		button("Quit", 350, 515, 100, 50, lightRed, red, "quit")
		
		# update screen
		pygame.display.update()
		clock.tick(15)
		
# ======================= pauseScreen() ==============================
# pauseScreen shows when escape is pressed. It is called by the main
	# loop. At this time, pause is implemented into all
	# events.
# ====================================================================

def pauseScreen():
	#debug step
	print("Pausing game..")
	
	# fill screen with backColor
	screen.fill(backColor)
	
	#set the font as the same font on title screen
	font = pygame.font.Font(pygame.font.get_default_font(), 64)
	
	# render the text on the screen
	textSurface = font.render("PAUSED", True, white)
	
	# create text utility object
	textRect = textSurface.get_rect()
	
	#center the text
	textRect.center = ((width/2),(height/2))
	
	#draw text onto screen
	screen.blit(textSurface, textRect)
	
	#bring in the state global variable
	global state
	
	while(state == PAUSED):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		
		# when continue is pressed, action set to True		
		action = button("Continue", 350,375,100,50, lightGreen, green, "continue")
		button("Quit", 350,450,100,50, lightRed, red, "quit")
		
		# if true, return to game
		if action == True:
			return
	
		pygame.display.update()
		clock.tick(15)

#-------------------------Events------------------------------

# ===================== mudslide() =============================
# mudslide randomly generates mud onto the shoe
	# in this event, points decrease at a medium rate
	# and the amount of decrease scales with the x2 multiplier
	# it is called during the gameLoop() and calls the PRNG
	# for numbers
# ==============================================================
def mudslide():
	# reference global vars
	global score
	global scoreMultiplier
	global upgradeCost
	global clickValue
	global hpoints 
	
	# list for storing mudSplat recs
	mudArray = []
	
	# load background image
	background = pygame.image.load("mudBG.jpg")
	# create background rectangle
	backgroundRect = background.get_rect()
	
	# load mood image
	global mood
	#create mood rectangle
	moodRect = mood.get_rect() #new
	
	# load Napkin Cursor Image
	napkinCursor = pygame.image.load("napkin.png")
    # napkin Cursor Rectangle
	napkinCursorRect = napkinCursor.get_rect()
    # set napkin cursor variable to not clicked yet
	napkinButtonPressed = False
	
	# load up mudSplat
	# mudSplatRects will be instantiated later
	mudSplat = pygame.image.load("mud.png")
	
	# load muddy shoe image
	muddyShoe = pygame.image.load("sneaker.png")
	# muddyShoe rectangle
	muddyShoeRect = muddyShoe.get_rect()
	
	# load napkin button
	napkinButton = pygame.image.load("napkinButton.png")
	# create napkin rectangle
	napkinButtonRect = napkinButton.get_rect()
	
	# load deodorant button
	deodorButton = pygame.image.load("spraycanButtonDisabled.png")
	# create napkin rectangle
	deodorButtonRect = deodorButton.get_rect()
	
	myfont = pygame.font.SysFont("monospace", 16)
	
	# set x,y position of shoe image on screen
	muddyShoeRect.x = width * 0.07
	muddyShoeRect.y = height * 0.15
		
	# set x,y position of napkin image on screen
	napkinButtonRect.x = width * 0.83
	napkinButtonRect.y = height * 0.25
	
	# set x,y position of deodorant image on screen
	deodorButtonRect.x = width * 0.83
	deodorButtonRect.y = height * 0.49
	
	# set x,y position of mood image on screen
	moodRect.x = width * .33 #new
	moodRect.y = height * .01 #new
	
	# place a number of mudSplats on shoe based on multiplier
	if scoreMultiplier == 1:
		mudSplatRect = mudSplat.get_rect()
		randNum = randomNumber()
		mudSplatRect.x = ((width * randNum) % (656 - 334)) + muddyShoeRect.x
		mudSplatRect.y = ((height * randNum) % (590 - 317)) + muddyShoeRect.y
		mudArray.append(mudSplatRect)
		
	elif scoreMultiplier == 2:
		prn1 = randomNumber()
		mudSplatRect1 = mudSplat.get_rect()
		mudSplatRect1.x = ((width * prn1) % (656 - 334)) + muddyShoeRect.x
		mudSplatRect1.y = ((height * prn1) % (590 - 317)) + muddyShoeRect.y
		mudArray.append(mudSplatRect1)
		
		myGen.setSeed(prn1)
		prn2 = (myGen.next_prn() % 100) + 1
		
		mudSplatRect2 = mudSplat.get_rect()
		mudSplatRect2.x = ((width * prn2) % (656 - 334)) + muddyShoeRect.x
		mudSplatRect2.y = ((height * prn2) % (590 - 317)) + muddyShoeRect.y
		mudArray.append(mudSplatRect2)
		
	elif scoreMultiplier > 2:
		prn1 = randomNumber()
		mudSplatRect1 = mudSplat.get_rect()
		mudSplatRect1.x = ((width * prn1) % (656 - 334)) + muddyShoeRect.x
		mudSplatRect1.y = ((height * prn1) % (590 - 317)) + muddyShoeRect.y
		mudArray.append(mudSplatRect1)
		
		myGen.setSeed(prn1)
		prn2 = (myGen.next_prn() % 100) + 1
		
		mudSplatRect2 = mudSplat.get_rect()
		mudSplatRect2.x = ((width * prn2) % (656 - 334)) + muddyShoeRect.x
		mudSplatRect2.y = ((height * prn2) % (590 - 317)) + muddyShoeRect.y
		mudArray.append(mudSplatRect2)
		
		myGen.setSeed(prn2)
		prn3 = (myGen.next_prn() % 100) + 1
		
		mudSplatRect3 = mudSplat.get_rect()
		mudSplatRect3.x = ((width * prn3) % (656 - 334)) + muddyShoeRect.x
		mudSplatRect3.y = ((height * prn3) % (590 - 317)) + muddyShoeRect.y
		mudArray.append(mudSplatRect3)
	
	start = time.time()
	
	while 1:
		# if exit button is pressed, close program
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			
			#check for pause
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					state = PAUSED
					pauseScreen()
			
			# if mudSplat is clicked, remove from array
			if event.type == pygame.MOUSEBUTTONDOWN and napkinButtonPressed == True:
				x, y = event.pos
				for item in mudArray:
					if item.collidepoint(x, y):
						click = pygame.mouse.get_pressed()
						mudArray.remove(item)
						hpoints += 1
						#happyMeter()
		
		# if score is less than or equal to 0, game over!
		if score < 0:
			print("You Lose!")
			gameOver()

	    # load multiplyer button
		if score >= upgradeCost:
			multiplier = pygame.image.load("x2Multiplier1.png")
		else : 
			multiplier = pygame.image.load("x2Multiplier1Disabled.png")
	    # create multiplyer rectangle
		multRect = multiplier.get_rect()

		# set x,y position of multiplier image on screen
		multRect.x = width * 0.83
		multRect.y = height * 0.01

		# draw images onto screen
		screen.blit(background, backgroundRect)
		screen.blit(muddyShoe, muddyShoeRect)
		screen.blit(multiplier, multRect)
		screen.blit(napkinButton, napkinButtonRect)
		screen.blit(deodorButton, deodorButtonRect)
		screen.blit(mood, moodRect) #new
		
		# draw all mudSplats on screen
		for item in mudArray:
			screen.blit(mudSplat, item)
		
		# render text on screen
		scoretext = myfont.render("Score {0}".format(score),1,(0,0,0))
		upgradetext = myfont.render("Upgrade Cost: {0}".format(upgradeCost),1,(0,0,0))
		multipliertext = myfont.render("Multiplier: x{0}".format(scoreMultiplier),1,(0,0,0))
		
		# draw text onto screen
		screen.blit(scoretext, (5,10))
		screen.blit(upgradetext, (5,30))
		screen.blit(multipliertext, (5,50))
		
		# object for getting mouse position and click value
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		
		# this is so we know to render the cursor as the napkin image if pressed
		if napkinButtonPressed == True:
			# making the cursor invisible
			pygame.mouse.set_visible( False )
			# place the napkin image over the cursor
			napkinCursorRect.center = pygame.mouse.get_pos()
			# display the napkin image over the cursor
			screen.blit(napkinCursor, napkinCursorRect)
		
		# activate multiplier if button is pressed
		if (multRect.x + 130 > mouse[0] > multRect.x and multRect.y + 130 > mouse[1] > multRect.y) and score >= upgradeCost:
			if click[0] == 1:
				score -= upgradeCost
				scoreMultiplier *= 2
				upgradeCost *= scoreMultiplier
				clickValue *= scoreMultiplier
				# reset left click[0] to 0
				click = pygame.mouse.get_pressed()
		
		# activate napkin if button is pressed
		if (napkinButtonRect.x + 130 > mouse[0] > napkinButtonRect.x and napkinButtonRect.y + 130 > mouse[1] > napkinButtonRect.y):
			if click[0] == 1:
				napkinButtonPressed = True
				# reset left click[0] to 0
				click = pygame.mouse.get_pressed()
		
		# if mudArray is empty, return to gameLoop()
		if len(mudArray) == 0:
			pygame.mouse.set_visible(True)
			end = time.time()
			lapse = end - start
			print("end - start: ", end - start)
			if lapse >= 1 and lapse < 1.5:
				hpoints += 1
				happyMeter()
			if lapse >= 1.5 and lapse < 2:
				hpoints -= 1
				happyMeter()
			if lapse >= 2:
				hpoints -= 2
				happyMeter()
				
			return
				
		# decrement score (medium decrease)
		score -= int(((20 * scoreMultiplier) / 5))
		
		# update the screen
		pygame.display.update()
		clock.tick(10)

# ===================== stinky() =============================
# stinky randomly generates fumes onto the shoe
	# in this event, points decrease at an extremely fast rate
	# and the amount of decrease scales with the x2 multiplier
	# it is called during the gameLoop() and calls the PRNG
	# for numbers
# ==============================================================

def stinky():
	# reference global vars
	global score
	global scoreMultiplier
	global upgradeCost
	global clickValue
	global hpoints
	
	# list for storing stinky rects
	stinkArray = []
	
	# load background image
	background = pygame.image.load("stinkyBG.jpg")
	# create background rectangle
	backgroundRect = background.get_rect()
	
	# load deodorant Cursor Image
	deodorCursor = pygame.image.load("spraycan.png")
    # deodorant Cursor Rectangle
	deodorCursorRect = deodorCursor.get_rect()
    # set napkin cursor variable to not clicked yet
	deodorButtonPressed = False
	
	# load up stinky fumes
	# stinkSplatRects will be instantiated later
	stinkSplat = pygame.image.load("fume1.png")
	stinkSplat2 = pygame.image.load("fume2.png")
	
	# load stinky shoe image
	stinkyShoe = pygame.image.load("sneaker.png")
	# stinkyShoe rectangle
	stinkyShoeRect = stinkyShoe.get_rect()
	
	# load mood image
	global mood
	#create mood rectangle
	moodRect = mood.get_rect() #new
	
	# load napkin button
	napkinButton = pygame.image.load("napkinButtonDisabled.png")
	# create napkin rectangle
	napkinButtonRect = napkinButton.get_rect()
	
	# load deodorant button
	deodorButton = pygame.image.load("spraycanButton.png")
	# create napkin rectangle
	deodorButtonRect = deodorButton.get_rect()
	
	myfont = pygame.font.SysFont("monospace", 16)
	
	# set x,y position of shoe image on screen
	stinkyShoeRect.x = width * 0.07
	stinkyShoeRect.y = height * 0.15
		
	# set x,y position of napkin image on screen
	napkinButtonRect.x = width * 0.83
	napkinButtonRect.y = height * 0.25
	
	# set x,y position of deodorant image on screen
	deodorButtonRect.x = width * 0.83
	deodorButtonRect.y = height * 0.49
	
	# set x,y position of mood image on screen
	moodRect.x = width * .33 #new
	moodRect.y = height * .01 #new
	
	# place a number of fumes on shoe based on multiplier
	if scoreMultiplier == 1:
		stinkSplatRect = stinkSplat.get_rect()
		randNum = randomNumber()
		stinkSplatRect.x = ((width * randNum) % (656 - 334)) + stinkyShoeRect.x
		stinkSplatRect.y = ((height * randNum) % (590 - 317)) + stinkyShoeRect.y
		
		stinkArray.append(stinkSplatRect)
		
	elif scoreMultiplier == 2:
		prn1 = randomNumber()
		stinkSplatRect1 = stinkSplat2.get_rect()
		stinkSplatRect1.x = ((width * prn1) % (656 - 334)) + stinkyShoeRect.x
		stinkSplatRect1.y = ((height * prn1) % (590 - 317)) + stinkyShoeRect.y
		stinkArray.append(stinkSplatRect1)
		
		myGen.setSeed(prn1)
		prn2 = (myGen.next_prn() % 100) + 1
		
		stinkSplatRect2 = stinkSplat.get_rect()
		stinkSplatRect2.x = ((width * prn2) % (656 - 334)) + stinkyShoeRect.x
		stinkSplatRect2.y = ((height * prn2) % (590 - 317)) + stinkyShoeRect.y
		stinkArray.append(stinkSplatRect2)
		
	elif scoreMultiplier > 2:
		prn1 = randomNumber()
		stinkSplatRect1 = stinkSplat2.get_rect()
		stinkSplatRect1.x = ((width * prn1) % (656 - 334)) + stinkyShoeRect.x
		stinkSplatRect1.y = ((height * prn1) % (590 - 317)) + stinkyShoeRect.y
		stinkArray.append(stinkSplatRect1)
		
		myGen.setSeed(prn1)
		prn2 = (myGen.next_prn() % 100) + 1
		
		stinkSplatRect2 = stinkSplat2.get_rect()
		stinkSplatRect2.x = ((width * prn2) % (656 - 334)) + stinkyShoeRect.x
		stinkSplatRect2.y = ((height * prn2) % (590 - 317)) + stinkyShoeRect.y
		stinkArray.append(stinkSplatRect2)
		
		myGen.setSeed(prn2)
		prn3 = (myGen.next_prn() % 100) + 1
		
		stinkSplatRect3 = stinkSplat.get_rect()
		stinkSplatRect3.x = ((width * prn3) % (656 - 334)) + stinkyShoeRect.x
		stinkSplatRect3.y = ((height * prn3) % (590 - 317)) + stinkyShoeRect.y
		stinkArray.append(stinkSplatRect3)
	
	start = time.time()
	
	while 1:
		# if exit button is pressed, close program
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			
			#check for pause
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					state = PAUSED
					pauseScreen()
			
			# if stinkySplat is clicked, remove from array
			if event.type == pygame.MOUSEBUTTONDOWN and deodorButtonPressed == True:
				x, y = event.pos
				for item in stinkArray:
					if item.collidepoint(x, y):
						click = pygame.mouse.get_pressed()
						stinkArray.remove(item)
						hpoints += 1
						#happyMeter()
		# if score is less than or equal to 0, game over!
		if score < 0:
			print("You Lose!")
			gameOver()

	    # load multiplyer button
		if score >= upgradeCost:
			multiplier = pygame.image.load("x2Multiplier1.png")
		else : 
			multiplier = pygame.image.load("x2Multiplier1Disabled.png")
	    # create multiplyer rectangle
		multRect = multiplier.get_rect()

		# set x,y position of multiplier image on screen
		multRect.x = width * 0.83
		multRect.y = height * 0.01

		# draw images onto screen
		screen.blit(background, backgroundRect)
		screen.blit(stinkyShoe, stinkyShoeRect)
		screen.blit(multiplier, multRect)
		screen.blit(napkinButton, napkinButtonRect)
		screen.blit(deodorButton, deodorButtonRect)
		screen.blit(mood, moodRect) #new
		
		# draw all stinkSplats on screen
		for item in stinkArray:
			screen.blit(stinkSplat, item)
		
		# render text on screen
		scoretext = myfont.render("Score {0}".format(score),1,(0,0,0))
		upgradetext = myfont.render("Upgrade Cost: {0}".format(upgradeCost),1,(0,0,0))
		multipliertext = myfont.render("Multiplier: x{0}".format(scoreMultiplier),1,(0,0,0))
		
		# draw text onto screen
		screen.blit(scoretext, (5,10))
		screen.blit(upgradetext, (5,30))
		screen.blit(multipliertext, (5,50))
		
		# object for getting mouse position and click value
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		
		# rendor deodorant mouse cursor
		if deodorButtonPressed == True:
			# making the cursor invisible
			pygame.mouse.set_visible( False )
			# place the napkin image over the cursor
			deodorCursorRect.center = pygame.mouse.get_pos()
			# display the napkin image over the cursor
			screen.blit(deodorCursor, deodorCursorRect)
		
		# activate multiplier if button is pressed
		if (multRect.x + 130 > mouse[0] > multRect.x and multRect.y + 130 > mouse[1] > multRect.y) and score >= upgradeCost:
			if click[0] == 1:
				score -= upgradeCost
				scoreMultiplier *= 2
				upgradeCost *= scoreMultiplier
				clickValue *= scoreMultiplier
				# reset left click[0] to 0
				click = pygame.mouse.get_pressed()
		
		# activate napkin if button is pressed
		if (deodorButtonRect.x + 130 > mouse[0] > deodorButtonRect.x and deodorButtonRect.y + 130 > mouse[1] > deodorButtonRect.y):
			if click[0] == 1:
				deodorButtonPressed = True
				# reset left click[0] to 0
				click = pygame.mouse.get_pressed()
		
		# if stinkyArray is empty, return to gameLoop()
		if len(stinkArray) == 0:
			pygame.mouse.set_visible(True)
			end = time.time()
			lapse = end - start
			print("end - start: ", end - start)
			if lapse >= 1 and lapse < 1.5:
				hpoints += 1
				happyMeter()
			if lapse >= 1.5 and lapse < 2:
				hpoints -= 1
				happyMeter()
			if lapse >= 2:
				hpoints -= 2
				happyMeter()
			return
				
		# decrement score (extreme decrease)
		score -= int(((50 * scoreMultiplier) / 5))
		
		# update the screen
		pygame.display.update()
		clock.tick(10)
		
# ===================== randomNumber() =============================
# returns a random number. This is called by the events and the
	# game loop.
# ==================================================================		

def randomNumber():
	# use current time as seed
	seed = int(time.time() % 60) + 1
		
	# seed the PRNG instance
	myGen.setSeed(seed)
		
	# generate the pseduo random number in range 1 to 100
	prn = (myGen.next_prn() % 100) + 1
		
	return prn

# ======================== getChance() =========================
# getChance triggers the events based on a random number.
# This number is multiplied by chance, based on the happy meter.
# ===============================================================

def getChance():
	# if score is a multiple of 50 (50 was picked arbitrarily), 
	# trigger random number generation
	if score % 50 == 0:
		randNum = randomNumber()
		print("Random number: ", randNum)
			
	# if random number is <= 50, trigger mudslide event
		if(randNum*chance <= 50):
			mudslide()
	#if random number is >= 70, trigger stinky event
		if(randNum*chance >= 70):
			stinky()

# ======================== happyMeter() =========================
# happyMeter changes the image of the the faces based on the 
# points. Chance is updated. Is called by events
# ===============================================================

def happyMeter():
	global hpoints
	global chance
	global mood
	
	#debuging:
	print("Happy points = ", hpoints)
	print("Chance = ", chance)
	
	if(hpoints <= 1):
		#load veryupset image
		mood = pygame.image.load("mood7.png")
		chance = 10
		return
	if(hpoints == 2):
		#load upset image
		mood = pygame.image.load("mood6.png")
		chance = 8
		return
	if(hpoints == 3):
		#load meh image
		mood = pygame.image.load("mood5.png")	
		chance = 6
		return
	if(hpoints == 4):
		#load neutral image
		mood = pygame.image.load("mood4.png")
		chance = 1.5
		return
	if(hpoints == 5):
		#load neutral_1 image
		mood = pygame.image.load("mood3.png")		
		chance = 1
		return
	if(hpoints == 6):
		#load happy image
		mood = pygame.image.load("mood2.png")
		chance = 0.5
		return
	if(hpoints >= 7):
		#load veryhappy image
		mood = pygame.image.load("mood1.png")
		chance = -1
		return
		
# ===================== gameLoop() =================================
# gameLoop() is the main game. It calls the events and the PRNG.
	# when the events finish, they return back to this loop.
	# This loop also plays the music.
# ==================================================================
def gameLoop():
	# reference global vars
	global score
	global scoreMultiplier
	global upgradeCost
	global clickValue
	global state
	
	# load background song #EPIC#
	pygame.mixer.music.load('song.mp3')
	# set volume of music
	pygame.mixer.music.set_volume(0.2)
	# play song repeatedly
	pygame.mixer.music.play(-1)
	
	# load background image
	background = pygame.image.load("blueBG.jpg")
	# create background rectangle
	backgroundRect = background.get_rect()
	
	# load shoe image
	shoe = pygame.image.load("sneaker.png")
	# create shoe utility object that represents the rectangular area
	shoeRect = shoe.get_rect()
	
	# load mood image
	global mood
	#create mood rectangle
	moodRect = mood.get_rect()
	
	# load napkin button - disabled
	napkin = pygame.image.load("napkinButtonDisabled.png")
	# create napkin rectangle
	napkinRect = napkin.get_rect()
	
	# load deodorant button
	deodorButton = pygame.image.load("spraycanButtonDisabled.png")
	# create deodorant rectangle
	deodorButtonRect = deodorButton.get_rect()
	
	# create a font object
	myfont = pygame.font.SysFont("monospace", 16)
	
	# set x,y position of shoe image on screen
	shoeRect.x = width * 0.07
	shoeRect.y = height * 0.15
		
	# set x,y position of napkin disabled image on screen
	napkinRect.x = width * 0.83
	napkinRect.y = height * 0.25
	
	# set x,y position of deodorant image on screen
	deodorButtonRect.x = width * 0.83
	deodorButtonRect.y = height * 0.49
	
	# set x,y position of mood image on screen
	moodRect.x = width * .33 #new
	moodRect.y = height * .01 #new
	
	while 1:
		# if exit button is pressed, close program
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			
			#check for pause
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					state = PAUSED
					pauseScreen()

	    # load multiplyer button
		if score >= upgradeCost:
			multiplier = pygame.image.load("x2Multiplier1.png")
		else : 
			multiplier = pygame.image.load("x2Multiplier1Disabled.png")
	    # create multiplyer rectangle
		multRect = multiplier.get_rect()

		# set x,y position of multiplier image on screen
		multRect.x = width * 0.83
		multRect.y = height * 0.01

		# draw images onto screen
		screen.blit(background, backgroundRect)
		screen.blit(shoe, shoeRect)
		screen.blit(multiplier, multRect)
		screen.blit(napkin, napkinRect)
		screen.blit(deodorButton, deodorButtonRect)
		screen.blit(mood, moodRect)
		
		# render text on screen
		scoretext = myfont.render("Score: {0}".format(score),1,(0,0,0))
		upgradetext = myfont.render("Upgrade Cost: {0}".format(upgradeCost),1,(0,0,0))
		multipliertext = myfont.render("Multiplier: x{0}".format(scoreMultiplier),1,(0,0,0))
		
		# draw text onto screen
		screen.blit(scoretext, (5,10))
		screen.blit(upgradetext, (5,30))
		screen.blit(multipliertext, (5,50))
		
		# get mouse position and click value
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		
		# add points to score when shoe image is clicked
		if shoeRect.x + 600 > mouse[0] > shoeRect.x and shoeRect.y + 510 > mouse[1] > shoeRect.y:
			if click[0] == 1:
				score += clickValue
				# reset left click[0] to 0
				click = pygame.mouse.get_pressed()
		
		# activate multiplier if button is pressed
		if (multRect.x + 130 > mouse[0] > multRect.x and multRect.y + 130 > mouse[1] > multRect.y) and score >= upgradeCost:
			if click[0] == 1:
				score -= upgradeCost
				scoreMultiplier *= 2
				upgradeCost *= scoreMultiplier
				clickValue *= scoreMultiplier
				# reset left click[0] to 0
				click = pygame.mouse.get_pressed()
		
		# call the chance function to determine event 
		if(score >= 1000 and upgradeCost >= 1000):
			getChance()
		
		# increment score
		score += 1
			
		# update the screen
		pygame.display.update()
		clock.tick(10)

def main():
	menu()	

if __name__ == "__main__":
	main()
