
import cv2
import numpy as np
import math
import time
Img = cv2.imread("Name.png")
#10 is middle
Grid = np.zeros((len(Img), len(Img[0]))).tolist()
for i in range(len(Img)):
    for j in range(len(Img[0])):
        if(int(Img[i][j][0]) + Img[i][j][1] + Img[i][j][2] != 0): 
            Grid[i][j] = np.argmax(Img[i][j])+1


Grid[1][0] = 1
Grid[2][0] = 1


Turn = 55

def GetDis(Start, End):
    NewTup = (Start[0] - End[0], Start[1] - End[1])
    Dis = math.sqrt(math.pow(NewTup[0], 2) + math.pow(NewTup[1], 2))
    return Dis

def Draw3D():
    win.fill((0,0,0))
    pygame.draw.rect(win, (158, 100, 205), (0, 200, 500, 400))
    Grid[StX][StY] = -2
    #print(np.array(Grid))

    for i in range(Turn, Turn+161):
        Index =  (i*1) * (math.pi/180) # (105 - (i-75))

        Found = False
        TimesNumber = 1
        Saved = (0,0)
        while not Found:
            Xget = StX - round(math.sin(Index) * TimesNumber)
            Yget = StY - round(math.cos(Index) * TimesNumber)

            colo = (255,0,0)
            colo2 = (100,0,0)

            if(Grid[Xget][Yget] >= 1):
                match Grid[Xget][Yget]:
                    case 1:
                        colo = (255,0,0)
                        colo2 = (100,0,0)
                    case 2:
                        colo = (0,255,0)
                        colo2 = (0,100,0)
                    case 3:
                        colo = (0,0,255)
                        colo2 = (0,0,100)

                TimesNumber -= 0.5
                SubtNum = 0.2
                timer = 0
                while not Found:
                    Xget = StX - round(math.sin(Index) * TimesNumber)
                    Yget = StY - round(math.cos(Index) * TimesNumber)

                    if(Grid[Xget][Yget] >= 1):
                        Found = True

                    Saved = ((StX - math.sin(Index) * TimesNumber), (StY - math.cos(Index) * TimesNumber))
                    if(SubtNum > 0.05):
                        SubtNum = SubtNum * 0.05
                    TimesNumber += SubtNum
                    timer += 1

                print(timer)

                TrueHit = ((StX - math.sin(Index) * TimesNumber), (StY - math.cos(Index) * TimesNumber))

                PreX = (Saved[0] - Xget)  
                PreY = (Saved[1] - Yget)  

                if abs(PreX) > abs(PreY):
                    colo = colo2
                
                DisToEnd = round(GetDis((StX, StY), TrueHit), 10)

                DrawInd = ((i*1) - Turn) * 7

                #if i == 135:



                pygame.draw.rect(win, colo, (DrawInd, 200, 7, int(300/DisToEnd)))


            Saved = ((StX - math.sin(Index) * TimesNumber), (StY - math.cos(Index) * TimesNumber))
            TimesNumber += 0.5  
    pygame.display.update()

    Grid[StX][StY] = 0



import pygame
windowx = 497
windowy = 500
win = pygame.display.set_mode((windowx, windowy))
pygame.display.set_caption("Ida's Raycast Box")


#45, 136)
#this is an extremly slow Raycaster
StX = 10
StY = 10

uioj = 9



Controls = [-1, 1, -1, 1]




run = True
while(run):
    pygame.time.delay(45)
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:

            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        Turn -= 5
        Draw3D()

    if keys[pygame.K_d]:
        Turn += 5
        Draw3D()

    if keys[pygame.K_LEFT] and not Grid[StX][StY - 1] >= 1:
        StY += Controls[0]
        Draw3D()

    if keys[pygame.K_RIGHT] and not Grid[StX][StY + 1] >= 1:
        StY += Controls[1]
        Draw3D()

    if keys[pygame.K_UP] and not Grid[StX - 1][StY] >= 1:
        StX += Controls[2]
        Draw3D()

    if keys[pygame.K_DOWN] and not Grid[StX + 1][StY] >= 1:
        StX += Controls[3]
        Draw3D()

    if uioj == 9:
        Draw3D()
        uioj += 1