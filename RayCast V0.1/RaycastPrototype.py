from ast import While
import cv2
import numpy as np
import math
Img = cv2.imread("Untitled.png")
#10 is middle
Grid = np.zeros((20, 20)).tolist()
for i in range(len(Img)):
    for j in range(len(Img[0])):
        if(Img[i][j][1] != 0): 
            Grid[i][j] = 1

Grid[1][11] = 1
#Grid[1][12] = 1
StX = 4
StY = 10
Grid[StX][StY] = 2



def GetDis(Start, End):
    NewTup = (Start[0] - End[0], Start[1] - End[1])
    Dis = math.sqrt(math.pow(NewTup[0], 2) + math.pow(NewTup[1], 2))
    return Dis



print(np.array(Grid))
import pygame
windowx = 310
windowy = 300
win = pygame.display.set_mode((windowx, windowy))
pygame.display.set_caption("Ida's Snake Game")
win.fill((0,0,0))
#this is an extremly slow Raycaster
for i in range(75, 106):
    Index =  i * (math.pi/180) # (105 - (i-75))

    Found = False
    TimesNumber = 1
    Saved = ()
    while not Found:
        Xget = StX - round(math.sin(Index) * TimesNumber)
        Yget = StY - round(math.cos(Index) * TimesNumber)

        if(Grid[Xget][Yget] == 1):
            TrueHit = ((StX - math.sin(Index) * TimesNumber), (StY - math.cos(Index) * TimesNumber))
            nnjf = (Saved[0] - Xget)  
            weer = (Saved[1] - Yget)  
            colo = (0, 255, 0)
            if abs(nnjf) > abs(weer):
                colo = (0, 100, 0)
            
            DisToEnd = round(GetDis((StX, StY), TrueHit), 10)
            #0.785398

            DrawInd = (i - 75) * 10

            pygame.draw.rect(win, colo, (DrawInd, 0, 10, int(300/DisToEnd)))

            Found = True
        Saved = ((StX - math.sin(Index) * TimesNumber), (StY - math.cos(Index) * TimesNumber))
        TimesNumber += 0.05

 
pygame.display.update()
run = True
while(run):
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:

            run = False