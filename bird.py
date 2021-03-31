import pygame
import core
from obstacle import Obstacle


class Bird:

    def __init__(self):
        self.couleur = ""
        self.rayon = None
        self.pos_x = None
        self.pos_y = None
        self.gravite = None
        self.vitesse_montee = None
        self.vitesse_descente = None
        self.tuyau = Obstacle()

    def affichage(self):

        pygame.draw.circle(core.screen, self.couleur, [self.pos_x, self.pos_y], self.rayon)

    def saut(self):

            self.pos_y = self.pos_y - 10


    def collision(self):
        pass
