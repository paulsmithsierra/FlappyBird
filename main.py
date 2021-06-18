# This is a recreation of the famous game "Flappy Bird"
# Made by:
# Quentin DÉMURGÉ (email: ) and Paul SMITH (email: paulsierra817@gmail.com)
# IUT Lyon 1 - LP RAVI

import sys
from random import randint
import pygame
import pygame.freetype
import core
from bird import Bird
from obstacle import Obstacle


# ---VARIABLES GLOBALES---
# Flappy Bird
flappy = Bird()
flappyImage = None

# Tuyaux
tuyau_1H = Obstacle()
tuyau_1B = Obstacle()
tuyau_2H = Obstacle()
tuyau_2B = Obstacle()

# Sol
sol = Obstacle()

# Score
score = None
lastScore = None
affichageScore = ""
maxScore = None
affichageMaxScore = ""
previousScore = None

# Partie
play = None

# Autres
menuFont = None
scoreFont = None
document = None
content = None



# INITIALISATION
def setup():
    global play, score, affichageScore, lastScore, maxScore, affichageMaxScore, previousScore, menuFont, \
        scoreFont, document, content, monTableau


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
    sol.couleur = "beige"
    sol.reset(0, 400, 800, 100)


    # ---Setup Score---
    score = 0
    affichageScore = "0"
    lastScore = "0"
    previousScore = 0

    # Récuperation du Max Score depuis fichier texte
    document = open('maxScore.txt', 'r')
    content = document.read()
    monTableau = [int(i) for i in content.split('\n')] # transformation en int
    maxScore = monTableau[0]
    affichageMaxScore = str(maxScore) # transformation en string pour affichage


    # ---Setup Partie---
    play = False


    # ---Setup Autres---
    menuFont = pygame.freetype.SysFont("Sans-serif", 40, True, False)
    scoreFont = pygame.freetype.SysFont("Sans-serif", 20, True, False)


    print("Setup END-----------")



# GAME LOOP
def run():
    global score, affichageScore, lastScore, maxScore, affichageMaxScore, previousScore, play, menuFont, scoreFont


    # ---MENU---
    if not play:

        # Affichage Menu Principal
        menuFont.render_to(core.screen, (200, 200), "Press ENTER to play", (255, 255, 255))
        scoreFont.render_to(core.screen, (200, 260), "(Use SPACEBAR to fly) ", ("yellow"))
        scoreFont.render_to(core.screen, (550, 415), "Last score: " + lastScore, (255, 255, 255))
        scoreFont.render_to(core.screen, (550, 450), "Max score: " + affichageMaxScore, ("dark green"))


        # Max Score
        if maxScore < previousScore:

            affichageMaxScore = str(previousScore)
            maxScore = previousScore

            # Écriture du nouveau Max Score
            document = open('maxScore.txt', 'w')
            document.write(affichageMaxScore)
            previousScore = 0



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
        scoreFont.render_to(core.screen, (550, 450), "Score: " + affichageScore, (0, 0, 0))

        # Points
        if tuyau_1H.pos_x1 == (flappy.pos_x - 2*flappy.rayon):
            score += 1
            affichageScore = str(score)

        if tuyau_2H.pos_x1 == (flappy.pos_x - 2*flappy.rayon):
            score += 1
            affichageScore = str(score)



        # ---COLLISIONS---
        # Collision sol
        if flappy.hitbox.colliderect(sol.hitbox):
            play = False
            lastScore = affichageScore
            previousScore = score
            score = 0
            affichageScore = "0"
            flappy.reset(80, 150)
            tuyau_1H.reset(800, 0, 50, randint(0, 200))
            tuyau_1B.reset(800, tuyau_1H.pos_y2 + 150, 50, 500)
            tuyau_2H.reset(1200, 0, 50, randint(0, 200))
            tuyau_2B.reset(1200, tuyau_2H.pos_y2 + 150, 50, 500)

        # Collision Tuyau 1H
        elif flappy.hitbox.colliderect(tuyau_1H.hitbox):
            play = False
            lastScore = affichageScore
            previousScore = score
            score = 0
            affichageScore = "0"
            flappy.reset(80, 150)
            tuyau_1H.reset(800, 0, 50, randint(0, 200))
            tuyau_1B.reset(800, tuyau_1H.pos_y2 + 150, 50, 500)
            tuyau_2H.reset(1200, 0, 50, randint(0, 200))
            tuyau_2B.reset(1200, tuyau_2H.pos_y2 + 150, 50, 500)

        # Collision Tuyau 1B
        elif flappy.hitbox.colliderect(tuyau_1B.hitbox):
            play = False
            lastScore = affichageScore
            previousScore = score
            score = 0
            affichageScore = "0"
            flappy.reset(80, 150)
            tuyau_1H.reset(800, 0, 50, randint(0, 200))
            tuyau_1B.reset(800, tuyau_1H.pos_y2 + 150, 50, 500)
            tuyau_2H.reset(1200, 0, 50, randint(0, 200))
            tuyau_2B.reset(1200, tuyau_2H.pos_y2 + 150, 50, 500)

        # Collision Tuyau 2H
        elif flappy.hitbox.colliderect(tuyau_2H.hitbox):
            play = False
            lastScore = affichageScore
            previousScore = score
            score = 0
            affichageScore = "0"
            flappy.reset(80, 150)
            tuyau_1H.reset(800, 0, 50, randint(0, 200))
            tuyau_1B.reset(800, tuyau_1H.pos_y2 + 150, 50, 500)
            tuyau_2H.reset(1200, 0, 50, randint(0, 200))
            tuyau_2B.reset(1200, tuyau_2H.pos_y2 + 150, 50, 500)

        # Collision Tuyau 2B
        elif flappy.hitbox.colliderect(tuyau_2B.hitbox):
            play = False
            lastScore = affichageScore
            previousScore = score
            score = 0
            affichageScore = "0"
            flappy.reset(80, 150)
            tuyau_1H.reset(800, 0, 50, randint(0, 200))
            tuyau_1B.reset(800, tuyau_1H.pos_y2 + 150, 50, 500)
            tuyau_2H.reset(1200, 0, 50, randint(0, 200))
            tuyau_2B.reset(1200, tuyau_2H.pos_y2 + 150, 50, 500)



if __name__ == '__main__':

    core.main(setup, run)
