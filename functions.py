import pygame


def text_to_screen(screen, text, x, y, size=None, color=(None, None, None), font_type=""):
    try:

        text = str(text)
        font = pygame.font.SysFont(font_type, size)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))

    except Exception as e:
        print('Font Error, saw it coming')
        raise e