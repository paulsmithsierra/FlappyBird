import pygame
import core


class Obstacle:

    def __init__(self):

        self.posX1 = None
        self.posX2 = None
        self.posY1 = None
        self.posY2 = None
        self.couleur = ""
        self.compteur_move_X1 = None

    def affichage(self):

        pygame.draw.rect(core.screen, self.couleur, (self.posX1, self.posY1, self.posX2, self.posY2), 0)
        print("Inside obstacle's affichage() method")


    def move(self):

        #Déplacement
        self.posX1 = self.posX1 - 1
        self.compteur_move_X1 = self.compteur_move_X1 + 1
        print(self.compteur_move_X1)

        #Reset
        if self.compteur_move_X1 == 800:

            self.posX1 = 800
            self.compteur_move_X1 = 0




