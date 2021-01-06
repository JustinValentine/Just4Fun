import pygame, sys, math, time 
from random import randint
from pygame.locals import *
from pygame import mixer
  
pygame.init() 
  
screen = pygame.display.set_mode(size = (1920, 1080)) 

width = screen.get_width() # width of the screen
  
height = screen.get_height() # height of the screen
  
# colors
color = (255,255,255) # white color 
color_light = (170,170,170) # light shade of the button
color_dark = (100,100,100) # dark shade of the button 
bg = (60,25,60)


#Assets
SkyWidth = 320
SkyHeight = math.floor((SkyWidth * 5) / 8)
sky1t = pygame.image.load('assets/Sky/sky0.png')
sky1 = pygame.transform.scale(sky1t, (SkyWidth, SkyHeight))

sky2t = pygame.image.load('assets/Sky/sky1.png')
sky2 = pygame.transform.scale(sky2t, (SkyWidth, SkyHeight))

sky3t = pygame.image.load('assets/Sky/sky2.png')
sky3 = pygame.transform.scale(sky3t, (SkyWidth, SkyHeight))

GrassWidth = 250
GrassHeight = 140
grass1 = pygame.image.load('assets/Grass/Grass0.png')
grass2 = pygame.image.load('assets/Grass/Grass1.png')
grass3 = pygame.image.load('assets/Grass/Grass2.png')

CubeWidth = 690
CubeHeight = 800
cube = pygame.image.load('assets/Cube.png')

TitleWidth = 800
TitleHeight = math.floor(TitleWidth / 2)
Titlet = pygame.image.load('assets/CubeSolver.png')
Title = pygame.transform.scale(Titlet, (TitleWidth, TitleHeight))

FireFrame = 0
FireWidth = 400
FireHeight = FireWidth
Fire0 = pygame.image.load('assets/Fire/Fire0.png')
Fire1 = pygame.image.load('assets/Fire/Fire1.png')
Fire2 = pygame.image.load('assets/Fire/Fire2.png')
Fire3 = pygame.image.load('assets/Fire/Fire3.png')
Fire4 = pygame.image.load('assets/Fire/Fire4.png')
Fire5 = pygame.image.load('assets/Fire/Fire5.png')
Fire6 = pygame.image.load('assets/Fire/Fire6.png')
Fire7 = pygame.image.load('assets/Fire/Fire7.png')
Fire8 = pygame.image.load('assets/Fire/Fire8.png')
Fire9 = pygame.image.load('assets/Fire/Fire9.png')
Fire10 = pygame.image.load('assets/Fire/Fire10.png')
Fire11 = pygame.image.load('assets/Fire/Fire11.png')

FireLst = [Fire0, Fire1, Fire2, Fire3, Fire4, Fire5, Fire6, Fire7, Fire8]

# backgound sound 
mixer.music.load('Loop.mp3')
mixer.music.play(-1)

# Fonts
smallfont = pygame.font.SysFont('Corbel',35) 
text = smallfont.render('quit' , True , color) # rendering a text object

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

def MainMenu():
    global FireFrame

    # Backgound
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
    # Grass 
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

    # Cube
    screen.blit(cube, (width-CubeWidth, height-GrassHeight-CubeHeight+40))

    # Title
    screen.blit(Title, (50, 50))

    # fire 
 
    screen.blit(FireLst[FireFrame%9], (width-CubeWidth-FireWidth,height-GrassHeight-FireHeight+80))
    FireFrame = FireFrame + 1

    print(FireFrame//3)


clock = pygame.time.Clock()

while True: 
    clock.tick(30)

    for ev in pygame.event.get(): 
          
        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE or (ev.type == pygame.QUIT): 
            pygame.quit() 

    #screen.fill((60,25,60)) # fills the screen with a color

    MainMenu()
        
    # updates the frames of the game 
    pygame.display.update() 

