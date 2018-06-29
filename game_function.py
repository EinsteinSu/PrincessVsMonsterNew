import pygame


def update_screen(settings, screen, princess):
    screen.fill(settings.bg_color)
    princess.blit()
    pygame.display.flip()
