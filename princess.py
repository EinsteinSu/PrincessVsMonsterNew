import pygame
from pygame.sprite import Sprite


class Princess(Sprite):

    def __init__(self, settings, screen):
        super(Princess, self).__init__()
        self.settings = settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load(settings.princess_image_path)
        self.rect = self.image.get_rect()

        self.rect.centerx = self.screen_rect.centerx;
        self.rect.centery = self.screen_rect.centery;
        self.rect.left = self.screen_rect.left;

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

        self.center = float(self.rect.centerx)
        self.vertical = float(self.rect.centery)

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.vertical -= self.settings.princess_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.vertical += self.settings.princess_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.princess_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.princess_speed_factor
        self.rect.centery = self.vertical
        self.rect.centerx = self.center

    def blit(self):
        self.screen.blit(self.image, self.rect)

    def reset_position(self):
        self.vertical = self.screen_rect.centery
        self.rect.left = self.screen_rect.left
