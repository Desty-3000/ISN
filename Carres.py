import pygame
from random import randint

pygame.init()

fenetre = pygame.display.set_mode((1920, 1080),pygame.RESIZABLE)

jeu = True

ListeCarre = []


def RefreshRect():

    fenetre.fill((0,0,0))

    for carre in ListeCarre:
        pygame.draw.rect(fenetre,(randint(0, 255),randint(0, 255),randint(0, 255)),carre)

    pygame.display.update()



while jeu == True:

    for event in pygame.event.get():

        if pygame.mouse.get_pressed()[0]:

            rect = pygame.Rect(event.pos[0]-25,event.pos[1]-25,50,50)
            ListeCarre.append(rect)

        if event.type == pygame.KEYDOWN:


            if event.key == 274:

                for carre in ListeCarre:
                    carre.move_ip(0,10)



        if event.type == pygame.QUIT:
            jeu = False

    RefreshRect()


pygame.display.quit()
pygame.quit()