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
affichageScore = ""

# Partie
play = None

# Autres
toto = None
MenuFont = None
ScoreFont = None
text_surface = None


# INITIALISATION
def setup():
    global play, score, affichageScore, finalScore, MenuFont, ScoreFont

    print("Setup START---------")

    # ---Fenêtre---
    core.fps = 70
    core.WINDOW_SIZE = [800, 500]


    # ---Setup Flappy---
    flappy.couleur = "yellow"
    flappy.rayon = 20
    flappy.reset(80, 150)


    # ---Setup Obstacles---
    # Tuyau 1
    ## Haut
    tuyau_1H.couleur = "dark green"
    tuyau_1H.reset(800, 0, 50, randint(0, 200))

    ## Bas
    tuyau_1B.couleur = "dark green"
    tuyau_1B.reset(800, tuyau_1H.pos_y2 + 150, 50, 500)

    # Tuyau 2
    ## Haut
    tuyau_2H.couleur = "dark green"
    tuyau_2H.reset(1200, 0, 50, randint(0, 200))

    ## Bas
    tuyau_2B.couleur = "dark green"
    tuyau_2B.reset(1200, tuyau_2H.pos_y2 + 150, 50, 500)


    # ---Setup Sol---
    sol.couleur = "brown"
    sol.reset(0, 400, 800, 100)


    # ---Setup Score---
    score = 0
    finalScore = 0
    affichageScore = ""


    # ---Setup Partie---
    play = False


    # ---Setup Autres---
    MenuFont = pygame.freetype.SysFont("Sans-serif", 30, True, False)
    ScoreFont = pygame.freetype.SysFont("Sans-serif", 20, True, False)

    print("Setup END-----------")


# GAME LOOP
def run():
    global score, affichageScore, finalScore, play, MenuFont, ScoreFont, toto

    # ---MENU---
    if not play:
        # Affichage Menu Principal
        MenuFont.render_to(core.screen, (225, 250), "Press ENTER to play", (255, 255, 255))


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
                toto = True

            # Sauter
            if event.key == pygame.K_SPACE:
                flappy.saut(60)



    # Gestion pour partie (affichage, mouvement...)
    if play:

        # ---TUYAUX---
        # Ecart
        # N° 1
        tuyau_1B.pos_y1 = tuyau_1H.pos_y2 + 150
        # N° 2
        tuyau_2B.pos_y1 = tuyau_2H.pos_y2 + 150

        # Affichage
        # N° 1
        tuyau_1H.affichage()
        tuyau_1B.affichage()
        # N° 2
        tuyau_2H.affichage()
        tuyau_2B.affichage()

        # Deplacement
        # N° 1
        tuyau_1H.move("H")
        tuyau_1B.move("B")
        # N° 2
        tuyau_2H.move("H")
        tuyau_2B.move("B")


        # ---FLAPPY BIRD---
        flappy.affichage()
        flappy.gravite(2)


        # ---SOL---
        sol.affichage()


        # ---SCORE---
        # Affichage
        ScoreFont.render_to(core.screen, (550, 450), "Score: " + affichageScore, (255, 255, 255))

        # Points
        if tuyau_1H.pos_x1 == (flappy.pos_x - flappy.rayon):
            score = score + 1
            affichageScore = str(score)

        if tuyau_2H.pos_x1 == (flappy.pos_x - flappy.rayon):
            score = score + 1
            affichageScore = str(score)



        # ---COLLISIONS---
        # Collision sol
        if flappy.hitbox.colliderect(sol.hitbox):
            print("collision sol")
            play = False
            finalScore = score
            score = 0
            affichageScore = ""
            flappy.reset(80, 150)
            tuyau_1H.reset(800, 0, 50, randint(0, 200))
            tuyau_1B.reset(800, tuyau_1H.pos_y2 + 150, 50, 500)
            tuyau_2H.reset(1200, 0, 50, randint(0, 200))
            tuyau_2B.reset(1200, tuyau_2H.pos_y2 + 150, 50, 500)

        # Collision Tuyau 1H
        elif flappy.hitbox.colliderect(tuyau_1H.hitbox):
            print("collision tuyau 1")
            play = False
            finalScore = score
            score = 0
            affichageScore = ""
            flappy.reset(80, 150)
            tuyau_1H.reset(800, 0, 50, randint(0, 200))
            tuyau_1B.reset(800, tuyau_1H.pos_y2 + 150, 50, 500)
            tuyau_2H.reset(1200, 0, 50, randint(0, 200))
            tuyau_2B.reset(1200, tuyau_2H.pos_y2 + 150, 50, 500)

        # Collision Tuyau 1B
        elif flappy.hitbox.colliderect(tuyau_1B.hitbox):
            print("collision tuyau 1")
            play = False
            finalScore = score
            score = 0
            affichageScore = ""
            flappy.reset(80, 150)
            tuyau_1H.reset(800, 0, 50, randint(0, 200))
            tuyau_1B.reset(800, tuyau_1H.pos_y2 + 150, 50, 500)
            tuyau_2H.reset(1200, 0, 50, randint(0, 200))
            tuyau_2B.reset(1200, tuyau_2H.pos_y2 + 150, 50, 500)

        # Collision Tuyau 2H
        elif flappy.hitbox.colliderect(tuyau_2H.hitbox):
            print("collision tuyau 2")
            play = False
            finalScore = score
            score = 0
            affichageScore = ""
            flappy.reset(80, 150)
            tuyau_1H.reset(800, 0, 50, randint(0, 200))
            tuyau_1B.reset(800, tuyau_1H.pos_y2 + 150, 50, 500)
            tuyau_2H.reset(1200, 0, 50, randint(0, 200))
            tuyau_2B.reset(1200, tuyau_2H.pos_y2 + 150, 50, 500)

        # Collision Tuyau 2B
        elif flappy.hitbox.colliderect(tuyau_2B.hitbox):
            print("collision tuyau 2")
            play = False
            finalScore = score
            score = 0
            affichageScore = ""
            flappy.reset(80, 150)
            tuyau_1H.reset(800, 0, 50, randint(0, 200))
            tuyau_1B.reset(800, tuyau_1H.pos_y2 + 150, 50, 500)
            tuyau_2H.reset(1200, 0, 50, randint(0, 200))
            tuyau_2B.reset(1200, tuyau_2H.pos_y2 + 150, 50, 500)



if __name__ == '__main__':

    core.main(setup, run)
