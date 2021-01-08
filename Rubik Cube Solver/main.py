import pygame, sys, math, time, os
from random import randint
from pygame import mixer
  
# initialize
pygame.mixer.pre_init()
pygame.mixer.init()
pygame.init()

# start playing the background music
pygame.mixer.music.load(os.path.join(os.getcwd(), 'assets', 'Loop.wav'))
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(loops=-1)  # loop forever

# Set Screen res(1920, 1080)
screen = pygame.display.set_mode(size = (1920, 1080)) 

# width of the screen
width = screen.get_width() 
# height of the screen
height = screen.get_height()  

InMenu = True
InGame = True

# ===== Assets ===== 

# Sky 
SkyWidth = 320
SkyHeight = math.floor((SkyWidth * 5) / 8)
sky1t = pygame.image.load('assets/sky0.png')
sky1 = pygame.transform.scale(sky1t, (SkyWidth, SkyHeight))

sky2t = pygame.image.load('assets/sky1.png')
sky2 = pygame.transform.scale(sky2t, (SkyWidth, SkyHeight))

sky3t = pygame.image.load('assets/sky2.png')
sky3 = pygame.transform.scale(sky3t, (SkyWidth, SkyHeight))

# Grass 
GrassWidth = 250
GrassHeight = 140
grass1 = pygame.image.load('assets/Grass0.png')
grass2 = pygame.image.load('assets/Grass1.png')
grass3 = pygame.image.load('assets/Grass2.png')

# Cube 
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

scalerCs = 0.55
CubeWidths = math.floor(690 * scalerCs)
CubeHeights = math.floor(800 * scalerCs)
cube0s = pygame.transform.scale(cube0t, (CubeWidths, CubeHeights))
cube1s = pygame.transform.scale(cube1t, (CubeWidths, CubeHeights))
cube2s = pygame.transform.scale(cube2t, (CubeWidths, CubeHeights))

CubeLst = [cube0, cube1, cube2, cube1, cube0]
CubeLsts = [cube2s, cube1s, cube0s, cube1s, cube2s]


# Title 
TitleWidth = 800
TitleHeight = math.floor(TitleWidth / 2)
Titlet0 = pygame.image.load('assets/TitleW.png')
Titlet1 = pygame.image.load('assets/TitleB.png')
Title = pygame.transform.scale(Titlet1, (TitleWidth, TitleHeight))
Title1 = pygame.transform.scale(Titlet0, (TitleWidth, TitleHeight))

# Fire 
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

FireLst = [Fire0, Fire1, Fire2, Fire3, Fire4, Fire5, Fire6, Fire7, Fire8, Fire9, Fire10, Fire11]

# Glow 
light_t0 = pygame.image.load('assets/glow.png')
light_t1 = pygame.image.load('assets/GlowTitle.png')
light = pygame.transform.scale(light_t0, (width, height))
light1 = pygame.transform.scale(light_t1, (width, height))

# FaceSelect 
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

# Cube Fold 
scalerCube = 1
CubeFoldWidth = 1035*scalerCube
CubeFoldHeight = 775*scalerCube
CubeFoldt = pygame.image.load('assets/CubeFold.png')
CubeFold = pygame.transform.scale(CubeFoldt,(CubeFoldWidth, CubeFoldHeight))

# Solve Button 
scaleSBut = 1
SolveButtonWidth = math.floor(400*scaleSBut)
SolveButtonHeight = math.floor(146*scaleSBut)
SolveButt = pygame.image.load('assets/Solve.png')
SolveBut = pygame.transform.scale(SolveButt, (SolveButtonWidth, SolveButtonHeight))

# Home Button 
scalerHome = 6
HomeButWidth = math.floor(11*scalerHome)
HomeButHeight = math.floor(7*scalerHome)
HomeButt = pygame.image.load('assets/Home.png')
HomeBut = pygame.transform.scale(HomeButt, (HomeButWidth, HomeButHeight))

# Sound-On Button 
scalerSound = 6
SoundOnWidth = math.floor(11*scalerHome)
SoundOnHeight = math.floor(7*scalerHome)
SoundOnt = pygame.image.load('assets/SoundON.png')
SoundOn = pygame.transform.scale(SoundOnt, (SoundOnWidth, SoundOnHeight))

# Title Bar 
scalerTitleBar = 0.25
TitleBarWidth = math.floor(250 * scalerTitleBar)
TitleBarHeight = TitleBarWidth
TitleBart = pygame.image.load('assets/TitleBar.png')
TitleBar = pygame.transform.scale(TitleBart, (TitleBarWidth, TitleBarHeight))



def SkyTiles(w, h, skyW, skyH):
    SkyHorzTile = math.ceil(w / skyW)
    SkyVerTile = math.ceil(h / skyH) 
    rand = [randint(1,3) for i in range(SkyHorzTile*SkyVerTile)]
    return rand

def GrassTiles(w, GrassW):
    GrassHorzTile = math.ceil(w / GrassW)
    rand = [randint(1,3) for i in range(GrassHorzTile)]
    return rand

RandSky = SkyTiles(width, height, SkyWidth, SkyHeight)
RandGrass = GrassTiles(width, GrassWidth)

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

def title():
    global TitleCount, InMenu, GameMenu

    if Title.get_rect().collidepoint(pygame.mouse.get_pos()):
        TitleCount = TitleCount + 1
        screen.blit(Title1, (50, 50))

        if TitleCount == 1:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('assets/Heaven.wav'), maxtime=-1)
            pygame.mixer.Channel(0).set_volume(1)
        pygame.mixer.music.set_volume(0)

    else:
        screen.blit(Title, (50, 50))
        screen.blit(light, (0,0))
        TitleCount = 0
        pygame.mixer.Channel(0).set_volume(0)
        pygame.mixer.music.set_volume(0.5)

def MainMenu():
    global FireFrame, CubeFrame, InGame, InMenu

    # Draw Sky
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

    # Draw Cube
    screen.blit(CubeLst[math.ceil((CubeFrame%12)/3)], (width-CubeWidth, height-GrassHeight-CubeHeight+40))
    screen.blit(CubeLsts[math.ceil((CubeFrame%12)/3)], (width-CubeWidth-FireWidth-CubeWidths+80, height-GrassHeight-CubeHeights+40))
    CubeFrame = CubeFrame + 1

    # Draw Fire 
    screen.blit(FireLst[FireFrame%12], (width-CubeWidth-FireWidth+45, height-GrassHeight-FireHeight+95))
    FireFrame = FireFrame + 1

    # Draw Title
    title()

    for ev in pygame.event.get(): 
        if ev.type == pygame.MOUSEBUTTONDOWN:
            x, y = ev.pos
            if Title1.get_rect().collidepoint(x, y):
                InMenu = False
                InGame = True

def GameMenu():
    global InGame, InMenu
    DrawSky()
    pygame.mixer.Channel(0).set_volume(0)
    pygame.mixer.music.set_volume(0.5)

    # Draw Solve Button
    screen.blit(SolveBut, (width-SolveButtonWidth - 20, height - SolveButtonHeight - 80 + TitleBarHeight))

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

    # Draw selection cube
    x, y = pygame.mouse.get_pos() 
    if x > cubeDisX+20 and x < cubeDisX+257 and y > cubeDisY+262 and y < cubeDisY+500:
        screen.blit(CubeBL, (20, 20 + TitleBarHeight))
    elif x > cubeDisX+278 and x<cubeDisX+513 and y > cubeDisY+262 and y < cubeDisY+500:
        screen.blit(CubeTop, (20, 20 + TitleBarHeight))
    elif x > cubeDisX+534 and x < cubeDisX+769 and y > cubeDisY+262 and y < cubeDisY+500:
        screen.blit(CubeFR, (20, 20 + TitleBarHeight))
    elif x > cubeDisX+790 and x < cubeDisX+1025 and y > cubeDisY+262 and y < cubeDisY+500:
        screen.blit(CubeBot, (20, 20 + TitleBarHeight))
    elif x > cubeDisX+278 and x<cubeDisX+513 and y > cubeDisY+11 and y < cubeDisY+245:
        screen.blit(CubeBR, (20, 20 + TitleBarHeight))
    elif x > cubeDisX+278 and x<cubeDisX+513 and y > cubeDisY+520 and y < cubeDisY+758:
        screen.blit(CubeFL, (20, 20 + TitleBarHeight))
    else:
        screen.blit(CubeEmpty, (20, 20 + TitleBarHeight))

    for ev in pygame.event.get(): 
        if ev.type == pygame.MOUSEBUTTONDOWN:
            x, y = ev.pos
            print(HomeBut.get_rect())
            print(x, y)
            if HomeBut.get_rect().collidepoint(x, y):
                InMenu = True
                InGame = False     

clock = pygame.time.Clock()

while True: 
    # Frame rate 
    clock.tick(60)

    for ev in pygame.event.get(): 
          
        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE: 
            pygame.quit()

    if InMenu == True:
        MainMenu()

    elif InGame == True:
        GameMenu()
        
        
    # updates the frames of the game 
    pygame.display.update() 
