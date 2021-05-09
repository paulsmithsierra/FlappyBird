import pygame
import core
from main import tuyau_1


class Espace:

    def __init__(self):

        self.E_posX1 = tuyau_1.O_posX1
        self.E_posX2 = tuyau_1.O_posX2
        self.E_posY1 = None
        self.E_posY2 = None
        self.E_couleur = "black"


    #def move(self):

        # Déplacement
        #self.E_posX1 = tuyau_1.O_posX1
        #self.E_posX2 = tuyau_1.O_posX2

    def affichage(self):

        pygame.draw.rect(core.screen, self.E_couleur, (self.E_posX1, self.E_posY1, self.E_posX2, self.E_posY2), 0)

    def posY_random(self):

        pass

