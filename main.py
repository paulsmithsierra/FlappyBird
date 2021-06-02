# This is a recreation of the famous game "Flappy Bird"
# Made by:
# Quentin DEMURGE (email: ) and Paul SMITH (email: paulsierra817@gmail.com)
# IUT Lyon 1 - LP RAVI

import sys
from random import randint
import pygame
import pygame.freetype
import core
import functions
from bird import Bird
from obstacle import Obstacle


# ---VARIABLES GLOBALES---
# Flappy Bird
flappy = Bird()

# Tuyaux
tuyau_1H = Obstacle()
tuyau_1B = Obstacle()
tuyau_2H = Obstacle()
tuyau_2B = Obstacle()

# Sol
sol = Obstacle()

# Score
score = None
finalScore = None

# Partie
play = None

# Autres
font = None


# INITIALISATION
def setup():
    global play, font, score, finalScore

    print("Setup START---------")

    # ---Fenêtre---
    core.fps = 60
    core.WINDOW_SIZE = [800, 500]


    # ---Setup Flappy---
    flappy.couleur = "yellow"
    flappy.pos_x = 80
    flappy.pos_y = 150
    flappy.rayon = 20


    # ---Setup Obstacles---
    # Tuyau 1
    ## Haut
    tuyau_1H.couleur = "dark green"
    tuyau_1H.posX1 = 800
    tuyau_1H.posY1 = 0
    tuyau_1H.posX2 = 50
    tuyau_1H.posY2 = randint(0, 200)

    ## Bas
    tuyau_1B.couleur = "dark green"
    tuyau_1B.posX1 = 800
    tuyau_1B.posY1 = tuyau_1H.posY2 + 150
    tuyau_1B.posX2 = 50
    tuyau_1B.posY2 = 500


    # Tuyau 2
    ## Haut
    tuyau_2H.couleur = "dark green"
    tuyau_2H.posX1 = 1200
    tuyau_2H.posY1 = 0
    tuyau_2H.posX2 = 50
    tuyau_2H.posY2 = randint(0, 200)

    ## Bas
    tuyau_2B.couleur = "dark green"
    tuyau_2B.posX1 = 1200
    tuyau_2B.posY1 = tuyau_2H.posY2 + 150
    tuyau_2B.posX2 = 50
    tuyau_2B.posY2 = 500


    # ---Setup Sol---
    sol.couleur = "brown"
    sol.posX1 = 0
    sol.posY1 = 400
    sol.posX2 = 800
    sol.posY2 = 100


    # ---Setup Score---
    score = 0
    finalScore = 0


    # ---Setup Partie---
    play = False

    # ---Setup Autres---
    font = pygame.freetype.SysFont("Sans-serif", 50, True, False)



    print("Setup END-----------")


# GAME LOOP
def run():
    global score, finalScore, play

    # Affichage Menu Principal
    functions.text_to_screen(core.screen, 'Press ENTER to play', 200, 250, 30, (255, 255, 255), "Sans-serif")


    # ---User Actions---
    for event in pygame.event.get():  # User did something

        # Fermer la fenêtre (croix rouge)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        # Appui touche clavier
        if event.type == pygame.KEYDOWN:
            # Débuter une partie
            if event.key == pygame.K_RETURN:
                play = True

            # Sauter
            if event.key == pygame.K_SPACE:
                flappy.saut(60)



    # Affichage flappy, obstacles et paysage pour partie
    if play:

        # ---Tuyaux---
        # Haut 1
        tuyau_1H.affichage()
        tuyau_1H.move("H")

        # Bas 1
        tuyau_1B.affichage()
        tuyau_1B.move("B")
        tuyau_1B.posY1 = tuyau_1H.posY2 + 150

        # Haut 2
        tuyau_2H.affichage()
        tuyau_2H.move("H")

        # Bas 2
        tuyau_2B.affichage()
        tuyau_2B.move("B")
        tuyau_2B.posY1 = tuyau_2H.posY2 + 150


        # ---Flappy Bird---
        flappy.affichage()
        flappy.gravite(3)


        # ---Sol---
        sol.affichage()


        # ---Score---
        # Affichage
        functions.text_to_screen(core.screen, 'Score: {0}'.format(score), 600, 450, 30, (255, 255, 255), "Sans-serif")

        # Faire des points
        if tuyau_1H.posX1 == (flappy.pos_x - flappy.rayon):
            score = score + 1
            print(score)

        if tuyau_2H.posX1 == (flappy.pos_x - flappy.rayon):
            score = score + 1
            print(score)


        # Collision sol
        if flappy.forme.colliderect(sol.forme):
            print("collision sol")
            finalScore = score
            score = 0
            play = False

        # Collision Tuyau 1H
        elif flappy.forme.colliderect(tuyau_1H.forme):
            print("collision tuyau 1")
            finalScore = score
            score = 0
            play = False

        # Collision Tuyau 1B
        elif flappy.forme.colliderect(tuyau_1B.forme):
            print("collision tuyau 1")
            finalScore = score
            score = 0
            play = False

        # Collision Tuyau 2H
        elif flappy.forme.colliderect(tuyau_2H.forme):
            print("collision tuyau 2")
            finalScore = score
            score = 0
            play = False

        # Collision Tuyau 2B
        elif flappy.forme.colliderect(tuyau_2B.forme):
            print("collision tuyau 2")
            finalScore = score
            score = 0
            play = False




if __name__ == '__main__':

    core.main(setup, run)
