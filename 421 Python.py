from random import*

#on veut lancer 3 dés , qui doivent au final former une suite 4,2,1. Si un des
#dés vaut 4,2,1 le dé n'est pas relancé . Au bout de 3 lancés sans la suite 421
#le joueur a perdu

#lancementDes lance n dés aléatoires entre 1 et 6 et stocke les résultats dans r1
def lancementDes(n):
    r1 = []
    for i in range(n):
        random = randint(1,6)
        r1.append(random)
    return r1



#Fonction principale du Script
def jeu():
    tour = 0
    #Dés valides
    listeFinale = []

    #On simule les 3 tours
    while tour!=3:
        #On lance (3-taille de listeFinale) dés

        lancementI = lancementDes(3-len(listeFinale))
        print("Lancement de ",3-len(listeFinale)," dés ... ",lancementI)

        #Si i est dans lancementI et pas dans listeFinale on ajoute i a listeFinale

        for i in range(5):
            if i!=3 and i not in listeFinale:
                if i in lancementI:
                    listeFinale.append(i)
                    listeFinale.sort()
                    print(i," ajouté")
        print(listeFinale," au tour ",tour+1)
        print(" ")
        tour+=1

    #On vérifie à la fin des lancés si listeFinale est complète ou non

    if tour==3 and listeFinale == [1,2,4]:
        return "Le joueur a gagné!"
    else:
        return "Le joueur a perdu!"


