import pygame
from pygame.sprite import Sprite


class Magic(Sprite):
    def __init__(self, settings, screen, princess):
        super(Magic, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(settings.magic_image_path)
        self.rect = self.image.get_rect()
        self.rect.centerx = princess.rect.centerx
        self.rect.top = princess.rect.top

        self.x = float(self.rect.x)
        self.speed_factor = settings.magic_speed_factor

    def update(self):
        self.x += self.speed_factor
        self.rect.x = self.x

    def blit(self):
        self.screen.blit(self.image, self.rect)
