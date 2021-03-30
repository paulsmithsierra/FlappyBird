import inspect
import time
from typing  import cast
from types import FrameType

import pygame

runfuntion = None
setupfunction = None
screen = None
fps = 60
loopLock = False
WINDOW_SIZE = [100, 100]
width = 0
height = 1
mouseclickleft=[-1,-1]
mouseclickL= False
mouseclickright=[-1,-1]
mouseclickR= False
keyPress=False
keyPressValue=None
keyReleaseValue = None


def noLoop():
    global loopLock
    loopLock = True

def getMouseLeftClick():
    if mouseclickL:
        return mouseclickleft
def getMouseRightClick():
    if mouseclickR:
        return mouseclickright
def getkeyPress():
    return keyPress

def getkeyPressValue():
    return keyPressValue

def getkeyRelease():
    return  keyReleaseValue




def setup():
    pygame.init()
    global WINDOW_SIZE
    WINDOW_SIZE
    if (setupfunction is not None):
        setupfunction()


    global screen
    screen = pygame.display.set_mode(WINDOW_SIZE)

    # Set title of screen
    pygame.display.set_caption("Window")


def run():
    if (runfuntion is not None):
        runfuntion()




def main(setupf,runf):
    print(inspect.stack()[1].function)
    global runfuntion
    runfuntion = runf
    global setupfunction
    setupfunction = setupf
    global mouseclickleft, mouseclickL, mouseclickright, mouseclickR,keyPress,keyPressValue, keyReleaseValue

    setup()

    clock = pygame.time.Clock()


    done = False
    print("Run START-----------")
    while not done:
        if not loopLock :
            screen.fill(0)
            run()

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

            elif event.type == pygame.KEYDOWN:
                keyPress = True
                keyPressValue = event.key
            elif event.type == pygame.KEYUP:
                keyPressValue = None

            elif event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:
                        mouseclickL= True
                        mouseclickleft = event.pos
                if event.button == 3:
                    mouseclickR = True
                    mouseclickright = event.pos


            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouseclickL= False
                    mouseclickleft=None
                if event.button == 3:
                    mouseclickR= False
                    mouseclickright=None

            elif event.type == pygame.MOUSEMOTION:
                if mouseclickL:
                    mouseclickleft = event.pos
                if mouseclickR:
                    mouseclickright = event.pos

            if hasattr(event,'key'):
                if keyPressValue:
                    keyReleaseValue = event.key
                else:
                    keyReleaseValue = None


        clock.tick(fps)
        #print(clock.get_time())
        # Go ahead and update the screen with what we 've drawn.
        pygame.display.flip()


