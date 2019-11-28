import pygame

pygame.init()

blanc = (255,255,255)
noir = (0,0,0)
rouge = (255,0,0)
bleufond = (135,206,250)





liste1 = [
(0,0,0,2,2,2,2,2,0,0),
(0,2,2,2,2,1,1,1,3,0)]

fenetre = pygame.display.set_mode((1920, 1080),pygame.RESIZABLE)
fenetre.fill(bleufond)


def rectangle(fen,c,x,y,t):
    if c == 1:
        color = blanc
    elif c == 2:
        color = noir
    elif c == 3:
        color = rouge
    if c != 0:
        pygame.draw.rect(fen,color,(x,y,t,t))

def mario(fen,xpos,ypos,l,liste):
    for i in range(len(liste)):
        for x in range(len(liste[i])):
            rectangle(fen,liste[i][x],xpos+x*l,ypos+l*i,l)

mario(fenetre,0,0,15,liste1)





pygame.display.flip()

jeu = True

while jeu == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jeu = False


pygame.display.quit()
pygame.quit()