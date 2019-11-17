
# Pour cet exercice, j'ai choisi de découper le triangle en 2, puis de calculer un Yminimal et Ymaximal à l'aide d'équations de droites
# La découpe s'effectue au X de A , puisque c'est ici que Yminimal devient croissant
# Finalement quand j'ai vérifié que Ym est au dessus de Yminimal, j'utilise l'équation de BC puisqu'elle est décroissante stricte pour calculer un YMaximal,
# et vérifier que Ym ne dépasse pas ce dernier.

def triangle1(Xm,Ym):
# On commence par inisialiser les données requises tel que les coordonées , m ou p dans l'équation de droite y=mx+p pour [AB],[BC],[AC] dans des tuples car valeurs fixes
    A=(60,100)
    B=(90,130)
    C=(30,110)
    mDroites=((B[1]-A[1])/(B[0]-A[0]),(C[1]-B[1])/(C[0]-B[0]),(C[1]-A[1])/(C[0]-A[0])) #on a ici les m de AB,BC,AC
    pDroites=(A[1]-mDroites[0]*A[0],B[1]-mDroites[1]*B[0],C[1]-mDroites[2]*C[0])       #on a ici les p de AB,BC,AC

    if Xm>=30 and Xm<=60:                           #si Xm est plus grand que 30 jusqu'à 60 , alors ymin dépendera de l'équation de la droite AC
        ymin= mDroites[2]*Xm+pDroites[2]            #on calcule y en fonction de Xm avec l'équation de droite de AC
    elif Xm>60 and Xm<=90:                          #si Xm est plus grand que 60 , alors ymin dépendera de léquation de la droite AB
           ymin= mDroites[0]*Xm+pDroites[0]       #on calcule y en fonction de Xm avec l'équation de droite de AB
    elif Xm<30 or Xm>90:return False                #On retourne False si Xm n'est pas entre 30 et 90, car il sera obligatoirement hors du triangle
    if Ym>=ymin and Ym<=mDroites[1]*Xm+pDroites[1]: #On vérifie si Ym est au dessus des droites CA et AB , il ne reste plus qu'a vérifier que Ym est en dessous de BC avec ymax
        return True                                 #M est donc bien dans le triangle donc on retourne False
    else: return False                              #Ym ne remplie pas les conditions de ymin et ymax donc on retourne False



def oy(Xa,Ya,Xb,Yb): #On récupère les coordonnées de A et B
    if Xb==Xa and Ya!=Yb:       #si x est constant sur la droite , alors elle est parallèle aux ordonnées et A et B ne doivent pas être confondus
        return True
    else:
        return False



def réduite(Xa,Ya,Xb,Yb):
    if oy(Xa,Ya,Xb,Yb)!=True: #On utilise la fonction précédément créee pour vérifier que (AB) à une équation de la forme y=mx+p
        m=(Yb-Ya)/(Xb-Xa)
        p= Ya-m*Xa
        return m,p
    else:
        return Xa #si la condition n'est pas remplie alors Xa=Xb=x=c donc Xa=c
