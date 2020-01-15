import pygame

pygame.init()
jeu = True
BlueBallList = []
RedBallList = []

class BlueBall:
    xVec = 1
    yVec = 1
    Rect = pygame.Rect(0,0,50,50)
    def __init__(self,x,y):
        self.Rect.center = (x,y)
    def move(self):
        self.Rect = self.Rect.move(self.xVec,self.yVec)
        pygame.draw.ellipse(fenetre,blue,self.Rect)

class RedBall:
    xVec = 0
    yVec = 2
    Rect = pygame.Rect(0,0,20,20)
    def __init__(self,x,y):
        self.Rect.center = (x,y)
    def move(self):
        self.Rect = self.Rect.move(self.xVec,self.yVec)
        pygame.draw.ellipse(fenetre,red,self.Rect)

FPS = 500
X = 1024
Y = 800

fps_clock = pygame.time.Clock()
fenetre = pygame.display.set_mode((X, Y))

white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)
border = ((Y-50),(0),(X-50))

while jeu:

    fenetre.fill(white)

    for ball in BlueBallList:
        ball.move()
        if ball.Rect.y >= border[0] or ball.Rect.y <= border[1]:
            ball.yVec = -ball.yVec
        if ball.Rect.x>= border[2] or ball.Rect.x <= border[1]:
            ball.xVec = -ball.xVec
        for ball2 in BlueBallList:
            if ball.Rect.colliderect(ball2.Rect) and ball != ball2:
                ball.xVec = -ball.xVec
                ball.yVec = -ball.yVec
    for ball in RedBallList:
        ball.move()
        if ball.Rect.y >= border[0]+30:
            ball.yVec = 0
        for ball2 in RedBallList:
            if ball.Rect.colliderect(ball2.Rect) and ball != ball2:
                ball.yVec = 0
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            jeu = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                BlueBallList.append(BlueBall(event.pos[0],event.pos[1]))
            if event.button == 3:
                RedBallList.append(RedBall(event.pos[0],event.pos[1]))
    pygame.display.update()
    fps_clock.tick(FPS)

pygame.display.quit()
pygame.quit()