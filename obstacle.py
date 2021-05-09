import pygame
import core


class Obstacle:

    def __init__(self):

        self.O_posX1 = None
        self.O_posX2 = None
        self.O_posY1 = None
        self.O_posY2 = None
        self.O_couleur = ""
        self.O_compteur_moveX1 = None

    def affichage(self):

        pygame.draw.rect(core.screen, self.O_couleur, (self.O_posX1, self.O_posY1, self.O_posX2, self.O_posY2), 0)


    def move(self):

        #Déplacement
        self.O_posX1 = self.O_posX1 - 5
        self.O_compteur_moveX1 = self.O_compteur_moveX1 + 5
        print(self.O_compteur_moveX1)

        #Reset
        if self.O_posX1 == 0:
            # Déplacement (pos X)
            self.O_posX1 = 800
            self.O_compteur_moveX1 = 0







