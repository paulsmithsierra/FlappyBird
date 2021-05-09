# This is a recreation of the famous game "Flappy Bird"
# Made by:
# Quentin DEMURGE (email: ) and Paul SMITH (email: paulsierra817@gmail.com)
# IUT Lyon 1 - LP RAVI


from random import randint
import pygame
from pygame import K_SPACE
import core
from bird import Bird
from obstacle import Obstacle


# ---Variables globales---
# Flappy Bird
flappy = Bird()
saut_front_montant = None
# Tuyaux
tuyau_1H = Obstacle()
tuyau_1B = Obstacle()
tuyau_2H = Obstacle()
tuyau_2B = Obstacle()
# Sol
sol = Obstacle()
# Autres
boucle_run = None



def setup():
    print("Setup START---------")
    global boucle_run
    boucle_run = True

    # ---Fenêtre---
    core.fps = 30
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
    tuyau_1H.posY2 = randint(1, 250)
    tuyau_1H.compteur_moveX1 = 0
    ## Bas
    tuyau_1B.couleur = "dark green"
    tuyau_1B.posX1 = 800
    tuyau_1B.posY1 = tuyau_1H.posY2 + 150
    tuyau_1B.posX2 = 50
    tuyau_1B.posY2 = 500
    tuyau_1B.compteur_moveX1 = 0

    # N°Tuyau 2
    ## Haut
    tuyau_2H.couleur = "dark green"
    tuyau_2H.posX1 = 1200
    tuyau_2H.posY1 = 0
    tuyau_2H.posX2 = 50
    tuyau_2H.posY2 = randint(1, 250)
    tuyau_2H.compteur_moveX1 = 0
    ## Bas
    tuyau_2B.couleur = "dark green"
    tuyau_2B.posX1 = 1200
    tuyau_2B.posY1 = tuyau_2H.posY2 + 150
    tuyau_2B.posX2 = 50
    tuyau_2B.posY2 = 500
    tuyau_2B.compteur_moveX1 = 0


    # ---Setup Sol---
    sol.couleur = "brown"
    sol.posX1 = 0
    sol.posY1 = 400
    sol.posX2 = 800
    sol.posY2 = 100


    print("Setup END-----------")


def run():
    print("running")

    # ---Tuyaux---
    # Haut 1
    tuyau_1H.affichage()
    tuyau_1H.move()
    # Bas 1
    tuyau_1B.affichage()
    tuyau_1B.move()
    # Haut 2
    tuyau_2H.affichage()
    tuyau_2H.move()
    # Bas 2
    tuyau_2B.affichage()
    tuyau_2B.move()

    # ---Flappy Bird---
    flappy.affichage()
    flappy.gravite(5)

    # ---Sol---
    sol.affichage()

    # ---Actions---
    # Sauter (spacebar)
    if pygame.key.get_pressed() [K_SPACE]:

        flappy.saut(30)

    # Collision
    if flappy.forme.colliderect(sol.forme):
        print("collision sol")

    elif flappy.forme.colliderect(tuyau_1H.forme):
        print("collision tuyau 1")

    elif flappy.forme.colliderect(tuyau_2H.forme):
        print("collision tuyau 2")


if __name__ == '__main__':

    core.main(setup, run)
