# This is a recreation of the famous game "Flappy Bird"
# Made by:
# Quentin DEMURGE (email: ) and Paul SMITH (email: paulsierra817@gmail.com)
# IUT Lyon 1 - LP RAVI

import sys
from random import randint
import pygame
from pygame import K_SPACE
import core
from bird import Bird
from obstacle import Obstacle


# ---Variables globales---
# Flappy Bird
flappy = Bird()
# Tuyaux
tuyau_1H = Obstacle()
tuyau_1B = Obstacle()
tuyau_2H = Obstacle()
tuyau_2B = Obstacle()
# Sol
sol = Obstacle()
# Score
score = None
# Autres



def setup():
    print("Setup START---------")

    # ---Fenêtre---
    core.fps = 60
    core.WINDOW_SIZE = [800, 500]

    # ---Setup Flappy---
    flappy.couleur = "yellow"
    flappy.pos_x = 80
    flappy.pos_y = 150
    flappy.rayon = 20

    # ---Setup Obstacles---
    # N°Tuyau 1
    ## Haut
    tuyau_1H.couleur = "dark green"
    tuyau_1H.posX1 = 800
    tuyau_1H.posY1 = 0
    tuyau_1H.posX2 = 50
    tuyau_1H.posY2 = randint(0, 200)



    ## Bas
    tuyau_1B.couleur = "dark green"
    tuyau_1B.posX1 = 800
    tuyau_1B.posY1 = tuyau_1H.posY2 + 150
    tuyau_1B.posX2 = 50
    tuyau_1B.posY2 = 500



    # N°Tuyau 2
    ## Haut
    tuyau_2H.couleur = "dark green"
    tuyau_2H.posX1 = 1200
    tuyau_2H.posY1 = 0
    tuyau_2H.posX2 = 50
    tuyau_2H.posY2 = randint(0, 200)



    ## Bas
    tuyau_2B.couleur = "dark green"
    tuyau_2B.posX1 = 1200
    tuyau_2B.posY1 = tuyau_2H.posY2 + 150
    tuyau_2B.posX2 = 50
    tuyau_2B.posY2 = 500



    # ---Setup Sol---
    sol.couleur = "brown"
    sol.posX1 = 0
    sol.posY1 = 400
    sol.posX2 = 800
    sol.posY2 = 100


    # ---Setup Score---
    global score
    score = 0

    # ---Setup Boucle Partie---




    print("Setup END-----------")




def run():


    # ---Tuyaux---
    # Haut 1
    tuyau_1H.affichage()
    tuyau_1H.move("H")


    # Bas 1
    tuyau_1B.affichage()
    tuyau_1B.move("B")
    tuyau_1B.posY1 = tuyau_1H.posY2 + 150

    # Haut 2
    tuyau_2H.affichage()
    tuyau_2H.move("H")


    # Bas 2
    tuyau_2B.affichage()
    tuyau_2B.move("B")
    tuyau_2B.posY1 = tuyau_2H.posY2 + 150



    # ---Flappy Bird---
    flappy.affichage()
    flappy.gravite(3)


    # ---Sol---
    sol.affichage()


    # ---Score---
    global score
    if tuyau_1H.posX1 == (flappy.pos_x - flappy.rayon):

        score = score + 1
        print(score)

    if tuyau_2H.posX1 == (flappy.pos_x - flappy.rayon):

        score = score + 1
        print(score)


    # ---Actions---
    # Sauter (spacebar)
    for event in pygame.event.get():  # User did something

        #Close window (X red corner icon)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #Appui barre d'espace
        elif event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                flappy.saut(60)



    # Collision
    if flappy.forme.colliderect(sol.forme):
        print("collision sol")
        score = 0

    elif flappy.forme.colliderect(tuyau_1H.forme):
        print("collision tuyau 1")
        score = 0

    elif flappy.forme.colliderect(tuyau_1B.forme):
        print("collision tuyau 1")
        score = 0


    elif flappy.forme.colliderect(tuyau_2H.forme):
        print("collision tuyau 2")
        score = 0


    elif flappy.forme.colliderect(tuyau_2B.forme):
        print("collision tuyau 2")
        score = 0




if __name__ == '__main__':

    core.main(setup, run)
