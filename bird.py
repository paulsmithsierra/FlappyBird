import pygame
import core


class Bird:

    def __init__(self):

        self.hitbox = None
        self.couleur = ""
        self.rayon = None
        self.pos_x = None
        self.pos_y = None


    # Init après collision
    def reset(self, posX, posY):
        self.pos_x = posX
        self.pos_y = posY


    # Affichage dans la fenêtre
    def affichage(self):

        self.hitbox = pygame.draw.circle(core.screen, self.couleur, [self.pos_x, self.pos_y], self.rayon)


    # Gravité
    def gravite(self, vitesse_tombee):

        self.pos_y += vitesse_tombee


    # Saut
    def saut(self, vitesse_montee):

        montee_done = None

        self.gravite(0)

        if (self.pos_y - vitesse_montee) < 0:
            self.pos_y = 0


        else:
            for i in range(0, vitesse_montee):
                self.pos_y -= 1

                if i == vitesse_montee:
                    montee_done = 1

            if montee_done == 1:
                for j in range(0, vitesse_montee):
                    self.pos_y += 1

                montee_done = 0


