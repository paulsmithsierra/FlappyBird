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
tuyau_1 = Obstacle()
tuyau_2 = Obstacle()
espace_1 = Obstacle()
espace_2 = Obstacle()
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
    tuyau_1.O_couleur = "dark green"
    tuyau_1.O_posX1 = 800
    tuyau_1.O_posY1 = 0
    tuyau_1.O_posX2 = 50
    tuyau_1.O_posY2 = 500
    tuyau_1.O_compteur_moveX1 = 0
    # N°Tuyau 2
    tuyau_2.O_couleur = "dark green"
    tuyau_2.O_posX1 = 1200
    tuyau_2.O_posY1 = 0
    tuyau_2.O_posX2 = 50
    tuyau_2.O_posY2 = 500
    tuyau_2.O_compteur_moveX1 = 0

    # ---Setup Espaces---
    # N°1
    espace_1.O_couleur = "black"
    espace_1.O_posX1 = tuyau_1.O_posX1
    espace_1.O_posY1 = randint(50, 300)
    espace_1.O_posX2 = tuyau_1.O_posX2
    espace_1.O_posY2 = 125
    espace_1.O_compteur_moveX1 = 0
    # N°2
    espace_2.O_couleur = "black"
    espace_2.O_posX1 = tuyau_2.O_posX1
    espace_2.O_posY1 = randint(50, 300)
    espace_2.O_posX2 = tuyau_2.O_posX2
    espace_2.O_posY2 = 125
    espace_2.O_compteur_moveX1 = 0

    # ---Setup Sol---
    sol.O_couleur = "brown"
    sol.O_posX1 = 0
    sol.O_posY1 = 400
    sol.O_posX2 = 800
    sol.O_posY2 = 100


    print("Setup END-----------")


def run():
    print("running")

    # ---Tuyaux---
    # N°1
    tuyau_1.affichage()
    tuyau_1.move()
    # N°2
    tuyau_2.affichage()
    tuyau_2.move()

    # ---Espaces---
    # N°1
    espace_1.affichage()
    espace_1.move()
    # N°2
    espace_2.affichage()
    espace_2.move()

    # ---Flappy Bird---
    flappy.affichage()
    flappy.gravite(5)

    # ---Sol---
    sol.affichage()

    # ---Actions---
    # Sauter (spacebar)


    if pygame.key.get_pressed() [K_SPACE]:

        flappy.saut(20)



    # Collision
    if flappy.forme.colliderect(sol.O_forme):
        print("collision sol")


    elif flappy.forme.colliderect(tuyau_1.O_forme):
        print("collision tuyau 1")

    elif flappy.forme.colliderect(tuyau_2.O_forme):
        print("collision tuyau 2")


if __name__ == '__main__':

    core.main(setup, run)
