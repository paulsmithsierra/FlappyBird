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
        self.compteur_moveX1 = None

    def affichage(self):

        self.forme = pygame.draw.rect(core.screen, self.couleur, (self.posX1, self.posY1, self.posX2, self.posY2), 0)


    def move(self):

        # Déplacement
        self.posX1 = self.posX1 - 5
        self.compteur_moveX1 = self.compteur_moveX1 + 5
        print(self.compteur_moveX1)

        # Reset position
        if self.posX1 == 0:
            # Déplacement (pos X)
            self.posX1 = 800
            self.compteur_moveX1 = 0