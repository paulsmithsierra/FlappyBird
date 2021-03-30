import pygame
from pygame.math import Vector2
import core
from bird import Bird

if __name__== '__main__':

    flappy = Bird()

    def setup():
        print("Setup START---------")
        core.fps = 30
        core.WINDOW_SIZE = [800, 500]

        #---Setup Flappy---#
        flappy.couleur = "yellow"
        flappy.pos_x = 80
        flappy.pos_y = 250
        flappy.rayon = 20


        print("Setup END-----------")


    def run():
        print("running")


        flappy.affichage(flappy.couleur, flappy.pos_x, flappy.pos_y, flappy.rayon)





    core.main(setup, run)
