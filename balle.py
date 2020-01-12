import pygame

pygame.init()

BallList = []
xVecList = []
yVecList = []

FPS = 500
fps_clock = pygame.time.Clock()
fenetre = pygame.display.set_mode((1024, 800))

white = (255,255,255)
blue = (0,0,255)

jeu = True

while jeu:
    fenetre.fill(white)
    i = 0
    for test in BallList:
        test.move_ip(xVecList[i],yVecList[i])
        if test.y >= 800-50:
            yVecList[i] = -1
        elif test.y <= 0:
            yVecList[i] = 1
        if test.x >= 1024-50:
            xVecList[i]= -1
        elif test.x <= 0:
            xVecList[i] = 1
        pygame.draw.ellipse(fenetre,blue,test)
        i+=1
    pygame.display.update()
    fps_clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            jeu = False
        if pygame.mouse.get_pressed()[0]:
            newRect = pygame.Rect(100,100,50,50)
            newxVec = 1
            newyVec = 1
            BallList.append(newRect)
            xVecList.append(newxVec)
            yVecList.append(newyVec)


pygame.display.quit()
pygame.quit()