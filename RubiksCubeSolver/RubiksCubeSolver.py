import pygame, sys, math, time, os, copy 
from random import randint
from pygame import mixer
  
# initializes the mixer for in game sounds 
pygame.mixer.init()
# initializes all imported pygame modules
pygame.init()

# start playing the background music
pygame.mixer.music.load(os.path.join(os.getcwd(), 'assets', 'Loop.wav'))
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(loops=-1)  # loops forever

# width of the screen
width = 1920
# height of the screen
height = 1080

# initializes a window 
screen = pygame.display.set_mode(size = (width, height)) 

# Booleans used in the main loop
InMenu = True
InGame = True
NotValid = True

# ===== Assets ===== 

# Sky tiles
SkyWidth = 320
SkyHeight = math.floor((SkyWidth * 5) / 8)

sky1t = pygame.image.load('assets/sky0.png')
sky1 = pygame.transform.scale(sky1t, (SkyWidth, SkyHeight))

sky2t = pygame.image.load('assets/sky1.png')
sky2 = pygame.transform.scale(sky2t, (SkyWidth, SkyHeight))

sky3t = pygame.image.load('assets/sky2.png')
sky3 = pygame.transform.scale(sky3t, (SkyWidth, SkyHeight))

# Grass tiles 
GrassWidth = 250
GrassHeight = 140
grass1 = pygame.image.load('assets/Grass0.png')
grass2 = pygame.image.load('assets/Grass1.png')
grass3 = pygame.image.load('assets/Grass2.png')

# Menu Cube big
CubeFrame = 0
scalerC = 0.75
CubeWidth = math.floor(690 * scalerC)
CubeHeight = math.floor(800 * scalerC)
cube0t = pygame.image.load('assets/Cube0.png')
cube0 = pygame.transform.scale(cube0t, (CubeWidth, CubeHeight))
cube1t = pygame.image.load('assets/Cube1.png')
cube1 = pygame.transform.scale(cube1t, (CubeWidth, CubeHeight))
cube2t = pygame.image.load('assets/Cube2.png')
cube2 = pygame.transform.scale(cube2t, (CubeWidth, CubeHeight))

# Menu Cube small
scalerCs = 0.55
CubeWidths = math.floor(690 * scalerCs)
CubeHeights = math.floor(800 * scalerCs)
cube0s = pygame.transform.scale(cube0t, (CubeWidths, CubeHeights))
cube1s = pygame.transform.scale(cube1t, (CubeWidths, CubeHeights))
cube2s = pygame.transform.scale(cube2t, (CubeWidths, CubeHeights))

# Lists for the cubes sprite animations 
CubeLst = [cube0, cube1, cube2, cube1, cube0]
CubeLsts = [cube2s, cube1s, cube0s, cube1s, cube2s]

# Title in Menu
TitleWidth = 800
TitleHeight = math.floor(TitleWidth / 2)
Titlet0 = pygame.image.load('assets/TitleW.png')
Titlet1 = pygame.image.load('assets/TitleB.png')
Title = pygame.transform.scale(Titlet1, (TitleWidth, TitleHeight))
Title1 = pygame.transform.scale(Titlet0, (TitleWidth, TitleHeight))

# Menu Fire Animation
FireFrame = 0
scalerF = 0.75
FireWidth = math.floor(400*scalerF)
FireHeight = math.floor(400*scalerF)
Fire0t = pygame.image.load('assets/Fire0.png')
Fire0 = pygame.transform.scale(Fire0t, (FireWidth, FireHeight))
Fire1t = pygame.image.load('assets/Fire1.png')
Fire1 = pygame.transform.scale(Fire1t, (FireWidth, FireHeight))
Fire2t = pygame.image.load('assets/Fire2.png')
Fire2 = pygame.transform.scale(Fire2t, (FireWidth, FireHeight))
Fire3t = pygame.image.load('assets/Fire3.png')
Fire3 = pygame.transform.scale(Fire3t, (FireWidth, FireHeight))
Fire4t = pygame.image.load('assets/Fire4.png')
Fire4 = pygame.transform.scale(Fire4t, (FireWidth, FireHeight))
Fire5t = pygame.image.load('assets/Fire5.png')
Fire5 = pygame.transform.scale(Fire5t, (FireWidth, FireHeight))
Fire6t = pygame.image.load('assets/Fire6.png')
Fire6 = pygame.transform.scale(Fire6t, (FireWidth, FireHeight))
Fire7t = pygame.image.load('assets/Fire7.png')
Fire7 = pygame.transform.scale(Fire7t, (FireWidth, FireHeight))
Fire8t = pygame.image.load('assets/Fire8.png')
Fire8 = pygame.transform.scale(Fire8t, (FireWidth, FireHeight))
Fire9t = pygame.image.load('assets/Fire9.png')
Fire9 = pygame.transform.scale(Fire8t, (FireWidth, FireHeight))
Fire10t = pygame.image.load('assets/Fire10.png')
Fire10 = pygame.transform.scale(Fire10t, (FireWidth, FireHeight))
Fire11t = pygame.image.load('assets/Fire11.png')
Fire11 = pygame.transform.scale(Fire11t, (FireWidth, FireHeight))

# list for the fire sprite animation
FireLst = [Fire0, Fire1, Fire2, Fire3, Fire4, Fire5, Fire6, Fire7, Fire8, Fire9, Fire10, Fire11]

# The Glow of the Title 
light_t0 = pygame.image.load('assets/glow.png')
light_t1 = pygame.image.load('assets/GlowTitle.png')
light = pygame.transform.scale(light_t0, (width, height))
light1 = pygame.transform.scale(light_t1, (width, height))

# The 3d Face Selection indicator  
CubeSelWidth = 250
CubeSelHeight = CubeSelWidth
CubeEmptyt = pygame.image.load('assets/CubeEmpty.png')
CubeEmpty = pygame.transform.scale(CubeEmptyt, (CubeSelWidth, CubeSelHeight))
CubeTopt = pygame.image.load('assets/CubeTop.png')
CubeTop = pygame.transform.scale(CubeTopt, (CubeSelWidth, CubeSelHeight))
CubeBLt = pygame.image.load('assets/CubeBL.png')
CubeBL = pygame.transform.scale(CubeBLt, (CubeSelWidth, CubeSelHeight))
CubeBRt = pygame.image.load('assets/CubeBR.png')
CubeBR = pygame.transform.scale(CubeBRt, (CubeSelWidth, CubeSelHeight))
CubeFLt = pygame.image.load('assets/CubeFL.png')
CubeFL = pygame.transform.scale(CubeFLt, (CubeSelWidth, CubeSelHeight))
CubeFRt = pygame.image.load('assets/CubeFR.png')
CubeFR = pygame.transform.scale(CubeFRt, (CubeSelWidth, CubeSelHeight))
CubeBott = pygame.image.load('assets/CubeBot.png')
CubeBot = pygame.transform.scale(CubeBott, (CubeSelWidth, CubeSelHeight))

# The main Cube 
scalerCube = 5
CubeFoldWidth = 188*scalerCube
CubeFoldHeight = 141*scalerCube
CubeFoldt = pygame.image.load('assets/CubeFold.png')
CubeFold = pygame.transform.scale(CubeFoldt,(CubeFoldWidth, CubeFoldHeight))

# Solve Button 
scaleSBut = 0.75
SolveButtonWidth = math.floor(400*scaleSBut)
SolveButtonHeight = math.floor(146*scaleSBut)
SolveButt = pygame.image.load('assets/Solve.png')
SolveBut = pygame.transform.scale(SolveButt, (SolveButtonWidth, SolveButtonHeight))

# Scramble Button 
ScrambleBut = 0.75
ScrambleButtonWidth = math.floor(400*scaleSBut)
ScrambleButtonHeight = math.floor(146*scaleSBut)
ScrambleButt = pygame.image.load('assets/Scramble.png')
ScrambleBut = pygame.transform.scale(ScrambleButt, (ScrambleButtonWidth, ScrambleButtonHeight))

# Home Button 
scalerHome = 6
HomeButWidth = math.floor(11*scalerHome)
HomeButHeight = math.floor(7*scalerHome)
HomeButt = pygame.image.load('assets/Home.png')
HomeBut = pygame.transform.scale(HomeButt, (HomeButWidth, HomeButHeight))

# Sound Button 
scalerSound = 6
SoundOnWidth = math.floor(11*scalerHome)
SoundOnHeight = math.floor(7*scalerHome)
SoundOnt = pygame.image.load('assets/SoundON.png')
SoundOn = pygame.transform.scale(SoundOnt, (SoundOnWidth, SoundOnHeight))

# Top Title Bar 
scalerTitleBar = 0.25
TitleBarWidth = math.floor(250 * scalerTitleBar)
TitleBarHeight = TitleBarWidth
TitleBart = pygame.image.load('assets/TitleBar.png')
TitleBar = pygame.transform.scale(TitleBart, (TitleBarWidth, TitleBarHeight))

# Exit Button 
ScaleBut = 0.5
ExitWidth = math.floor(100 * ScaleBut)
ExitHeight = math.floor(110 * ScaleBut)
ExitButtont = pygame.image.load('assets/Exit.png')
ExitButton = pygame.transform.scale(ExitButtont, (ExitWidth, ExitHeight))

# Cube Stikers
StickerWidth = 13*scalerCube
StickerHeight = StickerWidth
Stickert = pygame.image.load('assets/Test.png')
Sticker = pygame.transform.scale(Stickert, (StickerWidth, StickerHeight))
StickerDt = pygame.image.load('assets/TestD.png')
StickerD = pygame.transform.scale(StickerDt, (StickerWidth, StickerHeight))
Redt = pygame.image.load('assets/Red.png')
Red = pygame.transform.scale(Redt, (StickerWidth, StickerHeight))
Bluet = pygame.image.load('assets/Blue.png')
Blue = pygame.transform.scale(Bluet, (StickerWidth, StickerHeight))
Greent = pygame.image.load('assets/Green.png')
Green = pygame.transform.scale(Greent, (StickerWidth, StickerHeight))
Whitet = pygame.image.load('assets/White.png')
White = pygame.transform.scale(Whitet, (StickerWidth, StickerHeight))
Yellowt = pygame.image.load('assets/Yellow.png')
Yellow = pygame.transform.scale(Yellowt, (StickerWidth, StickerHeight))
Oranget = pygame.image.load('assets/Orange.png')
Orange = pygame.transform.scale(Oranget, (StickerWidth, StickerHeight))

# Movement buttons 
MoveWidth = 100
MoveHeight = 100
UpButt = pygame.image.load('assets/Up.png')
UpBut = pygame.transform.scale(UpButt, (MoveWidth, MoveHeight))
UpIButt = pygame.image.load('assets/UpI.png')
UpIBut = pygame.transform.scale(UpIButt, (MoveWidth, MoveHeight))
DownButt = pygame.image.load('assets/Down.png')
DownBut = pygame.transform.scale(DownButt, (MoveWidth, MoveHeight))
DownIButt = pygame.image.load('assets/DownI.png')
DownIBut = pygame.transform.scale(DownIButt, (MoveWidth, MoveHeight))
LeftButt = pygame.image.load('assets/Left.png')
LeftBut = pygame.transform.scale(LeftButt, (MoveWidth, MoveHeight))
LeftIButt = pygame.image.load('assets/LeftI.png')
LeftIBut = pygame.transform.scale(LeftIButt, (MoveWidth, MoveHeight))
RightButt = pygame.image.load('assets/Right.png')
RightBut = pygame.transform.scale(RightButt, (MoveWidth, MoveHeight))
RightIButt = pygame.image.load('assets/RightI.png')
RightIBut = pygame.transform.scale(RightIButt, (MoveWidth, MoveHeight))
FrontButt = pygame.image.load('assets/Front.png')
FrontBut = pygame.transform.scale(FrontButt, (MoveWidth, MoveHeight))
FrontIButt = pygame.image.load('assets/FrontI.png')
FrontIBut = pygame.transform.scale(FrontIButt, (MoveWidth, MoveHeight))

#NotValidCube
CubeSignS = 0.6
CubeSignW = math.floor(728 * CubeSignS)
CubeSignH = math.floor(790 * CubeSignS)
CubeSignt = pygame.image.load('assets/CubeSign.png')
CubeSign = pygame.transform.scale(CubeSignt, (CubeSignW, CubeSignH))

# Returns a minimal list of random numbers
# Used as instructions for drawing the sky  
def SkyTiles(w, h, skyW, skyH):
	SkyHorzTile = math.ceil(w / skyW)
	SkyVerTile = math.ceil(h / skyH) 
	rand = [randint(1,3) for i in range(SkyHorzTile*SkyVerTile)]
	return rand

# Returns a minimal list of random numbers
# Used as instructions for drawing the grass 
def GrassTiles(w, GrassW):
	GrassHorzTile = math.ceil(w / GrassW)
	rand = [randint(1,3) for i in range(GrassHorzTile)]
	return rand

RandSky = SkyTiles(width, height, SkyWidth, SkyHeight)
RandGrass = GrassTiles(width, GrassWidth)

# Draws the sky using the instructions
def DrawSky():
	count = 0
	for y in range(0, height, SkyHeight):
		for x in range(0, width, SkyWidth):
			rand = RandSky[count]
			if rand == 1:
				screen.blit( sky1, (x,y))
			elif rand == 2:
				screen.blit( sky2, (x,y))
			elif rand == 3:
				screen.blit( sky3, (x,y))
			count = count + 1

TitleCount = 0

# Draws the correct title 
# Plays the correct music 
def title():
	global TitleCount, InMenu, GameMenu

	if Title.get_rect().collidepoint(pygame.mouse.get_pos()): # If the mouse is over the title 
		TitleCount += 1
		screen.blit(Title1, (50, 50))

		if TitleCount == 1: # Only play heaven sound when first hovered over
			pygame.mixer.Channel(0).play(pygame.mixer.Sound('assets/Heaven.wav'), maxtime=-1)
			pygame.mixer.Channel(0).set_volume(1) 

	else:  # Mouse is not over the title 
		TitleCount = 0
		screen.blit(Title, (50, 50))
		screen.blit(light, (0,0))
		pygame.mixer.Channel(0).set_volume(0)
		pygame.mixer.music.set_volume(0.5)

# The main menu function
# Draws assets and flags if the game is launched 
def MainMenu():
	global FireFrame, CubeFrame, InGame, InMenu, done

	DrawSky()

	# Draw Grass 
	count = 0
	for x in range(0, width, GrassWidth):
		rand = RandGrass[count]
		if rand == 1:
			screen.blit( grass2, (x, height-GrassHeight))
		elif rand == 2:
			screen.blit( grass2, (x, height-GrassHeight))
		elif rand == 3:
			screen.blit( grass3, (x, height-GrassHeight))
		count = count + 1

	# Draw Dancing Cubes
	screen.blit(CubeLst[math.ceil((CubeFrame%12)/3)], (width-CubeWidth, height-GrassHeight-CubeHeight+40))
	screen.blit(CubeLsts[math.ceil((CubeFrame%12)/3)], (width-CubeWidth-FireWidth-CubeWidths+80, height-GrassHeight-CubeHeights+40))
	CubeFrame = CubeFrame + 1

	# Draw Fire 
	screen.blit(FireLst[FireFrame%12], (width-CubeWidth-FireWidth+45, height-GrassHeight-FireHeight+95))
	FireFrame = FireFrame + 1

	# Draw Exit button
	screen.blit(ExitButton, (width-ExitWidth, 0))

	# Draw Title
	title()
	
	# Checks if the tile was clicked or if the exit button was clicked 
	for ev in pygame.event.get(): 
		if ev.type == pygame.MOUSEBUTTONDOWN:
			x, y = ev.pos
			if Title1.get_rect(topleft=(50, 50)).collidepoint(x, y):
				InMenu = False
				InGame = True
			elif ExitButton.get_rect(topleft=(width-ExitWidth, 0)).collidepoint(x, y):
				done = True

# CubeClick[0][i] = Green face 
# CubeClick[1][i] = white face 
# CubeClick[2][i] = blue face 
# CubeClick[3][i] = yellow face 
# CubeClick[4][i] = orange face 
# CubeClick[5][i] = red face 
# 0 -> green, 1 -> white, 2 -> blue, 3 -> yellow, 4 -> orange, 5 -> red    

CubeClick = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
			 [1, 1, 1, 1, 1, 1, 1, 1, 1],
			 [2, 2, 2, 2, 2, 2, 2, 2, 2],
			 [3, 3, 3, 3, 3, 3, 3, 3, 3],
			 [4, 4, 4, 4, 4, 4, 4, 4, 4],
			 [5, 5, 5, 5, 5, 5, 5, 5, 5]]

# Draws a highlight on the sticker your mouse is over 
def StickerSel(y, cubeDisX, cubeDisY, xdis1, ydis1): 
	if y > cubeDisY+ydis1 and y < cubeDisY+ydis1+65:
		screen.blit(Sticker, (cubeDisX + xdis1, cubeDisY+ydis1))
	elif y > cubeDisY+ydis1+65+10 and y < cubeDisY+ydis1+65+10+65:
		screen.blit(Sticker, (cubeDisX + xdis1, cubeDisY+ydis1+65+10))
	elif y > cubeDisY+ydis1+65+10+65+10 and y < cubeDisY+ydis1+65+10+65+10+65:
		screen.blit(Sticker, (cubeDisX + xdis1, cubeDisY+ydis1+65+10+65+10)) 

# Draws the sticks based off the input cube index values
def DrawStick(i, j, cubeDisX, cubeDisY, DisX, DisY):
	if CubeClick[i][j]%6 == 0:
		screen.blit(Green, (cubeDisX + DisX, cubeDisY+DisY))
	elif CubeClick[i][j]%6 == 1:
		screen.blit(White, (cubeDisX + DisX, cubeDisY+DisY))
	elif CubeClick[i][j]%6 == 2:
		screen.blit(Blue, (cubeDisX + DisX, cubeDisY+DisY))
	elif CubeClick[i][j]%6 == 3:
		screen.blit(Yellow, (cubeDisX + DisX, cubeDisY+DisY))
	elif CubeClick[i][j]%6 == 4:
		screen.blit(Orange, (cubeDisX + DisX, cubeDisY+DisY))
	elif CubeClick[i][j]%6 == 5:
		screen.blit(Red, (cubeDisX + DisX, cubeDisY+DisY))

GameMenuCount = 1
			  
# Verifies that the scramble input is valid
def CubeCheck():
	global NotValid, InGame
	
	edge = 0 # num or correct edges 

	# Check Edges 
	if CubeClick[0][1]%6==0 and (CubeClick[3][7]%6==3 or CubeClick[3][7]%6==4 or CubeClick[3][7]%6==1 or CubeClick[3][7]%6==5):
		edge += 1
		#print('1')
	elif CubeClick[0][1]%6==3 and (CubeClick[3][7]%6==5 or CubeClick[3][7]%6==4 or CubeClick[3][7]%6==2 or CubeClick[3][7]%6==0):
		edge += 1
		#print('1')
	elif CubeClick[0][1]%6==1 and (CubeClick[3][7]%6==5 or CubeClick[3][7]%6==4 or CubeClick[3][7]%6==2 or CubeClick[3][7]%6==0):
		edge += 1
		#print('1')
	elif CubeClick[0][1]%6==2 and (CubeClick[3][7]%6==3 or CubeClick[3][7]%6==4 or CubeClick[3][7]%6==1 or CubeClick[3][7]%6==5):
		edge += 1
		#print('1')
	elif CubeClick[0][1]%6==4 and (CubeClick[3][7]%6==0 or CubeClick[3][7]%6==1 or CubeClick[3][7]%6==2 or CubeClick[3][7]%6==3):
		edge += 1
		#print('1')
	elif CubeClick[0][1]%6==5 and (CubeClick[3][7]%6==0 or CubeClick[3][7]%6==1 or CubeClick[3][7]%6==2 or CubeClick[3][7]%6==3):
		edge += 1
		#print('1')

	if CubeClick[0][3]%6==0 and (CubeClick[4][1]%6==3 or CubeClick[4][1]%6==4 or CubeClick[4][1]%6==1 or CubeClick[4][1]%6==5):
		edge += 1
		#print('2')
	elif CubeClick[0][3]%6==3 and (CubeClick[4][1]%6==5 or CubeClick[4][1]%6==4 or CubeClick[4][1]%6==2 or CubeClick[4][1]%6==0):
		edge += 1
		#print('2')
	elif CubeClick[0][3]%6==1 and (CubeClick[4][1]%6==5 or CubeClick[4][1]%6==4 or CubeClick[4][1]%6==2 or CubeClick[4][1]%6==0):
		edge += 1
		#print('2')
	elif CubeClick[0][3]%6==2 and (CubeClick[4][1]%6==3 or CubeClick[4][1]%6==4 or CubeClick[4][1]%6==1 or CubeClick[4][1]%6==5):
		edge += 1
		#print('2')
	elif CubeClick[0][3]%6==4 and (CubeClick[4][1]%6==0 or CubeClick[4][1]%6==1 or CubeClick[4][1]%6==2 or CubeClick[4][1]%6==3):
		edge += 1
		#print('2')
	elif CubeClick[0][3]%6==5 and (CubeClick[4][1]%6==0 or CubeClick[4][1]%6==1 or CubeClick[4][1]%6==2 or CubeClick[4][1]%6==3):
		edge += 1
		#print('2')

	if CubeClick[0][7]%6==0 and (CubeClick[1][1]%6==3 or CubeClick[1][1]%6==4 or CubeClick[1][1]%6==1 or CubeClick[1][1]%6==5):
		edge += 1
		#print('3')
	elif CubeClick[0][7]%6==3 and (CubeClick[1][1]%6==5 or CubeClick[1][1]%6==4 or CubeClick[1][1]%6==2 or CubeClick[1][1]%6==0):
		edge += 1
		#print('3')
	elif CubeClick[0][7]%6==1 and (CubeClick[1][1]%6==5 or CubeClick[1][1]%6==4 or CubeClick[1][1]%6==2 or CubeClick[1][1]%6==0):
		edge += 1
		#print('3')
	elif CubeClick[0][7]%6==2 and (CubeClick[1][1]%6==3 or CubeClick[1][1]%6==4 or CubeClick[1][1]%6==1 or CubeClick[1][1]%6==5):
		edge += 1
		#print('3')
	elif CubeClick[0][7]%6==4 and (CubeClick[1][1]%6==0 or CubeClick[1][1]%6==1 or CubeClick[1][1]%6==2 or CubeClick[1][1]%6==3):
		edge += 1
		#print('3')
	elif CubeClick[0][7]%6==5 and (CubeClick[1][1]%6==0 or CubeClick[1][1]%6==1 or CubeClick[1][1]%6==2 or CubeClick[1][1]%6==3):
		edge += 1
		#print('3')

	if CubeClick[0][5]%6==0 and (CubeClick[5][1]%6==3 or CubeClick[5][1]%6==4 or CubeClick[5][1]%6==1 or CubeClick[5][1]%6==5):
		edge += 1
		#print('4')
	elif CubeClick[0][5]%6==3 and (CubeClick[5][1]%6==5 or CubeClick[5][1]%6==4 or CubeClick[5][1]%6==2 or CubeClick[5][1]%6==0):
		edge += 1
		#print('4')
	elif CubeClick[0][5]%6==1 and (CubeClick[5][1]%6==5 or CubeClick[5][1]%6==4 or CubeClick[5][1]%6==2 or CubeClick[5][1]%6==0):
		edge += 1
		#print('4') 
	elif CubeClick[0][5]%6==2 and (CubeClick[5][1]%6==3 or CubeClick[5][1]%6==4 or CubeClick[5][1]%6==1 or CubeClick[5][1]%6==5):
		edge += 1
		#print('4')
	elif CubeClick[0][5]%6==4 and (CubeClick[5][1]%6==0 or CubeClick[5][1]%6==1 or CubeClick[5][1]%6==2 or CubeClick[5][1]%6==3):
		edge += 1
		#print('4')
	elif CubeClick[0][5]%6==5 and (CubeClick[5][1]%6==0 or CubeClick[5][1]%6==1 or CubeClick[5][1]%6==2 or CubeClick[5][1]%6==3):
		edge += 1
		#print('4')

	if CubeClick[3][1]%6==0 and (CubeClick[2][7]%6==3 or CubeClick[2][7]%6==4 or CubeClick[2][7]%6==1 or CubeClick[2][7]%6==5):
		edge += 1
		#print('5')
	elif CubeClick[3][1]%6==3 and (CubeClick[2][7]%6==5 or CubeClick[2][7]%6==4 or CubeClick[2][7]%6==2 or CubeClick[2][7]%6==0):
		edge += 1
		#print('5')
	elif CubeClick[3][1]%6==1 and (CubeClick[2][7]%6==5 or CubeClick[2][7]%6==4 or CubeClick[2][7]%6==2 or CubeClick[2][7]%6==0):
		edge += 1
		#print('5')
	elif CubeClick[3][1]%6==2 and (CubeClick[2][7]%6==3 or CubeClick[2][7]%6==4 or CubeClick[2][7]%6==1 or CubeClick[2][7]%6==5):
		edge += 1
		#print('5')
	elif CubeClick[3][1]%6==4 and (CubeClick[2][7]%6==0 or CubeClick[2][7]%6==1 or CubeClick[2][7]%6==2 or CubeClick[2][7]%6==3):
		edge += 1
		#print('5')
	elif CubeClick[3][1]%6==5 and (CubeClick[2][7]%6==0 or CubeClick[2][7]%6==1 or CubeClick[2][7]%6==2 or CubeClick[2][7]%6==3):
		edge += 1
		#print('5')

	if CubeClick[3][3]%6==0 and (CubeClick[4][3]%6==3 or CubeClick[4][3]%6==4 or CubeClick[4][3]%6==1 or CubeClick[4][3]%6==5):
		edge += 1
		#print('6')
	elif CubeClick[3][3]%6==3 and (CubeClick[4][3]%6==5 or CubeClick[4][3]%6==4 or CubeClick[4][3]%6==2 or CubeClick[4][3]%6==0):
		edge += 1
		#print('6')
	elif CubeClick[3][3]%6==1 and (CubeClick[4][3]%6==5 or CubeClick[4][3]%6==4 or CubeClick[4][3]%6==2 or CubeClick[4][3]%6==0):
		edge += 1
		#print('6')
	elif CubeClick[3][3]%6==2 and (CubeClick[4][3]%6==3 or CubeClick[4][3]%6==4 or CubeClick[4][3]%6==1 or CubeClick[4][3]%6==5):
		edge += 1
		#print('6')
	elif CubeClick[3][3]%6==4 and (CubeClick[4][3]%6==0 or CubeClick[4][3]%6==1 or CubeClick[4][3]%6==2 or CubeClick[4][3]%6==3):
		edge += 1
		#print('6')
	elif CubeClick[3][3]%6==5 and (CubeClick[4][3]%6==0 or CubeClick[4][3]%6==1 or CubeClick[4][3]%6==2 or CubeClick[4][3]%6==3):
		edge += 1
		#print('6')

	if CubeClick[3][5]%6==0 and (CubeClick[5][5]%6==3 or CubeClick[5][5]%6==4 or CubeClick[5][5]%6==1 or CubeClick[5][5]%6==5):
		edge += 1
		#print('7')
	elif CubeClick[3][5]%6==3 and (CubeClick[5][5]%6==5 or CubeClick[5][5]%6==4 or CubeClick[5][5]%6==2 or CubeClick[5][5]%6==0):
		edge += 1
		#print('7')
	elif CubeClick[3][5]%6==1 and (CubeClick[5][5]%6==5 or CubeClick[5][5]%6==4 or CubeClick[5][5]%6==2 or CubeClick[5][5]%6==0):
		edge += 1
		#print('7')
	elif CubeClick[3][5]%6==2 and (CubeClick[5][5]%6==3 or CubeClick[5][5]%6==4 or CubeClick[5][5]%6==1 or CubeClick[5][5]%6==5):
		edge += 1
		#print('7')
	elif CubeClick[3][5]%6==4 and (CubeClick[5][5]%6==0 or CubeClick[5][5]%6==1 or CubeClick[5][5]%6==2 or CubeClick[5][5]%6==3):
		edge += 1
		#print('7')
	elif CubeClick[3][5]%6==5 and (CubeClick[5][5]%6==0 or CubeClick[5][5]%6==1 or CubeClick[5][5]%6==2 or CubeClick[5][5]%6==3):
		edge += 1
		#print('7')

	if CubeClick[1][7]%6==0 and (CubeClick[2][1]%6==3 or CubeClick[2][1]%6==4 or CubeClick[2][1]%6==1 or CubeClick[2][1]%6==5):
		edge += 1
		#print('8')
	elif CubeClick[1][7]%6==3 and (CubeClick[2][1]%6==5 or CubeClick[2][1]%6==4 or CubeClick[2][1]%6==2 or CubeClick[2][1]%6==0):
		edge += 1
		#print('8')
	elif CubeClick[1][7]%6==1 and (CubeClick[2][1]%6==5 or CubeClick[2][1]%6==4 or CubeClick[2][1]%6==2 or CubeClick[2][1]%6==0):
		edge += 1
		#print('8')
	elif CubeClick[1][7]%6==2 and (CubeClick[2][1]%6==3 or CubeClick[2][1]%6==4 or CubeClick[2][1]%6==1 or CubeClick[2][1]%6==5):
		edge += 1
		#print('8')
	elif CubeClick[1][7]%6==4 and (CubeClick[2][1]%6==0 or CubeClick[2][1]%6==1 or CubeClick[2][1]%6==2 or CubeClick[2][1]%6==3):
		edge += 1
		#print('8')
	elif CubeClick[1][7]%6==5 and (CubeClick[2][1]%6==0 or CubeClick[2][1]%6==1 or CubeClick[2][1]%6==2 or CubeClick[2][1]%6==3):
		edge += 1
		#print('8')

	if CubeClick[1][3]%6==0 and (CubeClick[4][5]%6==3 or CubeClick[4][5]%6==4 or CubeClick[4][5]%6==1 or CubeClick[4][5]%6==5):
		edge += 1
		#print('9')
	elif CubeClick[1][3]%6==3 and (CubeClick[4][5]%6==5 or CubeClick[4][5]%6==4 or CubeClick[4][5]%6==2 or CubeClick[4][5]%6==0):
		edge += 1
		#print('9')
	elif CubeClick[1][3]%6==1 and (CubeClick[4][5]%6==5 or CubeClick[4][5]%6==4 or CubeClick[4][5]%6==2 or CubeClick[4][5]%6==0):
		edge += 1
		#print('9')
	elif CubeClick[1][3]%6==2 and (CubeClick[4][5]%6==3 or CubeClick[4][5]%6==4 or CubeClick[4][5]%6==1 or CubeClick[4][5]%6==5):
		edge += 1
		#print('9')
	elif CubeClick[1][3]%6==4 and (CubeClick[4][5]%6==0 or CubeClick[4][5]%6==1 or CubeClick[4][5]%6==2 or CubeClick[4][5]%6==3):
		edge += 1
		#print('9')
	elif CubeClick[1][3]%6==5 and (CubeClick[4][5]%6==0 or CubeClick[4][5]%6==1 or CubeClick[4][5]%6==2 or CubeClick[4][5]%6==3):
		edge += 1
		#print('9')

	if CubeClick[1][5]%6==0 and (CubeClick[5][3]%6==3 or CubeClick[5][3]%6==4 or CubeClick[5][3]%6==1 or CubeClick[5][3]%6==5):
		edge += 1
		#print('10')
	elif CubeClick[1][5]%6==3 and (CubeClick[5][3]%6==5 or CubeClick[5][3]%6==4 or CubeClick[5][3]%6==2 or CubeClick[5][3]%6==0):
		edge += 1
		#print('10')
	elif CubeClick[1][5]%6==1 and (CubeClick[5][3]%6==5 or CubeClick[5][3]%6==4 or CubeClick[5][3]%6==2 or CubeClick[5][3]%6==0):
		edge += 1
		#print('10')
	elif CubeClick[1][5]%6==2 and (CubeClick[5][3]%6==3 or CubeClick[5][3]%6==4 or CubeClick[5][3]%6==1 or CubeClick[5][3]%6==5):
		edge += 1
		#print('10')
	elif CubeClick[1][5]%6==4 and (CubeClick[5][3]%6==0 or CubeClick[5][3]%6==1 or CubeClick[5][3]%6==2 or CubeClick[5][3]%6==3):
		edge += 1
		#print('10')
	elif CubeClick[1][5]%6==5 and (CubeClick[3][5]%6==0 or CubeClick[3][5]%6==1 or CubeClick[3][5]%6==2 or CubeClick[5][3]%6==3):
		edge += 1
		#print('10')

	if CubeClick[2][3]%6==0 and (CubeClick[4][7]%6==3 or CubeClick[4][7]%6==4 or CubeClick[4][7]%6==1 or CubeClick[4][7]%6==5):
		edge += 1
		#print('11')
	elif CubeClick[2][3]%6==3 and (CubeClick[4][7]%6==5 or CubeClick[4][7]%6==4 or CubeClick[4][7]%6==2 or CubeClick[4][7]%6==0):
		edge += 1
		#print('11')
	elif CubeClick[2][3]%6==1 and (CubeClick[4][7]%6==5 or CubeClick[4][7]%6==4 or CubeClick[4][7]%6==2 or CubeClick[4][7]%6==0):
		edge += 1
		#print('11')
	elif CubeClick[2][3]%6==2 and (CubeClick[4][7]%6==3 or CubeClick[4][7]%6==4 or CubeClick[4][7]%6==1 or CubeClick[4][7]%6==5):
		edge += 1
		#print('11')
	elif CubeClick[2][3]%6==4 and (CubeClick[4][7]%6==0 or CubeClick[4][7]%6==1 or CubeClick[4][7]%6==2 or CubeClick[4][7]%6==3):
		edge += 1
		#print('11')
	elif CubeClick[2][3]%6==5 and (CubeClick[4][7]%6==0 or CubeClick[4][7]%6==1 or CubeClick[4][7]%6==2 or CubeClick[4][7]%6==3):
		edge += 1
		#print('11')

	if CubeClick[2][5]%6==0 and (CubeClick[5][7]%6==3 or CubeClick[5][7]%6==4 or CubeClick[5][7]%6==1 or CubeClick[5][7]%6==5):
		edge += 1
		#print('12')
	elif CubeClick[2][5]%6==3 and (CubeClick[5][7]%6==5 or CubeClick[5][7]%6==4 or CubeClick[5][7]%6==2 or CubeClick[5][7]%6==0):
		edge += 1
		#print('12')
	elif CubeClick[2][5]%6==1 and (CubeClick[5][7]%6==5 or CubeClick[5][7]%6==4 or CubeClick[5][7]%6==2 or CubeClick[5][7]%6==0):
		edge += 1
		#print('12')
	elif CubeClick[2][5]%6==2 and (CubeClick[5][7]%6==3 or CubeClick[5][7]%6==4 or CubeClick[5][7]%6==1 or CubeClick[5][7]%6==5):
		edge += 1
		#print('12')
	elif CubeClick[2][5]%6==4 and (CubeClick[5][7]%6==0 or CubeClick[5][7]%6==1 or CubeClick[5][7]%6==2 or CubeClick[5][7]%6==3):
		edge += 1
		#print('12')
	elif CubeClick[2][5]%6==5 and (CubeClick[5][7]%6==0 or CubeClick[5][7]%6==1 or CubeClick[5][7]%6==2 or CubeClick[5][7]%6==3):
		edge += 1
		#print('12')

	Corner = 0
	if ((CubeClick[0][0]%6==0 and CubeClick[3][6]%6==3 and CubeClick[4][0]%6==4) or 
	   (CubeClick[0][0]%6==0 and CubeClick[3][6]%6==1 and CubeClick[4][0]%6==5) or 
	   (CubeClick[0][0]%6==0 and CubeClick[3][6]%6==4 and CubeClick[4][0]%6==1) or 
	   (CubeClick[0][0]%6==0 and CubeClick[3][6]%6==5 and CubeClick[4][0]%6==3) or 
	   (CubeClick[0][0]%6==1 and CubeClick[3][6]%6==0 and CubeClick[4][0]%6==4) or 
	   (CubeClick[0][0]%6==1 and CubeClick[3][6]%6==5 and CubeClick[4][0]%6==0) or 
	   (CubeClick[0][0]%6==1 and CubeClick[3][6]%6==4 and CubeClick[4][0]%6==2) or 
	   (CubeClick[0][0]%6==1 and CubeClick[3][6]%6==2 and CubeClick[4][0]%6==5) or 
	   (CubeClick[0][0]%6==2 and CubeClick[3][6]%6==1 and CubeClick[4][0]%6==4) or 
	   (CubeClick[0][0]%6==2 and CubeClick[3][6]%6==3 and CubeClick[4][0]%6==5) or 
	   (CubeClick[0][0]%6==2 and CubeClick[3][6]%6==4 and CubeClick[4][0]%6==3) or 
	   (CubeClick[0][0]%6==2 and CubeClick[3][6]%6==5 and CubeClick[4][0]%6==1) or 
	   (CubeClick[0][0]%6==3 and CubeClick[3][6]%6==0 and CubeClick[4][0]%6==5) or 
	   (CubeClick[0][0]%6==3 and CubeClick[3][6]%6==4 and CubeClick[4][0]%6==0) or 
	   (CubeClick[0][0]%6==3 and CubeClick[3][6]%6==5 and CubeClick[4][0]%6==2) or 
	   (CubeClick[0][0]%6==3 and CubeClick[3][6]%6==2 and CubeClick[4][0]%6==4) or 
	   (CubeClick[0][0]%6==4 and CubeClick[3][6]%6==0 and CubeClick[4][0]%6==3) or 
	   (CubeClick[0][0]%6==4 and CubeClick[3][6]%6==3 and CubeClick[4][0]%6==2) or 
	   (CubeClick[0][0]%6==4 and CubeClick[3][6]%6==2 and CubeClick[4][0]%6==1) or 
	   (CubeClick[0][0]%6==4 and CubeClick[3][6]%6==1 and CubeClick[4][0]%6==0) or 
	   (CubeClick[0][0]%6==5 and CubeClick[3][6]%6==1 and CubeClick[4][0]%6==2) or 
	   (CubeClick[0][0]%6==5 and CubeClick[3][6]%6==3 and CubeClick[4][0]%6==0) or 
	   (CubeClick[0][0]%6==5 and CubeClick[3][6]%6==0 and CubeClick[4][0]%6==1) or 
	   (CubeClick[0][0]%6==5 and CubeClick[3][6]%6==2 and CubeClick[4][0]%6==3)):
		Corner += 1

	if ((CubeClick[0][6]%6==0 and CubeClick[1][0]%6==4 and CubeClick[4][2]%6==3) or 
	   (CubeClick[0][6]%6==0 and CubeClick[1][0]%6==3 and CubeClick[4][2]%6==5) or 
	   (CubeClick[0][6]%6==0 and CubeClick[1][0]%6==5 and CubeClick[4][2]%6==1) or 
	   (CubeClick[0][6]%6==0 and CubeClick[1][0]%6==1 and CubeClick[4][2]%6==4) or 
	   (CubeClick[0][6]%6==1 and CubeClick[1][0]%6==0 and CubeClick[4][2]%6==5) or 
	   (CubeClick[0][6]%6==1 and CubeClick[1][0]%6==5 and CubeClick[4][2]%6==2) or 
	   (CubeClick[0][6]%6==1 and CubeClick[1][0]%6==4 and CubeClick[4][2]%6==0) or 
	   (CubeClick[0][6]%6==1 and CubeClick[1][0]%6==2 and CubeClick[4][2]%6==4) or 
	   (CubeClick[0][6]%6==2 and CubeClick[1][0]%6==1 and CubeClick[4][2]%6==5) or 
	   (CubeClick[0][6]%6==2 and CubeClick[1][0]%6==3 and CubeClick[4][2]%6==4) or 
	   (CubeClick[0][6]%6==2 and CubeClick[1][0]%6==4 and CubeClick[4][2]%6==1) or 
	   (CubeClick[0][6]%6==2 and CubeClick[1][0]%6==5 and CubeClick[4][2]%6==3) or 
	   (CubeClick[0][6]%6==3 and CubeClick[1][0]%6==2 and CubeClick[4][2]%6==5) or 
	   (CubeClick[0][6]%6==3 and CubeClick[1][0]%6==4 and CubeClick[4][2]%6==2) or 
	   (CubeClick[0][6]%6==3 and CubeClick[1][0]%6==0 and CubeClick[4][2]%6==4) or 
	   (CubeClick[0][6]%6==3 and CubeClick[1][0]%6==5 and CubeClick[4][2]%6==0) or 
	   (CubeClick[0][6]%6==4 and CubeClick[1][0]%6==2 and CubeClick[4][2]%6==3) or 
	   (CubeClick[0][6]%6==4 and CubeClick[1][0]%6==1 and CubeClick[4][2]%6==2) or 
	   (CubeClick[0][6]%6==4 and CubeClick[1][0]%6==0 and CubeClick[4][2]%6==1) or 
	   (CubeClick[0][6]%6==4 and CubeClick[1][0]%6==3 and CubeClick[4][2]%6==0) or 
	   (CubeClick[0][6]%6==5 and CubeClick[1][0]%6==0 and CubeClick[4][2]%6==3) or 
	   (CubeClick[0][6]%6==5 and CubeClick[1][0]%6==1 and CubeClick[4][2]%6==0) or 
	   (CubeClick[0][6]%6==5 and CubeClick[1][0]%6==3 and CubeClick[4][2]%6==2) or 
	   (CubeClick[0][6]%6==5 and CubeClick[1][0]%6==2 and CubeClick[4][2]%6==1)):
		Corner += 1

	if ((CubeClick[0][2]%6==0 and CubeClick[5][2]%6==3 and CubeClick[3][8]%6==4) or 
	   (CubeClick[0][2]%6==0 and CubeClick[5][2]%6==1 and CubeClick[3][8]%6==5) or 
	   (CubeClick[0][2]%6==0 and CubeClick[5][2]%6==4 and CubeClick[3][8]%6==1) or 
	   (CubeClick[0][2]%6==0 and CubeClick[5][2]%6==5 and CubeClick[3][8]%6==3) or 
	   (CubeClick[0][2]%6==1 and CubeClick[5][2]%6==0 and CubeClick[3][8]%6==4) or 
	   (CubeClick[0][2]%6==1 and CubeClick[5][2]%6==5 and CubeClick[3][8]%6==0) or 
	   (CubeClick[0][2]%6==1 and CubeClick[5][2]%6==4 and CubeClick[3][8]%6==2) or 
	   (CubeClick[0][2]%6==1 and CubeClick[5][2]%6==2 and CubeClick[3][8]%6==5) or 
	   (CubeClick[0][2]%6==2 and CubeClick[5][2]%6==1 and CubeClick[3][8]%6==4) or 
	   (CubeClick[0][2]%6==2 and CubeClick[5][2]%6==3 and CubeClick[3][8]%6==5) or 
	   (CubeClick[0][2]%6==2 and CubeClick[5][2]%6==4 and CubeClick[3][8]%6==3) or 
	   (CubeClick[0][2]%6==2 and CubeClick[5][2]%6==5 and CubeClick[3][8]%6==1) or 
	   (CubeClick[0][2]%6==3 and CubeClick[5][2]%6==0 and CubeClick[3][8]%6==5) or 
	   (CubeClick[0][2]%6==3 and CubeClick[5][2]%6==4 and CubeClick[3][8]%6==0) or 
	   (CubeClick[0][2]%6==3 and CubeClick[5][2]%6==5 and CubeClick[3][8]%6==2) or 
	   (CubeClick[0][2]%6==3 and CubeClick[5][2]%6==2 and CubeClick[3][8]%6==4) or 
	   (CubeClick[0][2]%6==4 and CubeClick[5][2]%6==0 and CubeClick[3][8]%6==3) or 
	   (CubeClick[0][2]%6==4 and CubeClick[5][2]%6==3 and CubeClick[3][8]%6==2) or 
	   (CubeClick[0][2]%6==4 and CubeClick[5][2]%6==2 and CubeClick[3][8]%6==1) or 
	   (CubeClick[0][2]%6==4 and CubeClick[5][2]%6==1 and CubeClick[3][8]%6==0) or 
	   (CubeClick[0][2]%6==5 and CubeClick[5][2]%6==1 and CubeClick[3][8]%6==2) or 
	   (CubeClick[0][2]%6==5 and CubeClick[5][2]%6==3 and CubeClick[3][8]%6==0) or 
	   (CubeClick[0][2]%6==5 and CubeClick[5][2]%6==0 and CubeClick[3][8]%6==1) or 
	   (CubeClick[0][2]%6==5 and CubeClick[5][2]%6==2 and CubeClick[3][8]%6==3)):
		Corner += 1

	if ((CubeClick[0][8]%6==0 and CubeClick[5][0]%6==4 and CubeClick[1][2]%6==3) or 
	   (CubeClick[0][8]%6==0 and CubeClick[5][0]%6==3 and CubeClick[1][2]%6==5) or 
	   (CubeClick[0][8]%6==0 and CubeClick[5][0]%6==5 and CubeClick[1][2]%6==1) or 
	   (CubeClick[0][8]%6==0 and CubeClick[5][0]%6==1 and CubeClick[1][2]%6==4) or 
	   (CubeClick[0][8]%6==1 and CubeClick[5][0]%6==0 and CubeClick[1][2]%6==5) or 
	   (CubeClick[0][8]%6==1 and CubeClick[5][0]%6==5 and CubeClick[1][2]%6==2) or 
	   (CubeClick[0][8]%6==1 and CubeClick[5][0]%6==4 and CubeClick[1][2]%6==0) or 
	   (CubeClick[0][8]%6==1 and CubeClick[5][0]%6==2 and CubeClick[1][2]%6==4) or 
	   (CubeClick[0][8]%6==2 and CubeClick[5][0]%6==1 and CubeClick[1][2]%6==5) or 
	   (CubeClick[0][8]%6==2 and CubeClick[5][0]%6==3 and CubeClick[1][2]%6==4) or 
	   (CubeClick[0][8]%6==2 and CubeClick[5][0]%6==4 and CubeClick[1][2]%6==1) or 
	   (CubeClick[0][8]%6==2 and CubeClick[5][0]%6==5 and CubeClick[1][2]%6==3) or 
	   (CubeClick[0][8]%6==3 and CubeClick[5][0]%6==2 and CubeClick[1][2]%6==5) or 
	   (CubeClick[0][8]%6==3 and CubeClick[5][0]%6==4 and CubeClick[1][2]%6==2) or 
	   (CubeClick[0][8]%6==3 and CubeClick[5][0]%6==0 and CubeClick[1][2]%6==4) or 
	   (CubeClick[0][8]%6==3 and CubeClick[5][0]%6==5 and CubeClick[1][2]%6==0) or 
	   (CubeClick[0][8]%6==4 and CubeClick[5][0]%6==2 and CubeClick[1][2]%6==3) or 
	   (CubeClick[0][8]%6==4 and CubeClick[5][0]%6==1 and CubeClick[1][2]%6==2) or 
	   (CubeClick[0][8]%6==4 and CubeClick[5][0]%6==0 and CubeClick[1][2]%6==1) or 
	   (CubeClick[0][8]%6==4 and CubeClick[5][0]%6==3 and CubeClick[1][2]%6==0) or 
	   (CubeClick[0][8]%6==5 and CubeClick[5][0]%6==0 and CubeClick[1][2]%6==3) or 
	   (CubeClick[0][8]%6==5 and CubeClick[5][0]%6==1 and CubeClick[1][2]%6==0) or 
	   (CubeClick[0][8]%6==5 and CubeClick[5][0]%6==3 and CubeClick[1][2]%6==2) or 
	   (CubeClick[0][8]%6==5 and CubeClick[5][0]%6==2 and CubeClick[1][2]%6==1)):
		Corner += 1

	if ((CubeClick[2][0]%6==0 and CubeClick[1][6]%6==3 and CubeClick[4][8]%6==4) or 
	   (CubeClick[2][0]%6==0 and CubeClick[1][6]%6==1 and CubeClick[4][8]%6==5) or 
	   (CubeClick[2][0]%6==0 and CubeClick[1][6]%6==4 and CubeClick[4][8]%6==1) or 
	   (CubeClick[2][0]%6==0 and CubeClick[1][6]%6==5 and CubeClick[4][8]%6==3) or 
	   (CubeClick[2][0]%6==1 and CubeClick[1][6]%6==0 and CubeClick[4][8]%6==4) or 
	   (CubeClick[2][0]%6==1 and CubeClick[1][6]%6==5 and CubeClick[4][8]%6==0) or 
	   (CubeClick[2][0]%6==1 and CubeClick[1][6]%6==4 and CubeClick[4][8]%6==2) or 
	   (CubeClick[2][0]%6==1 and CubeClick[1][6]%6==2 and CubeClick[4][8]%6==5) or 
	   (CubeClick[2][0]%6==2 and CubeClick[1][6]%6==1 and CubeClick[4][8]%6==4) or 
	   (CubeClick[2][0]%6==2 and CubeClick[1][6]%6==3 and CubeClick[4][8]%6==5) or 
	   (CubeClick[2][0]%6==2 and CubeClick[1][6]%6==4 and CubeClick[4][8]%6==3) or 
	   (CubeClick[2][0]%6==2 and CubeClick[1][6]%6==5 and CubeClick[4][8]%6==1) or 
	   (CubeClick[2][0]%6==3 and CubeClick[1][6]%6==0 and CubeClick[4][8]%6==5) or 
	   (CubeClick[2][0]%6==3 and CubeClick[1][6]%6==4 and CubeClick[4][8]%6==0) or 
	   (CubeClick[2][0]%6==3 and CubeClick[1][6]%6==5 and CubeClick[4][8]%6==2) or 
	   (CubeClick[2][0]%6==3 and CubeClick[1][6]%6==2 and CubeClick[4][8]%6==4) or 
	   (CubeClick[2][0]%6==4 and CubeClick[1][6]%6==0 and CubeClick[4][8]%6==3) or 
	   (CubeClick[2][0]%6==4 and CubeClick[1][6]%6==3 and CubeClick[4][8]%6==2) or 
	   (CubeClick[2][0]%6==4 and CubeClick[1][6]%6==2 and CubeClick[4][8]%6==1) or 
	   (CubeClick[2][0]%6==4 and CubeClick[1][6]%6==1 and CubeClick[4][8]%6==0) or 
	   (CubeClick[2][0]%6==5 and CubeClick[1][6]%6==1 and CubeClick[4][8]%6==2) or 
	   (CubeClick[2][0]%6==5 and CubeClick[1][6]%6==3 and CubeClick[4][8]%6==0) or 
	   (CubeClick[2][0]%6==5 and CubeClick[1][6]%6==0 and CubeClick[4][8]%6==1) or 
	   (CubeClick[2][0]%6==5 and CubeClick[1][6]%6==2 and CubeClick[4][8]%6==3)):
		Corner += 1

	if ((CubeClick[2][2]%6==0 and CubeClick[5][6]%6==3 and CubeClick[1][8]%6==4) or 
	   (CubeClick[2][2]%6==0 and CubeClick[5][6]%6==1 and CubeClick[1][8]%6==5) or 
	   (CubeClick[2][2]%6==0 and CubeClick[5][6]%6==4 and CubeClick[1][8]%6==1) or 
	   (CubeClick[2][2]%6==0 and CubeClick[5][6]%6==5 and CubeClick[1][8]%6==3) or 
	   (CubeClick[2][2]%6==1 and CubeClick[5][6]%6==0 and CubeClick[1][8]%6==4) or 
	   (CubeClick[2][2]%6==1 and CubeClick[5][6]%6==5 and CubeClick[1][8]%6==0) or 
	   (CubeClick[2][2]%6==1 and CubeClick[5][6]%6==4 and CubeClick[1][8]%6==2) or 
	   (CubeClick[2][2]%6==1 and CubeClick[5][6]%6==2 and CubeClick[1][8]%6==5) or 
	   (CubeClick[2][2]%6==2 and CubeClick[5][6]%6==1 and CubeClick[1][8]%6==4) or 
	   (CubeClick[2][2]%6==2 and CubeClick[5][6]%6==3 and CubeClick[1][8]%6==5) or 
	   (CubeClick[2][2]%6==2 and CubeClick[5][6]%6==4 and CubeClick[1][8]%6==3) or 
	   (CubeClick[2][2]%6==2 and CubeClick[5][6]%6==5 and CubeClick[1][8]%6==1) or 
	   (CubeClick[2][2]%6==3 and CubeClick[5][6]%6==0 and CubeClick[1][8]%6==5) or 
	   (CubeClick[2][2]%6==3 and CubeClick[5][6]%6==4 and CubeClick[1][8]%6==0) or 
	   (CubeClick[2][2]%6==3 and CubeClick[5][6]%6==5 and CubeClick[1][8]%6==2) or 
	   (CubeClick[2][2]%6==3 and CubeClick[5][6]%6==2 and CubeClick[1][8]%6==4) or 
	   (CubeClick[2][2]%6==4 and CubeClick[5][6]%6==0 and CubeClick[1][8]%6==3) or 
	   (CubeClick[2][2]%6==4 and CubeClick[5][6]%6==3 and CubeClick[1][8]%6==2) or 
	   (CubeClick[2][2]%6==4 and CubeClick[5][6]%6==2 and CubeClick[1][8]%6==1) or 
	   (CubeClick[2][2]%6==4 and CubeClick[5][6]%6==1 and CubeClick[1][8]%6==0) or 
	   (CubeClick[2][2]%6==5 and CubeClick[5][6]%6==1 and CubeClick[1][8]%6==2) or 
	   (CubeClick[2][2]%6==5 and CubeClick[5][6]%6==3 and CubeClick[1][8]%6==0) or 
	   (CubeClick[2][2]%6==5 and CubeClick[5][6]%6==0 and CubeClick[1][8]%6==1) or 
	   (CubeClick[2][2]%6==5 and CubeClick[5][6]%6==2 and CubeClick[1][8]%6==3)):
		Corner += 1

	if ((CubeClick[2][6]%6==0 and CubeClick[4][6]%6==3 and CubeClick[3][0]%6==4) or 
	   (CubeClick[2][6]%6==0 and CubeClick[4][6]%6==1 and CubeClick[3][0]%6==5) or 
	   (CubeClick[2][6]%6==0 and CubeClick[4][6]%6==4 and CubeClick[3][0]%6==1) or 
	   (CubeClick[2][6]%6==0 and CubeClick[4][6]%6==5 and CubeClick[3][0]%6==3) or 
	   (CubeClick[2][6]%6==1 and CubeClick[4][6]%6==0 and CubeClick[3][0]%6==4) or 
	   (CubeClick[2][6]%6==1 and CubeClick[4][6]%6==5 and CubeClick[3][0]%6==0) or 
	   (CubeClick[2][6]%6==1 and CubeClick[4][6]%6==4 and CubeClick[3][0]%6==2) or 
	   (CubeClick[2][6]%6==1 and CubeClick[4][6]%6==2 and CubeClick[3][0]%6==5) or 
	   (CubeClick[2][6]%6==2 and CubeClick[4][6]%6==1 and CubeClick[3][0]%6==4) or 
	   (CubeClick[2][6]%6==2 and CubeClick[4][6]%6==3 and CubeClick[3][0]%6==5) or 
	   (CubeClick[2][6]%6==2 and CubeClick[4][6]%6==4 and CubeClick[3][0]%6==3) or 
	   (CubeClick[2][6]%6==2 and CubeClick[4][6]%6==5 and CubeClick[3][0]%6==1) or 
	   (CubeClick[2][6]%6==3 and CubeClick[4][6]%6==0 and CubeClick[3][0]%6==5) or 
	   (CubeClick[2][6]%6==3 and CubeClick[4][6]%6==4 and CubeClick[3][0]%6==0) or 
	   (CubeClick[2][6]%6==3 and CubeClick[4][6]%6==5 and CubeClick[3][0]%6==2) or 
	   (CubeClick[2][6]%6==3 and CubeClick[4][6]%6==2 and CubeClick[3][0]%6==4) or 
	   (CubeClick[2][6]%6==4 and CubeClick[4][6]%6==0 and CubeClick[3][0]%6==3) or 
	   (CubeClick[2][6]%6==4 and CubeClick[4][6]%6==3 and CubeClick[3][0]%6==2) or 
	   (CubeClick[2][6]%6==4 and CubeClick[4][6]%6==2 and CubeClick[3][0]%6==1) or 
	   (CubeClick[2][6]%6==4 and CubeClick[4][6]%6==1 and CubeClick[3][0]%6==0) or 
	   (CubeClick[2][6]%6==5 and CubeClick[4][6]%6==1 and CubeClick[3][0]%6==2) or 
	   (CubeClick[2][6]%6==5 and CubeClick[4][6]%6==3 and CubeClick[3][0]%6==0) or 
	   (CubeClick[2][6]%6==5 and CubeClick[4][6]%6==0 and CubeClick[3][0]%6==1) or 
	   (CubeClick[2][6]%6==5 and CubeClick[4][6]%6==2 and CubeClick[3][0]%6==3)):
		Corner += 1
	if ((CubeClick[2][8]%6==0 and CubeClick[3][2]%6==3 and CubeClick[5][8]%6==4) or 
	   (CubeClick[2][8]%6==0 and CubeClick[3][2]%6==1 and CubeClick[5][8]%6==5) or 
	   (CubeClick[2][8]%6==0 and CubeClick[3][2]%6==4 and CubeClick[5][8]%6==1) or 
	   (CubeClick[2][8]%6==0 and CubeClick[3][2]%6==5 and CubeClick[5][8]%6==3) or 
	   (CubeClick[2][8]%6==1 and CubeClick[3][2]%6==0 and CubeClick[5][8]%6==4) or 
	   (CubeClick[2][8]%6==1 and CubeClick[3][2]%6==5 and CubeClick[5][8]%6==0) or 
	   (CubeClick[2][8]%6==1 and CubeClick[3][2]%6==4 and CubeClick[5][8]%6==2) or 
	   (CubeClick[2][8]%6==1 and CubeClick[3][2]%6==2 and CubeClick[5][8]%6==5) or 
	   (CubeClick[2][8]%6==2 and CubeClick[3][2]%6==1 and CubeClick[5][8]%6==4) or 
	   (CubeClick[2][8]%6==2 and CubeClick[3][2]%6==3 and CubeClick[5][8]%6==5) or 
	   (CubeClick[2][8]%6==2 and CubeClick[3][2]%6==4 and CubeClick[5][8]%6==3) or 
	   (CubeClick[2][8]%6==2 and CubeClick[3][2]%6==5 and CubeClick[5][8]%6==1) or 
	   (CubeClick[2][8]%6==3 and CubeClick[3][2]%6==0 and CubeClick[5][8]%6==5) or 
	   (CubeClick[2][8]%6==3 and CubeClick[3][2]%6==4 and CubeClick[5][8]%6==0) or 
	   (CubeClick[2][8]%6==3 and CubeClick[3][2]%6==5 and CubeClick[5][8]%6==2) or 
	   (CubeClick[2][8]%6==3 and CubeClick[3][2]%6==2 and CubeClick[5][8]%6==4) or 
	   (CubeClick[2][8]%6==4 and CubeClick[3][2]%6==0 and CubeClick[5][8]%6==3) or 
	   (CubeClick[2][8]%6==4 and CubeClick[3][2]%6==3 and CubeClick[5][8]%6==2) or 
	   (CubeClick[2][8]%6==4 and CubeClick[3][2]%6==2 and CubeClick[5][8]%6==1) or 
	   (CubeClick[2][8]%6==4 and CubeClick[3][2]%6==1 and CubeClick[5][8]%6==0) or 
	   (CubeClick[2][8]%6==5 and CubeClick[3][2]%6==1 and CubeClick[5][8]%6==2) or 
	   (CubeClick[2][8]%6==5 and CubeClick[3][2]%6==3 and CubeClick[5][8]%6==0) or 
	   (CubeClick[2][8]%6==5 and CubeClick[3][2]%6==0 and CubeClick[5][8]%6==1) or 
	   (CubeClick[2][8]%6==5 and CubeClick[3][2]%6==2 and CubeClick[5][8]%6==3)):
		Corner += 1
	print(edge)
	print(Corner)
	if edge != 12 or Corner != 8:
		InGame = False
		NotValid = True
	
def Front(CubeClicki):
	Cube = copy.deepcopy(CubeClicki)
	# Front face (face 0)
	Cube[0][0] = CubeClicki[0][2]
	Cube[0][1] = CubeClicki[0][5]
	Cube[0][2] = CubeClicki[0][8]
	Cube[0][3] = CubeClicki[0][1]
	Cube[0][4] = CubeClicki[0][4]
	Cube[0][5] = CubeClicki[0][7]
	Cube[0][6] = CubeClicki[0][0]
	Cube[0][7] = CubeClicki[0][3]
	Cube[0][8] = CubeClicki[0][6]
	# Right face (face 1)
	Cube[1][0] = CubeClicki[4][0]
	Cube[1][1] = CubeClicki[4][1]
	Cube[1][2] = CubeClicki[4][2]
	# Left face (face 3)
	Cube[3][6] = CubeClicki[5][2]
	Cube[3][7] = CubeClicki[5][1]
	Cube[3][8] = CubeClicki[5][0]
	# Top face (face 4)
	Cube[4][0] = CubeClicki[3][8]
	Cube[4][1] = CubeClicki[3][7]
	Cube[4][2] = CubeClicki[3][6]
	# Bottom face (face 5)
	Cube[5][2] = CubeClicki[1][2]
	Cube[5][1] = CubeClicki[1][1]
	Cube[5][0] = CubeClicki[1][0]

	return Cube

def FrontI(CubeClicki):
	Cube = copy.deepcopy(CubeClicki)
	# Front face (face 0)
	Cube[0][0] = CubeClicki[0][6]
	Cube[0][1] = CubeClicki[0][3]
	Cube[0][2] = CubeClicki[0][0]
	Cube[0][3] = CubeClicki[0][7]
	Cube[0][4] = CubeClicki[0][4]
	Cube[0][5] = CubeClicki[0][1]
	Cube[0][6] = CubeClicki[0][8]
	Cube[0][7] = CubeClicki[0][5]
	Cube[0][8] = CubeClicki[0][2]
	# Right face (face 1)
	Cube[1][0] = CubeClicki[5][0]
	Cube[1][1] = CubeClicki[5][1]
	Cube[1][2] = CubeClicki[5][2]
	# Left face (face 3)
	Cube[3][6] = CubeClicki[4][2]
	Cube[3][7] = CubeClicki[4][1]
	Cube[3][8] = CubeClicki[4][0]
	# Top face (face 4)
	Cube[4][0] = CubeClicki[1][0]
	Cube[4][1] = CubeClicki[1][1]
	Cube[4][2] = CubeClicki[1][2]
	# Bottom face (face 5)
	Cube[5][2] = CubeClicki[3][6]
	Cube[5][1] = CubeClicki[3][7]
	Cube[5][0] = CubeClicki[3][8]

	return Cube

def Left(CubeClicki):
	Cube = copy.deepcopy(CubeClicki)
	# Front face (face 0)
	Cube[3][0] = CubeClicki[3][2]
	Cube[3][1] = CubeClicki[3][5]
	Cube[3][2] = CubeClicki[3][8]
	Cube[3][3] = CubeClicki[3][1]
	Cube[3][4] = CubeClicki[3][4]
	Cube[3][5] = CubeClicki[3][7]
	Cube[3][6] = CubeClicki[3][0]
	Cube[3][7] = CubeClicki[3][3]
	Cube[3][8] = CubeClicki[3][6]
	# Right face (face 1)
	Cube[0][0] = CubeClicki[4][6]
	Cube[0][1] = CubeClicki[4][3]
	Cube[0][2] = CubeClicki[4][0]
	# Left face (face 3)
	Cube[4][0] = CubeClicki[2][6]
	Cube[4][3] = CubeClicki[2][7]
	Cube[4][6] = CubeClicki[2][8]
	# Top face (face 4)
	Cube[2][6] = CubeClicki[5][8]
	Cube[2][7] = CubeClicki[5][5]
	Cube[2][8] = CubeClicki[5][2]
	# Bottom face (face 5)
	Cube[5][2] = CubeClicki[0][0]
	Cube[5][5] = CubeClicki[0][1]
	Cube[5][8] = CubeClicki[0][2]

	return Cube

def LeftI(CubeClicki):
	Cube = copy.deepcopy(CubeClicki)
	# Front face (face 0)
	Cube[3][0] = CubeClicki[3][6]
	Cube[3][1] = CubeClicki[3][3]
	Cube[3][2] = CubeClicki[3][0]
	Cube[3][3] = CubeClicki[3][7]
	Cube[3][4] = CubeClicki[3][4]
	Cube[3][5] = CubeClicki[3][1]
	Cube[3][6] = CubeClicki[3][8]
	Cube[3][7] = CubeClicki[3][5]
	Cube[3][8] = CubeClicki[3][2]
	# Right face (face 1)
	Cube[0][0] = CubeClicki[5][2]
	Cube[0][1] = CubeClicki[5][5]
	Cube[0][2] = CubeClicki[5][8]
	# Left face (face 3)
	Cube[4][0] = CubeClicki[0][2]
	Cube[4][3] = CubeClicki[0][1]
	Cube[4][6] = CubeClicki[0][0]
	# Top face (face 4)
	Cube[2][6] = CubeClicki[4][0]
	Cube[2][7] = CubeClicki[4][3]
	Cube[2][8] = CubeClicki[4][6]
	# Bottom face (face 5)
	Cube[5][2] = CubeClicki[2][8]
	Cube[5][5] = CubeClicki[2][7]
	Cube[5][8] = CubeClicki[2][6]

	return Cube

def Right(CubeClicki):
	Cube = copy.deepcopy(CubeClicki)
	# Front face (face 0)
	Cube[1][0] = CubeClicki[1][2]
	Cube[1][1] = CubeClicki[1][5]
	Cube[1][2] = CubeClicki[1][8]
	Cube[1][3] = CubeClicki[1][1]
	Cube[1][4] = CubeClicki[1][4]
	Cube[1][5] = CubeClicki[1][7]
	Cube[1][6] = CubeClicki[1][0]
	Cube[1][7] = CubeClicki[1][3]
	Cube[1][8] = CubeClicki[1][6]
	# Right face (face 1)
	Cube[0][6] = CubeClicki[5][0]
	Cube[0][7] = CubeClicki[5][3]
	Cube[0][8] = CubeClicki[5][6]
	# Left face (face 3)
	Cube[4][2] = CubeClicki[0][8]
	Cube[4][5] = CubeClicki[0][7]
	Cube[4][8] = CubeClicki[0][6]
	# Top face (face 4)
	Cube[2][0] = CubeClicki[4][2]
	Cube[2][1] = CubeClicki[4][5]
	Cube[2][2] = CubeClicki[4][8]
	# Bottom face (face 5)
	Cube[5][0] = CubeClicki[2][2]
	Cube[5][3] = CubeClicki[2][1]
	Cube[5][6] = CubeClicki[2][0]

	return Cube

def RightI(CubeClicki):
	Cube = copy.deepcopy(CubeClicki)
	# Front face (face 0)
	Cube[1][0] = CubeClicki[1][6]
	Cube[1][1] = CubeClicki[1][3]
	Cube[1][2] = CubeClicki[1][0]
	Cube[1][3] = CubeClicki[1][7]
	Cube[1][4] = CubeClicki[1][4]
	Cube[1][5] = CubeClicki[1][1]
	Cube[1][6] = CubeClicki[1][8]
	Cube[1][7] = CubeClicki[1][5]
	Cube[1][8] = CubeClicki[1][2]
	# Right face (face 1)
	Cube[0][6] = CubeClicki[4][8]
	Cube[0][7] = CubeClicki[4][5]
	Cube[0][8] = CubeClicki[4][2]
	# Left face (face 3)
	Cube[4][2] = CubeClicki[2][0]
	Cube[4][5] = CubeClicki[2][1]
	Cube[4][8] = CubeClicki[2][2]
	# Top face (face 4)
	Cube[2][0] = CubeClicki[5][6]
	Cube[2][1] = CubeClicki[5][3]
	Cube[2][2] = CubeClicki[5][0]
	# Bottom face (face 5)
	Cube[5][0] = CubeClicki[0][6]
	Cube[5][3] = CubeClicki[0][7]
	Cube[5][6] = CubeClicki[0][8]

	return Cube

def Up(CubeClicki):
	Cube = copy.deepcopy(CubeClicki)
	# Front face (face 0)
	Cube[4][0] = CubeClicki[4][2]
	Cube[4][1] = CubeClicki[4][5]
	Cube[4][2] = CubeClicki[4][8]
	Cube[4][3] = CubeClicki[4][1]
	Cube[4][4] = CubeClicki[4][4]
	Cube[4][5] = CubeClicki[4][7]
	Cube[4][6] = CubeClicki[4][0]
	Cube[4][7] = CubeClicki[4][3]
	Cube[4][8] = CubeClicki[4][6]
	# Right face (face 1)
	Cube[0][0] = CubeClicki[1][0]
	Cube[0][3] = CubeClicki[1][3]
	Cube[0][6] = CubeClicki[1][6]
	# Left face (face 3)
	Cube[3][0] = CubeClicki[0][0]
	Cube[3][3] = CubeClicki[0][3]
	Cube[3][6] = CubeClicki[0][6]
	# Top face (face 4)
	Cube[2][0] = CubeClicki[3][0]
	Cube[2][3] = CubeClicki[3][3]
	Cube[2][6] = CubeClicki[3][6]
	# Bottom face (face 5)
	Cube[1][0] = CubeClicki[2][0]
	Cube[1][3] = CubeClicki[2][3]
	Cube[1][6] = CubeClicki[2][6]

	return Cube  

def UpI(CubeClicki):
	Cube = copy.deepcopy(CubeClicki)
	# Front face (face 0)
	Cube[4][0] = CubeClicki[4][6]
	Cube[4][1] = CubeClicki[4][3]
	Cube[4][2] = CubeClicki[4][0]
	Cube[4][3] = CubeClicki[4][7]
	Cube[4][4] = CubeClicki[4][4]
	Cube[4][5] = CubeClicki[4][1]
	Cube[4][6] = CubeClicki[4][8]
	Cube[4][7] = CubeClicki[4][5]
	Cube[4][8] = CubeClicki[4][2]
	# Right face (face 1)
	Cube[0][0] = CubeClicki[3][0]
	Cube[0][3] = CubeClicki[3][3]
	Cube[0][6] = CubeClicki[3][6]
	# Left face (face 3)
	Cube[3][0] = CubeClicki[2][0]
	Cube[3][3] = CubeClicki[2][3]
	Cube[3][6] = CubeClicki[2][6]
	# Top face (face 4)
	Cube[2][0] = CubeClicki[1][0]
	Cube[2][3] = CubeClicki[1][3]
	Cube[2][6] = CubeClicki[1][6]
	# Bottom face (face 5)
	Cube[1][0] = CubeClicki[0][0]
	Cube[1][3] = CubeClicki[0][3]
	Cube[1][6] = CubeClicki[0][6]

	return Cube  

def Down(CubeClicki):
	Cube = copy.deepcopy(CubeClicki)
	# Front face (face 0)
	Cube[5][0] = CubeClicki[5][2]
	Cube[5][1] = CubeClicki[5][5]
	Cube[5][2] = CubeClicki[5][8]
	Cube[5][3] = CubeClicki[5][1]
	Cube[5][4] = CubeClicki[5][4]
	Cube[5][5] = CubeClicki[5][7]
	Cube[5][6] = CubeClicki[5][0]
	Cube[5][7] = CubeClicki[5][3]
	Cube[5][8] = CubeClicki[5][6]
	# Right face (face 1)
	Cube[0][2] = CubeClicki[3][2]
	Cube[0][5] = CubeClicki[3][5]
	Cube[0][8] = CubeClicki[3][8]
	# Left face (face 3)
	Cube[3][2] = CubeClicki[2][2]
	Cube[3][5] = CubeClicki[2][5]
	Cube[3][8] = CubeClicki[2][8]
	# Top face (face 4)
	Cube[2][2] = CubeClicki[1][2]
	Cube[2][5] = CubeClicki[1][5]
	Cube[2][8] = CubeClicki[1][8]
	# Bottom face (face 5)
	Cube[1][2] = CubeClicki[0][2]
	Cube[1][5] = CubeClicki[0][5]
	Cube[1][8] = CubeClicki[0][8]

	return Cube 

def DownI(CubeClicki):
	Cube = copy.deepcopy(CubeClicki)
	# Front face (face 0)
	Cube[5][0] = CubeClicki[5][6]
	Cube[5][1] = CubeClicki[5][3]
	Cube[5][2] = CubeClicki[5][0]
	Cube[5][3] = CubeClicki[5][7]
	Cube[5][4] = CubeClicki[5][4]
	Cube[5][5] = CubeClicki[5][1]
	Cube[5][6] = CubeClicki[5][8]
	Cube[5][7] = CubeClicki[5][5]
	Cube[5][8] = CubeClicki[5][2]
	# Right face (face 1)
	Cube[0][2] = CubeClicki[1][2]
	Cube[0][5] = CubeClicki[1][5]
	Cube[0][8] = CubeClicki[1][8]
	# Left face (face 3)
	Cube[3][2] = CubeClicki[0][2]
	Cube[3][5] = CubeClicki[0][5]
	Cube[3][8] = CubeClicki[0][8]
	# Top face (face 4)
	Cube[2][2] = CubeClicki[3][2]
	Cube[2][5] = CubeClicki[3][5]
	Cube[2][8] = CubeClicki[3][8]
	# Bottom face (face 5)
	Cube[1][2] = CubeClicki[2][2]
	Cube[1][5] = CubeClicki[2][5]
	Cube[1][8] = CubeClicki[2][8]

	return Cube 

def Scrambel():
	global CubeClick
	randnum = [randint(0,9) for i in range(20)]
	for i in range(len(randnum)):
		if randnum[i] == 0:
			CubeClick = Left(CubeClick)
		elif randnum[i] == 1:
			CubeClick = LeftI(CubeClick)
		elif randnum[i] == 2:
			CubeClick = Right(CubeClick)
		elif randnum[i] == 3:
			CubeClick = RightI(CubeClick)
		elif randnum[i] == 4:
			CubeClick = Up(CubeClick)
		elif randnum[i] == 5:
			CubeClick = UpI(CubeClick)
		elif randnum[i] == 6:
			CubeClick = Down(CubeClick)
		elif randnum[i] == 7:
			CubeClick = DownI(CubeClick)
		elif randnum[i] == 8:
			CubeClick = Front(CubeClick)
		elif randnum[i] == 9:
			CubeClick = FrontI(CubeClick)

def FindWhite():
	facelst = [0,1,2,4,5]
	piecelst = [1,3,5,7]
	found = False

	while found == False:
		for i in facelst:
			for j in piecelst:
				if CubeClick[i][j]%6 == 1:
					retlist = [i,j]
					found = True
	return retlist
	
def WhiteToYellow(loc):
	global CubeClick
	i = loc[0] #Face That the white piece is on
	j = loc[1] #Location number on the face 

	if loc[0] == 0:
		if loc[1] == 1:
			move = [[i, j], ['Front', 'Up'], [7, 3]]
			return move
		elif loc[1] == 3: 
			move = [[i, j], ['Up'], [3]]
			return move
		elif loc[1] == 5:
			move = [[i, j], ['DownI'], [5]]
			return move
		elif loc[1] == 7:
			move = [[i, j], ['FrontI', 'Up'], [7, 3]]
			return move 

	elif loc[0] == 4:
		if loc[1] == 1:
			move = [[i, j], ['FrontI'], [7]]
			return move
		elif loc[1] == 3:
			move = [[i, j], ['UpI', 'FrontI'], [3, 7]] 
			return move
		elif loc[1] == 5:
			move = [[i, j], ['Up', 'FrontI'], [3, 7]]
			return move
		elif loc[1] == 7:  
			move = [[i, j], ['Up', 'Up', 'FrontI'], [3, 3, 7]]
			return move 

	elif loc[0] == 2:
		if loc[1] == 1:
			move = [[i, j], ['RightI', 'Up', 'FrontI'], ['', 3, 7]]
			return move
		elif loc[1] == 3: 
			move = [[i, j], ['UpI'], [3]]
			return move
		elif loc[1] == 5:
			move = [[i, j], ['Down'], [5]]
			return move
		elif loc[1] == 7:  
			move = [[i, j], ['Left', 'UpI', 'FrontI'], ['', 3, 7]]
			return move

	elif loc[0] == 5:
		if loc[1] == 1:
			move = [[i, j], ['Front'], [7]]
			return move
		elif loc[1] == 3: 
			move = [[i, j], ['DownI', 'Front'], [5, 7]]
			return move
		elif loc[1] == 5:
			move = [[i, j], ['Down', 'Front'], [5, 7]]
			return move
		elif loc[1] == 7: 
			move = [[i, j], ['Down', 'Down', 'Front'], [5, 5, 7]] 
			return move

	elif loc[0] == 1:
		if loc[1] == 1:
			move = [[i, j], ['Front', 'Front'], [7, 7]]
			return move
		elif loc[1] == 3: 
			move = [[i, j], ['Up', 'Up'], [3, 3]]
			return move
		elif loc[1] == 5:
			move = [[i, j], ['DownI', 'DownI'], [5, 5]]
			return move
		elif loc[1] == 7:  
			move = [[i, j], ['Right', 'DownI', 'DownI'], ['', 5, 5]]
			return move

def CheckTop():
	global CubeClick

	edge = [1,3,5,7]
	done = []
	for i in edge:
		if CubeClick[3][i]%6 == 1:
			done.append(i)
	if len(done) == 4:
		done = True
	return done

def MoveUpdate(move, top):
	# move = [[i, j], ['Right', 'DownI', 'DownI'], ['', 5, 5]]
	# top = [ List of white pieces on the top]
	global CubeClick
	TheTop = copy.deepcopy(top)
	FinMove = copy.deepcopy(move[1])
	print(move[0][0])

	if move[0][0] == 0:
		for i in range(len(move[1])):
			good = False
			while not good:
				if move[2][i] in TheTop:
					CubeClick = Left(CubeClick)
					TheTop = CheckTop()
				else:
					if move[1][i] == 'Front':
						CubeClick = Front(CubeClick)
					elif move[1][i] == 'FrontI':
						CubeClick = FrontI(CubeClick)
					elif move[1][i] == 'DownI':
						CubeClick = DownI(CubeClick)
					elif move[1][i] == 'Up':
						CubeClick = Up(CubeClick)
					print('here')
					good = True

	elif move[0][0] == 4 :
		for i in range(len(move[1])):
			good = False
			while not good:
				if move[2][i] in TheTop:
					CubeClick = Left(CubeClick)
					TheTop = CheckTop()
				else:
					if move[1][i] == 'FrontI':
						CubeClick = FrontI(CubeClick)
					elif move[1][i] == 'Up':
						CubeClick = Up(CubeClick)
					elif move[1][i] == 'UpI':
						CubeClick = UpI(CubeClick)
					good = True

	elif move[0][0] == 2 :
		for i in range(len(move[1])):
			good = False
			while not good:
				if move[2][i] in TheTop:
					CubeClick = Left(CubeClick)
					TheTop = CheckTop()
				else:
					if move[1][i] == 'FrontI':
						CubeClick = FrontI(CubeClick)
					elif move[1][i] == 'Up':
						CubeClick = Up(CubeClick)
					elif move[1][i] == 'UpI':
						CubeClick = UpI(CubeClick)
					elif move[1][i] == 'RightI':
						CubeClick = RightI(CubeClick)
					elif move[1][i] == 'Down':
						CubeClick = Down(CubeClick) 
					elif move[1][i] == 'Left':
						CubeClick = Left(CubeClick)   
					good = True

	elif move[0][0] == 5 :
		for i in range(len(move[1])):
			good = False
			while not good:
				if move[2][i] in TheTop:
					CubeClick = Left(CubeClick)
					TheTop = CheckTop()
				else:
					if move[1][i] == 'Front':
						CubeClick = Front(CubeClick)
					elif move[1][i] == 'Down':
						CubeClick = Down(CubeClick) 
					elif move[1][i] == 'DownI':
						CubeClick = DownI(CubeClick) 
					good = True

	elif move[0][0] == 1 :
		for i in range(len(move[1])):
			good = False
			while not good:
				if move[2][i] in TheTop:
					CubeClick = Left(CubeClick)
					TheTop = CheckTop()
				else:
					if move[1][i] == 'Front':
						CubeClick = Front(CubeClick)
					elif move[1][i] == 'Up':
						CubeClick = Up(CubeClick) 
					elif move[1][i] == 'DownI':
						CubeClick = DownI(CubeClick) 
					elif move[1][i] == 'Right':
						CubeClick = Right(CubeClick)
					good = True

# Step 1
def TopDaisy():
	Done = False
	while not Done:
		TopLst = CheckTop()
		if TopLst == True:
			Done = True 
		else:
			location = FindWhite()
			MoveSet = WhiteToYellow(location)
			MoveUpdate(MoveSet, TopLst)
			print(CubeClick)
	

def GameMenu():
	global InGame, InMenu, GameMenuCount, StickerLst, CubeClick

	DrawSky()
	pygame.mixer.Channel(0).set_volume(0)
	pygame.mixer.music.set_volume(0.5)

	# Draw Solve Button
	screen.blit(SolveBut, (width-SolveButtonWidth - 20, height - SolveButtonHeight - 80 + TitleBarHeight))

	# draw Scramble
	screen.blit(ScrambleBut, (width-SolveButtonWidth - 20, height - 2*SolveButtonHeight - 100 + TitleBarHeight))

	# Draw Title Bar 
	for x in range(0, width, TitleBarWidth):
		screen.blit(TitleBar, (x,0))

	# Draw Home Button 
	screen.blit(HomeBut, (width-HomeButWidth-20, 10))

	# Draw Sound Button 
	screen.blit(SoundOn, (width-SoundOnWidth-HomeButWidth-40, 10))

	# Draw cube Fold
	cubeDisX = width//2 - CubeFoldWidth//2 
	cubeDisY = height//2 - CubeFoldHeight//2 + TitleBarHeight 
	screen.blit(CubeFold, (cubeDisX, cubeDisY))

	# Draw Moves
	startBut = 280
	screen.blit(LeftBut, (startBut, 100))
	screen.blit(LeftIBut, (startBut+100+40, 100))
	screen.blit(RightBut, (startBut+200+80, 100))
	screen.blit(RightIBut, (startBut+300+120, 100))
	screen.blit(UpBut, (startBut+400+160, 100))
	screen.blit(UpIBut, (startBut+500+200, 100))
	screen.blit(DownBut, (startBut+600+240, 100))
	screen.blit(DownIBut, (startBut+700+280, 100))
	screen.blit(FrontBut, (startBut+800+320, 100))
	screen.blit(FrontIBut, (startBut+900+360, 100))

	# Draw selection cube
	x, y = pygame.mouse.get_pos() 
	if x > cubeDisX+10 and x < cubeDisX+225 and y > cubeDisY+245 and y < cubeDisY+460:
		screen.blit(CubeBL, (20, height-260))
	elif x > cubeDisX+245 and x<cubeDisX+460 and y > cubeDisY+245 and y < cubeDisY+460:
		screen.blit(CubeTop, (20, height-260))
	elif x > cubeDisX+480 and x < cubeDisX+695 and y > cubeDisY+245 and y < cubeDisY+460:
		screen.blit(CubeFR, (20, height-260))
	elif x > cubeDisX+715 and x < cubeDisX+930 and y > cubeDisY+245 and y < cubeDisY+460:
		screen.blit(CubeBot, (20, height-260))
	elif x > cubeDisX+245 and x<cubeDisX+460 and y > cubeDisY+10 and y < cubeDisY+225:
		screen.blit(CubeBR, (20, height-260))
	elif x > cubeDisX+245 and x<cubeDisX+460 and y > cubeDisY+480 and y < cubeDisY+695:
		screen.blit(CubeFL, (20, height-260))
	else:
		screen.blit(CubeEmpty, (20, height-260))

	# Exit To Menu, Defining stickers
	for ev in pygame.event.get(): 
		if ev.type == pygame.MOUSEBUTTONDOWN:
			x, y = ev.pos
			# Exit To Menu 
			if HomeBut.get_rect(topleft=(width-HomeButWidth-20, 10)).collidepoint(x, y):
				InMenu = True
				InGame = False 
				CubeClick = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
							 [1, 1, 1, 1, 1, 1, 1, 1, 1],
							 [2, 2, 2, 2, 2, 2, 2, 2, 2],
							 [3, 3, 3, 3, 3, 3, 3, 3, 3],
							 [4, 4, 4, 4, 4, 4, 4, 4, 4],
							 [5, 5, 5, 5, 5, 5, 5, 5, 5]]
			# Turn Sound Off 
			elif SoundOn.get_rect(topleft=(width-SoundOnWidth-HomeButWidth-40, 10)).collidepoint(x, y):
				GameMenuCount = GameMenuCount + 1

			# Check if Scrambel is possible 
			elif SolveBut.get_rect(topleft=(width-SolveButtonWidth - 20, height - SolveButtonHeight - 80 + TitleBarHeight)).collidepoint(x, y):
				CubeCheck()
				TopDaisy()

			# Scrambel
			elif ScrambleBut.get_rect(topleft=(width-SolveButtonWidth - 20, height - 2*SolveButtonHeight - 100 + TitleBarHeight)).collidepoint(x, y):
				Scrambel()

			# Moves
			elif LeftBut.get_rect(topleft=(startBut, 100)).collidepoint(x,y):
				CubeClick = Left(CubeClick)
			elif LeftBut.get_rect(topleft=(startBut+140, 100)).collidepoint(x,y):
				CubeClick = LeftI(CubeClick) 
			elif LeftBut.get_rect(topleft=(startBut+280, 100)).collidepoint(x,y):
				CubeClick = Right(CubeClick)
			elif LeftBut.get_rect(topleft=(startBut+420, 100)).collidepoint(x,y):
				CubeClick = RightI(CubeClick)
			elif LeftBut.get_rect(topleft=(startBut+560, 100)).collidepoint(x,y):
				CubeClick = Up(CubeClick)
			elif LeftBut.get_rect(topleft=(startBut+700, 100)).collidepoint(x,y):
				CubeClick = UpI(CubeClick)
			elif LeftBut.get_rect(topleft=(startBut+840, 100)).collidepoint(x,y):
				CubeClick = Down(CubeClick)
			elif LeftBut.get_rect(topleft=(startBut+980, 100)).collidepoint(x,y):
				CubeClick = DownI(CubeClick)
			elif LeftBut.get_rect(topleft=(startBut+1120, 100)).collidepoint(x,y):
				CubeClick = Front(CubeClick)
			elif LeftBut.get_rect(topleft=(startBut+1260, 100)).collidepoint(x,y):
				CubeClick = FrontI(CubeClick)

			# Green 
			elif x > cubeDisX + 10 and x < cubeDisX+75: 
				if y > cubeDisY+245 and y < cubeDisY+310:
					CubeClick[0][0] = CubeClick[0][0] + 1
				elif y > cubeDisY+320 and y < cubeDisY+385:
					CubeClick[0][1] = CubeClick[0][1] + 1
				elif y > cubeDisY+395 and y < cubeDisY+460:
					CubeClick[0][2] = CubeClick[0][2] + 1
			elif x > cubeDisX + 85 and x < cubeDisX+150:
				if y > cubeDisY+245 and y < cubeDisY+310:
					CubeClick[0][3] = CubeClick[0][3] + 1
				elif y > cubeDisY+395 and y < cubeDisY+460:
					CubeClick[0][5] = CubeClick[0][5] + 1   
			elif x > cubeDisX + 160 and x < cubeDisX+225:
				if y > cubeDisY+245 and y < cubeDisY+310:
					CubeClick[0][6] = CubeClick[0][6] + 1
				elif y > cubeDisY+320 and y < cubeDisY+385:
					CubeClick[0][7] = CubeClick[0][7] + 1
				elif y > cubeDisY+395 and y < cubeDisY+460:
					CubeClick[0][8] = CubeClick[0][8] + 1 

			# White, Orange, Red 
			elif x > cubeDisX+245 and x < cubeDisX+310:
				# White
				if y > cubeDisY+245 and y < cubeDisY+310:
					CubeClick[1][0] = CubeClick[1][0] + 1
				elif y > cubeDisY+320 and y < cubeDisY+385:
					CubeClick[1][1] = CubeClick[1][1] + 1
				elif y > cubeDisY+395 and y < cubeDisY+460:
					CubeClick[1][2] = CubeClick[1][2] + 1
				# Red
				elif y>cubeDisY+480 and y<cubeDisY+545:
					CubeClick[5][0] = CubeClick[5][0] + 1
				elif y>cubeDisY+555 and y<cubeDisY+620:
					CubeClick[5][1] = CubeClick[5][1] + 1
				elif y>cubeDisY+630 and y<cubeDisY+695:
					CubeClick[5][2] = CubeClick[5][2] + 1
				# Orange
				elif y>cubeDisY+10 and y<cubeDisY+75:
					CubeClick[4][0] = CubeClick[4][0] + 1
				elif y>cubeDisY+85 and y<cubeDisY+150:
					CubeClick[4][1] = CubeClick[4][1] + 1
				elif y>cubeDisY+160 and y<cubeDisY+225:
					CubeClick[4][2] = CubeClick[4][2] + 1

			# White, Orange, Red 
			elif x > cubeDisX+320 and x < cubeDisX+385:
				# White
				if y > cubeDisY+245 and y < cubeDisY+310:
					CubeClick[1][3] = CubeClick[1][3] + 1
				elif y > cubeDisY+395 and y < cubeDisY+460:
					CubeClick[1][5] = CubeClick[1][5] + 1  
				# Red
				elif y>cubeDisY+480 and y<cubeDisY+545:
					CubeClick[5][3] = CubeClick[5][3] + 1
				elif y>cubeDisY+630 and y<cubeDisY+695:
					CubeClick[5][5] = CubeClick[5][5] + 1
				# Orange
				elif y>cubeDisY+10 and y<cubeDisY+75:
					CubeClick[4][3] = CubeClick[4][3] + 1
				elif y>cubeDisY+160 and y<cubeDisY+225:
					CubeClick[4][5] = CubeClick[4][5] + 1
			# White, Orange, Red 
			elif x > cubeDisX+395 and x < cubeDisX+460:
				# White
				if y > cubeDisY+245 and y < cubeDisY+310:
					CubeClick[1][6] = CubeClick[1][6] + 1
				elif y > cubeDisY+320 and y < cubeDisY+385:
					CubeClick[1][7] = CubeClick[1][7] + 1
				elif y > cubeDisY+395 and y < cubeDisY+460:
					CubeClick[1][8] = CubeClick[1][8] + 1 
				# Red
				elif y>cubeDisY+480 and y<cubeDisY+545:
					CubeClick[5][6] = CubeClick[5][6] + 1
				elif y>cubeDisY+555 and y<cubeDisY+620:
					CubeClick[5][7] = CubeClick[5][7] + 1
				elif y>cubeDisY+630 and y<cubeDisY+695:
					CubeClick[5][8] = CubeClick[5][8] + 1 
				# Orange
				elif y>cubeDisY+10 and y<cubeDisY+75:
					CubeClick[4][6] = CubeClick[4][6] + 1
				elif y>cubeDisY+85 and y<cubeDisY+150:
					CubeClick[4][7] = CubeClick[4][7] + 1
				elif y>cubeDisY+160 and y<cubeDisY+225:
					CubeClick[4][8] = CubeClick[4][8] + 1       
			# Blue
			elif x > cubeDisX+480 and x < cubeDisX+545:
				if y > cubeDisY+245 and y < cubeDisY+310:
					CubeClick[2][0] = CubeClick[2][0] + 1
				elif y > cubeDisY+320 and y < cubeDisY+385:
					CubeClick[2][1] = CubeClick[2][1] + 1
				elif y > cubeDisY+395 and y < cubeDisY+460:
					CubeClick[2][2] = CubeClick[2][2] + 1   
			elif x > cubeDisX+555 and x < cubeDisX+620:
				if y > cubeDisY+245 and y < cubeDisY+310:
					CubeClick[2][3] = CubeClick[2][3] + 1
				elif y > cubeDisY+395 and y < cubeDisY+460:
					CubeClick[2][5] = CubeClick[2][5] + 1  
			elif x > cubeDisX+630 and x < cubeDisX+695:
				if y > cubeDisY+245 and y < cubeDisY+310:
					CubeClick[2][6] = CubeClick[2][6] + 1
				elif y > cubeDisY+320 and y < cubeDisY+385:
					CubeClick[2][7] = CubeClick[2][7] + 1
				elif y > cubeDisY+395 and y < cubeDisY+460:
					CubeClick[2][8] = CubeClick[2][8] + 1
			# Yellow
			elif x > cubeDisX+715 and x < cubeDisX+780:
				if y > cubeDisY+245 and y < cubeDisY+310:
					CubeClick[3][0] = CubeClick[3][0] + 1
				elif y > cubeDisY+320 and y < cubeDisY+385:
					CubeClick[3][1] = CubeClick[3][1] + 1
				elif y > cubeDisY+395 and y < cubeDisY+460:
					CubeClick[3][2] = CubeClick[3][2] + 1  
			elif x > cubeDisX+790 and x < cubeDisX+855:
				if y > cubeDisY+245 and y < cubeDisY+310:
					CubeClick[3][3] = CubeClick[3][3] + 1
				elif y > cubeDisY+395 and y < cubeDisY+460:
					CubeClick[3][5] = CubeClick[3][5] + 1 
			elif x > cubeDisX+865 and x < cubeDisX+930:
				if y > cubeDisY+245 and y < cubeDisY+310:
					CubeClick[3][6] = CubeClick[3][6] + 1
				elif y > cubeDisY+320 and y < cubeDisY+385:
					CubeClick[3][7] = CubeClick[3][7] + 1
				elif y > cubeDisY+395 and y < cubeDisY+460:
					CubeClick[3][8] = CubeClick[3][8] + 1

	# Draw Stickers 
	for i in range(len(CubeClick)):
		for j in range(len(CubeClick[i])):
			if i == 0:
				if j == 0:
					DrawStick(i,j,cubeDisX,cubeDisY,10,245)
				elif j == 1:
					DrawStick(i,j,cubeDisX,cubeDisY,10,320)
				elif j == 2:
					DrawStick(i,j,cubeDisX,cubeDisY,10,395)
				elif j == 3:
					DrawStick(i,j,cubeDisX,cubeDisY,85,245)
				elif j == 4:
					DrawStick(i,j,cubeDisX,cubeDisY,85,320)
				elif j == 5:
					DrawStick(i,j,cubeDisX,cubeDisY,85,395)
				elif j == 6:
					DrawStick(i,j,cubeDisX,cubeDisY,160,245)
				elif j == 7:
					DrawStick(i,j,cubeDisX,cubeDisY,160,320)
				elif j == 8:
					DrawStick(i,j,cubeDisX,cubeDisY,160,395) 
			elif i == 1:
				if j == 0:
					DrawStick(i,j,cubeDisX,cubeDisY,245,245)
				elif j == 1:
					DrawStick(i,j,cubeDisX,cubeDisY,245,320)
				elif j == 2:
					DrawStick(i,j,cubeDisX,cubeDisY,245,395)
				elif j == 3:
					DrawStick(i,j,cubeDisX,cubeDisY,320,245)
				elif j == 4:
					DrawStick(i,j,cubeDisX,cubeDisY,320,320)
				elif j == 5:
					DrawStick(i,j,cubeDisX,cubeDisY,320,395)
				elif j == 6:
					DrawStick(i,j,cubeDisX,cubeDisY,395,245)
				elif j == 7:
					DrawStick(i,j,cubeDisX,cubeDisY,395,320)
				elif j == 8:
					DrawStick(i,j,cubeDisX,cubeDisY,395,395)
			elif i == 2:
				if j == 0:
					DrawStick(i,j,cubeDisX,cubeDisY,480,245)
				elif j == 1:
					DrawStick(i,j,cubeDisX,cubeDisY,480,320)
				elif j == 2:
					DrawStick(i,j,cubeDisX,cubeDisY,480,395)
				elif j == 3:
					DrawStick(i,j,cubeDisX,cubeDisY,555,245)
				elif j == 4:
					DrawStick(i,j,cubeDisX,cubeDisY,555,320)
				elif j == 5:
					DrawStick(i,j,cubeDisX,cubeDisY,555,395)
				elif j == 6:
					DrawStick(i,j,cubeDisX,cubeDisY,630,245)
				elif j == 7:
					DrawStick(i,j,cubeDisX,cubeDisY,630,320)
				elif j == 8:
					DrawStick(i,j,cubeDisX,cubeDisY,630,395)
			elif i == 3:
				if j == 0:
					DrawStick(i,j,cubeDisX,cubeDisY,715,245)
				elif j == 1:
					DrawStick(i,j,cubeDisX,cubeDisY,715,320)
				elif j == 2:
					DrawStick(i,j,cubeDisX,cubeDisY,715,395)
				elif j == 3:
					DrawStick(i,j,cubeDisX,cubeDisY,790,245)
				elif j == 4:
					DrawStick(i,j,cubeDisX,cubeDisY,790,320)
				elif j == 5:
					DrawStick(i,j,cubeDisX,cubeDisY,790,395)
				elif j == 6:
					DrawStick(i,j,cubeDisX,cubeDisY,865,245)
				elif j == 7:
					DrawStick(i,j,cubeDisX,cubeDisY,865,320)
				elif j == 8:
					DrawStick(i,j,cubeDisX,cubeDisY,865,395)
			elif i == 4:
				if j == 0:
					DrawStick(i,j,cubeDisX,cubeDisY,245,10)
				elif j == 1:
					DrawStick(i,j,cubeDisX,cubeDisY,245,85)
				elif j == 2:
					DrawStick(i,j,cubeDisX,cubeDisY,245,160)
				elif j == 3:
					DrawStick(i,j,cubeDisX,cubeDisY,320,10)
				elif j == 4:
					DrawStick(i,j,cubeDisX,cubeDisY,320,85)
				elif j == 5:
					DrawStick(i,j,cubeDisX,cubeDisY,320,160)
				elif j == 6:
					DrawStick(i,j,cubeDisX,cubeDisY,395,10)
				elif j == 7:
					DrawStick(i,j,cubeDisX,cubeDisY,395,85)
				elif j == 8:
					DrawStick(i,j,cubeDisX,cubeDisY,395,160)
			elif i == 5:
				if j == 0:
					DrawStick(i,j,cubeDisX,cubeDisY,245,480)
				elif j == 1:
					DrawStick(i,j,cubeDisX,cubeDisY,245,555)
				elif j == 2:
					DrawStick(i,j,cubeDisX,cubeDisY,245,630)
				elif j == 3:
					DrawStick(i,j,cubeDisX,cubeDisY,320,480)
				elif j == 4:
					DrawStick(i,j,cubeDisX,cubeDisY,320,555)
				elif j == 5:
					DrawStick(i,j,cubeDisX,cubeDisY,320,630)
				elif j == 6:
					DrawStick(i,j,cubeDisX,cubeDisY,395,480)
				elif j == 7:
					DrawStick(i,j,cubeDisX,cubeDisY,395,555)
				elif j == 8:
					DrawStick(i,j,cubeDisX,cubeDisY,395,630)

	# Draw Stickers Hover over
	if x > cubeDisX + 10 and x < cubeDisX+75:
		StickerSel(y, cubeDisX, cubeDisY, 10, 245) 
	elif x > cubeDisX + 85 and x < cubeDisX+150:
		StickerSel(y, cubeDisX, cubeDisY, 85, 245)  
	elif x > cubeDisX + 160 and x < cubeDisX+225:
		StickerSel(y, cubeDisX, cubeDisY, 160, 245)
	elif x > cubeDisX+245 and x < cubeDisX+310:
		StickerSel(y, cubeDisX, cubeDisY, 245, 245)   
		StickerSel(y, cubeDisX, cubeDisY, 245, 480)
		StickerSel(y, cubeDisX, cubeDisY, 245, 10)
	elif x > cubeDisX+320 and x < cubeDisX+385:
		StickerSel(y, cubeDisX, cubeDisY, 320, 245)
		StickerSel(y, cubeDisX, cubeDisY, 320, 480)
		StickerSel(y, cubeDisX, cubeDisY, 320, 10)
	elif x > cubeDisX+395 and x < cubeDisX+460:
		StickerSel(y, cubeDisX, cubeDisY, 395, 245)
		StickerSel(y, cubeDisX, cubeDisY, 395, 480)
		StickerSel(y, cubeDisX, cubeDisY, 395, 10)       
	elif x > cubeDisX+480 and x < cubeDisX+545:
		StickerSel(y, cubeDisX, cubeDisY, 480, 245) 
	elif x > cubeDisX+555 and x < cubeDisX+620:
		StickerSel(y, cubeDisX, cubeDisY, 555, 245) 
	elif x > cubeDisX+630 and x < cubeDisX+695:
		StickerSel(y, cubeDisX, cubeDisY, 630, 245) 
	elif x > cubeDisX+715 and x < cubeDisX+780:
		StickerSel(y, cubeDisX, cubeDisY, 715, 245)  
	elif x > cubeDisX+790 and x < cubeDisX+855:
		StickerSel(y, cubeDisX, cubeDisY, 790, 245)
	elif x > cubeDisX+865 and x < cubeDisX+930:
		StickerSel(y, cubeDisX, cubeDisY, 865, 245) 

	if GameMenuCount%2 != 0:
		pygame.mixer.music.unpause()
	if GameMenuCount%2 == 0:
		pygame.mixer.music.pause()
	
def NotValidMenu():
	DrawSky()

	# Draw Grass 
	count = 0
	for x in range(0, width, GrassWidth):
		rand = RandGrass[count]
		if rand == 1:
			screen.blit( grass2, (x, height-GrassHeight))
		elif rand == 2:
			screen.blit( grass2, (x, height-GrassHeight))
		elif rand == 3:
			screen.blit( grass3, (x, height-GrassHeight))
		count = count + 1

	screen.blit(CubeSign, (width//2-CubeSignW//2, height-GrassHeight-CubeSignH+40))

clock = pygame.time.Clock()
done = False
while not done: 
	# Frame rate 
	clock.tick(60)

	if InMenu == True:
		MainMenu()

	elif InGame == True:
		GameMenu()
	
	elif NotValid == True:
		NotValidMenu()
		
	# updates the frames of the game 
	pygame.display.update() 
