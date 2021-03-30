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

    def affichage(self, couleur, pos_x, pos_y, rayon):
        pygame.draw.circle(core.screen, couleur, [pos_x, pos_y], rayon)

    def saut(self, pos_y):
        core.getkeyPressValue()
        if core.keyPressValue == " ":
            pos_y + 50


    def collision(self):
        pass
