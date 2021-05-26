from random import randint

import pygame
import core


class Obstacle:

    def __init__(self):

        self.forme = None
        self.posX1 = None
        self.posX2 = None
        self.posY1 = None
        self.posY2 = None
        self.couleur = ""



    def affichage(self):

        self.forme = pygame.draw.rect(core.screen, self.couleur, (self.posX1, self.posY1, self.posX2, self.posY2), 0)



    def move(self, partieHaute):

        # Déplacement
        self.posX1 = self.posX1 - 5

        # Tuyau hors écran
        if self.posX1 == 0:

            # RAZ pos X
            self.posX1 = 800

            # Nouvelle hauteur aléatoire tuyau HAUT
            if partieHaute == "H":

                self.posY2 = randint(0, 200)
                print("random height")

            elif partieHaute == "B":
                None





