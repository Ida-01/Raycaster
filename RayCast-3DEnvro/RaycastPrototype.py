from ast import While
import cv2
import numpy as np
import math
import time
Img = cv2.imread("Untitled.png")
#10 is middle
Grid = np.zeros((len(Img), len(Img[0]))).tolist()
for i in range(len(Img)):
    for j in range(len(Img[0])):
        if(Img[i][j][1] != 0): 
            Grid[i][j] = 1








def GetDis(Start, End):
    NewTup = (Start[0] - End[0], Start[1] - End[1])
    Dis = math.sqrt(math.pow(NewTup[0], 2) + math.pow(NewTup[1], 2))
    return Dis

def Draw3D():
    win.fill((0,0,0))
    pygame.draw.rect(win, (50, 0, 255), (0, 300, 450, 300))
    Grid[StX][StY] = 2
    print(np.array(Grid))
    for i in range(45, 136):
        Index =  (i*1) * (math.pi/180) # (105 - (i-75))

        Found = False
        TimesNumber = 1
        Saved = (0,0)
        while not Found:
            Xget = StX - round(math.sin(Index) * TimesNumber)
            Yget = StY - round(math.cos(Index) * TimesNumber)

            if(Grid[Xget][Yget] == 1):
                TimesNumber -= 0.5
                while not Found:
                    Xget = StX - round(math.sin(Index) * TimesNumber)
                    Yget = StY - round(math.cos(Index) * TimesNumber)

                    if(Grid[Xget][Yget] == 1):
                        Found = True

                    Saved = ((StX - math.sin(Index) * TimesNumber), (StY - math.cos(Index) * TimesNumber))
                    TimesNumber += 0.005

                TrueHit = ((StX - math.sin(Index) * TimesNumber), (StY - math.cos(Index) * TimesNumber))

                PreX = (Saved[0] - Xget)  
                PreY = (Saved[1] - Yget)  

                colo = (0, 255, 0)
                if abs(PreX) > abs(PreY):
                    colo = (0, 100, 0)
                
                DisToEnd = round(GetDis((StX, StY), TrueHit), 10)

                DrawInd = ((i*1) - 45) * 5

                #if i == 135:
                Subtrac = abs(90 - 90) / 75
                pygame.draw.rect(win, colo, (DrawInd, 300, 5, int(300/DisToEnd)))


            Saved = ((StX - math.sin(Index) * TimesNumber), (StY - math.cos(Index) * TimesNumber))
            TimesNumber += 0.5  
    pygame.display.update()

    Grid[StX][StY] = 0



import pygame
windowx = 450
windowy = 600
win = pygame.display.set_mode((windowx, windowy))
pygame.display.set_caption("Ida's Snake Game")


#45, 136)
#this is an extremly slow Raycaster
StX = 5
StY = 10

uioj = 9

run = True
while(run):
    pygame.time.delay(100)
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:

            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and not Grid[StX][StY - 1] == 1:
        StY -= 1
        Draw3D()

    if keys[pygame.K_RIGHT] and not Grid[StX][StY + 1] == 1:
        StY += 1
        Draw3D()

    if keys[pygame.K_UP] and not Grid[StX - 1][StY] == 1:
        StX -= 1
        Draw3D()

    if keys[pygame.K_DOWN] and not Grid[StX + 1][StY] == 1:
        StX += 1
        Draw3D()

    if uioj == 9:
        Draw3D()
        uioj += 1