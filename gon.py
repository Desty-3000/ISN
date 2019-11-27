import pygame
from math import *

pygame.init()

fenetre = pygame.display.set_mode((1920, 1080),pygame.RESIZABLE)

jaune = (255,220,0)
blanc = (255,255,255)
noir = (0,0,0)
beige = (255,220,177)
bleufond = (135,206,250)
marronOeil = (205,133,63)

vertCheveux = (0, 14, 0)
vertCheveux2 = (58, 137, 35)

fenetre.fill(bleufond)
faceCoteGauche = ((950,500),(850,450),(870,480),(750,460),(800,490),(700,490),(735,510),(688,540),(715,535),(698,575),(715,562),(698,600),(770,890),(945,990),(950,990))
faceCoteDroit = []

faceContourGauche = ((696,600),(768,892),(943,992),(950,993))
faceContourDroit = []

effacement1 = ((698,600),(770,890),(945,990),(950,990))
effacement2 = []

sourcilGauche = ((870,570),(800,540),(720,595))
sourcilDroit = []

sourcilDessusGauche = ((870,574),(800,542),(720,599))
sourcilDessusDroit = []


for i in range(len(faceCoteGauche)):
    faceCoteDroit.append([(950 - faceCoteGauche[i][0])+950,faceCoteGauche[i][1]])
for i in range(len(faceContourGauche)):
    faceContourDroit.append([(950 - faceContourGauche[i][0])+950,faceContourGauche[i][1]])
for i in range(len(effacement1)):
    effacement2.append([(950 - effacement1[i][0])+950,effacement1[i][1]])



for i in range(len(sourcilGauche)):
    if i==0:
        sourcilDroit.append([(950 - sourcilGauche[2][0])+920,sourcilGauche[0][1]])
    elif i==2:
        sourcilDroit.append([(950 - sourcilGauche[0][0])+920,sourcilGauche[2][1]])
    else:
        sourcilDroit.append([(950 - sourcilGauche[i][0])+920,sourcilGauche[i][1]])

for i in range(len(sourcilDessusGauche)):
    if i==0:
        sourcilDessusDroit.append([(950 - sourcilDessusGauche[2][0])+920,sourcilDessusGauche[0][1]])
    elif i==2:
        sourcilDessusDroit.append([(950 - sourcilDessusGauche[0][0])+920,sourcilDessusGauche[2][1]])
    else:
        sourcilDessusDroit.append([(950 - sourcilDessusGauche[i][0])+920,sourcilDessusGauche[i][1]])


pygame.draw.polygon(fenetre,vertCheveux,((700,700),(600,250),(698,400),(710,140),(770,350),(860,110),(880,300),(1095,60),(1100,355),(1350,130),(1250,440),(1380,350),(1200,700)))

pygame.draw.polygon(fenetre,noir,faceContourGauche)
pygame.draw.polygon(fenetre,noir,faceContourDroit)

pygame.draw.polygon(fenetre,beige,faceCoteGauche)
pygame.draw.polygon(fenetre,beige,faceCoteDroit)

pygame.draw.ellipse(fenetre,noir,(680,670,90,150))
pygame.draw.ellipse(fenetre,noir,(1130,670,90,150))

pygame.draw.ellipse(fenetre,beige,(682,672,86,146))
pygame.draw.ellipse(fenetre,beige,(1132,672,86,146))


pygame.draw.polygon(fenetre,beige,effacement1)
pygame.draw.polygon(fenetre,beige,effacement2)

pygame.draw.polygon(fenetre,noir,sourcilGauche)
pygame.draw.polygon(fenetre,noir,sourcilDroit)

pygame.draw.polygon(fenetre,beige,sourcilDessusGauche)
pygame.draw.polygon(fenetre,beige,sourcilDessusDroit)

pygame.draw.ellipse(fenetre,noir,(759,593,120,155))
pygame.draw.ellipse(fenetre,noir,(1019,593,120,155))

pygame.draw.ellipse(fenetre,blanc,(765,600,120,155))
pygame.draw.ellipse(fenetre,blanc,(1015,600,120,155))

pygame.draw.ellipse(fenetre,marronOeil,(823,621,50,120))
pygame.draw.ellipse(fenetre,marronOeil,(1027,621,50,120))

pygame.draw.ellipse(fenetre,noir,(838,640,25,80))
pygame.draw.ellipse(fenetre,noir,(1040,640,25,80))

pygame.draw.polygon(fenetre,noir,((950,770),(920,790),(938,810)))
pygame.draw.polygon(fenetre,beige,((956,770),(926,790),(945,810)))

pygame.draw.arc(fenetre,noir,(820,790,250,100),7/6*pi,0,5)

pygame.display.flip()

jeu = True

while jeu == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jeu = False


pygame.display.quit()
pygame.quit()