import pygame
import core
from obstacle import Obstacle


class Bird:

    def __init__(self):

        self.forme = None
        self.couleur = ""
        self.rayon = None
        self.pos_x = None
        self.pos_y = None


    # Affichage dans la fenêtre
    def affichage(self):

        self.forme = pygame.draw.circle(core.screen, self.couleur, [self.pos_x, self.pos_y], self.rayon)


    # Gravité
    def gravite(self, vitesse_tombee):

        self.pos_y = self.pos_y + vitesse_tombee


    # Saut
    def saut(self, vitesse_montee):

        self.gravite(0)

        if (self.pos_y - vitesse_montee) < 0:
            self.pos_y = 0


        else:
            for i in range(0, vitesse_montee):
                self.pos_y = self.pos_y - 1

        self.gravite(1)



    def collision(self):

        pass
