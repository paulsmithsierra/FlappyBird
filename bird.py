import pygame
import core
from obstacle import Obstacle


class Bird:

    def __init__(self):
        self.couleur = ""
        self.rayon = None
        self.pos_x = None
        self.pos_y = None
        self.tuyau = Obstacle()

    # Affichage dans la fenêtre
    def affichage(self):

        pygame.draw.circle(core.screen, self.couleur, [self.pos_x, self.pos_y], self.rayon)

    # Gravité
    def gravite(self):

        self.pos_y = self.pos_y + 5

    # Saut
    def saut(self):

            self.pos_y = self.pos_y - 20


    def collision(self):
        pass
