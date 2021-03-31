#This is a recreation of the famous game "Flappy Bird"
#Made by:
#Quentin DEMURGE (email: ) and Paul SMITH (email: paulsierra817@gmail.com)
#IUT Lyon 1 - LP RAVI

import pygame
from pygame import K_s, K_SPACE
from pygame.math import Vector2
import core
from bird import Bird
from obstacle import Obstacle

#Variables globales
flappy = Bird()
tuyau = Obstacle()
i = None


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [800, 500]

    #---Setup Flappy---#
    flappy.couleur = "yellow"
    flappy.pos_x = 80
    flappy.pos_y = 250
    flappy.rayon = 20

    #---Setup Tuyau---#
    tuyau.couleur = "dark green"
    tuyau.posX1 = 800
    tuyau.posY1 = 0
    tuyau.posX2 = 50
    tuyau.posY2 = 500




    print("Setup END-----------")


def run():
    print("running")

    #Affichage Flappy
    flappy.affichage()

    #Affichage Tuyau
    tuyau.affichage()



    #Saut

    if pygame.key.get_pressed()[K_SPACE]:

        flappy.saut()




if __name__ == '__main__':

    core.main(setup, run)
