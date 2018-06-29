import pygame
from pygame.sprite import Sprite


class Monster(Sprite):

    def __init__(self, settings, screen):
        super(Monster, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(settings.monster_image_path)
        self.rect = self.image.get_rect()
        self.settings = settings
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blit(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += (self.settings.monster_speed_factor * self.settings.monster_fleet_direction)
        self.rect.y = self.y


    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True
        if self.rect.top <= 0:
            return True
