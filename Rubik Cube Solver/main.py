import pygame, sys, math, time 
import os
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

CubeLst = [cube0, cube1, cube2, cube1, cube0]

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

TitleCount = 0

def title():
    global TitleCount

    if Title.get_rect().collidepoint(pygame.mouse.get_pos()):
        TitleCount = TitleCount + 1
        screen.blit(Title1, (50, 50))
        screen.blit(light1, (0,0))
        screen.blit(light1, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return GameMenu()

        if TitleCount == 1:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('assets/Heaven.wav'), maxtime=-1)
            pygame.mixer.Channel(0).set_volume(1)
        pygame.mixer.music.set_volume(0)



    else:
        screen.blit(Title, (50, 50))
        screen.blit(light, (0,0))
        screen.blit(light, (0,0))
        TitleCount = 0
        pygame.mixer.Channel(0).set_volume(0)
        pygame.mixer.music.set_volume(0.5)

def GameMenu():
    screen.fill((0,0,255))
    pygame.display.flip()


def MainMenu():
    global FireFrame, CubeFrame

    # Draw Sky
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
    CubeFrame = CubeFrame + 1

    # Draw Fire 
    screen.blit(FireLst[FireFrame%12], (width-CubeWidth-FireWidth+45, height-GrassHeight-FireHeight+95))
    FireFrame = FireFrame + 1

    # Draw Title
    title()


clock = pygame.time.Clock()

while True: 
    # Frame rate 
    clock.tick(60)

    for ev in pygame.event.get(): 
          
        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE or (ev.type == pygame.QUIT): 
            pygame.quit() 

    MainMenu()
        
    # updates the frames of the game 
    pygame.display.update() 
