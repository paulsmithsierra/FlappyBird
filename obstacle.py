from random import randint
import pygame
import core



class Obstacle:

    def __init__(self):

        self.hitbox = None
        self.pos_x1 = None
        self.pos_x2 = None
        self.pos_y1 = None
        self.pos_y2 = None
        self.couleur = ""


    # Init après collision
    def reset(self, posX1, posY1, posX2, posY2):
        self.pos_x1 = posX1
        self.pos_y1 = posY1
        self.pos_x2 = posX2
        self.pos_y2 = posY2


    # Affichage
    def affichage(self):

        self.hitbox = pygame.draw.rect(core.screen, self.couleur, (self.pos_x1, self.pos_y1, self.pos_x2, self.pos_y2), 0)


    # Deplacement
    def move(self, partieHaute):

        # Déplacement
        self.pos_x1 -= 4

        # Tuyau hors écran
        if self.pos_x1 == 0:

            # RAZ pos X
            self.pos_x1 = 800

            # Nouvelle hauteur aléatoire tuyau HAUT
            if partieHaute == "H":

                self.pos_y2 = randint(0, 200)

            elif partieHaute == "B":
                self.pos_y2 += 150





