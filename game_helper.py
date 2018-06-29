import sys

import pygame

from magic import Magic
from monster import Monster


class GameHelper():

    def __init__(self, settings, screen, stats, princess, monsters, magics, button, board):
        self.settings = settings
        self.screen = screen
        self.stats = stats
        self.princess = princess
        self.monsters = monsters
        self.magics = magics
        self.button = button
        self.board = board

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYUP:
                self.check_keyup(event)
            elif event.type == pygame.KEYDOWN:
                self.check_keydown(event)

    def check_keyup(self, event):
        if event.key == pygame.K_UP:
            self.princess.moving_up = False
        if event.key == pygame.K_DOWN:
            self.princess.moving_down = False
        if event.key == pygame.K_LEFT:
            self.princess.moving_left = False
        if event.key == pygame.K_RIGHT:
            self.princess.moving_right = False

    def check_keydown(self, event):
        if event.key == pygame.K_UP:
            self.princess.moving_up = True
        if event.key == pygame.K_DOWN:
            self.princess.moving_down = True
        if event.key == pygame.K_LEFT:
            self.princess.moving_left = True
        if event.key == pygame.K_RIGHT:
            self.princess.moving_right = True
        elif event.key == pygame.K_SPACE:
            self.use_magic()

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.princess.blit()
        for magic in self.magics.sprites():
            magic.blit()
        self.board.show_score()
        self.monsters.draw(self.screen)
        pygame.display.flip()

    def use_magic(self):
        if len(self.magics) < self.settings.magic_allowed:
            new_magic = Magic(self.settings, self.screen, self.princess)
            self.magics.add(new_magic)

    def update_magic(self):
        self.magics.update()
        for magic in self.magics.copy():
            if magic.rect.right >= self.settings.screen_width:
                self.magics.remove(magic)
        self.check_magic_monster_collisions()

    def update_monster(self):
        self.check_monster_fleet_edges()
        self.monsters.update()
        if pygame.sprite.spritecollideany(self.princess, self.monsters):
            print('game over!')

    def create_fleet(self):
        monster = Monster(self.settings, self.screen)
        number_monster_y = self.get_number_monsters_y(monster.rect.height)
        number_cols = self.get_number_cols(monster.rect.width)
        for col in range(number_cols):
            for row in range(number_monster_y):
                self.create_monster(col, row)

    def create_monster(self, col_number, row_number):
        monster = Monster(self.settings, self.screen)
        monster_height = monster.rect.height
        monster.y = monster_height + 2 * monster_height * row_number
        monster_width = monster.rect.width
        monster.rect.x = self.settings.screen_width - 2 * monster_width * col_number
        print("monster x: " + str(monster.rect.x))
        monster.rect.y = monster.y
        print("monster y: " + str(monster.rect.y))
        self.monsters.add(monster)

    def get_number_cols(self, monster_width):
        avaliable_space_x = (
                                    self.settings.screen_width - self.princess.rect.width) - 3 * monster_width - self.settings.distance
        number_cols = int(avaliable_space_x / (2 * monster_width))
        return number_cols

    def get_number_monsters_y(self, monster_height):
        avaliable_space_y = self.settings.screen_height - 2 * monster_height
        number_monsters_y = int(avaliable_space_y / (2 * monster_height))
        return number_monsters_y

    def check_monster_fleet_edges(self):
        for monster in self.monsters.sprites():
            if monster.check_edges():
                self.change_monster_fleet_direction()
                break

    def change_monster_fleet_direction(self):
        for monster in self.monsters.sprites():
            monster.rect.x -= self.settings.monster_fleet_moving_speed
        self.settings.monster_fleet_direction *= -1

    def check_magic_monster_collisions(self):
        collisions = pygame.sprite.groupcollide(self.magics, self.monsters, True, True)
        if collisions:
            for monster in collisions.values():
                self.stats.score += self.settings.monster_points * len(monster)
                self.board.prep_score()
            self.check_high_score()
        if len(self.monsters) == 0:
            self.stats.level += 1
            self.board.prep_level()
            self.magics.empty()
            self.create_fleet()
            # todo: calculate score, create monsters

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.board.prep_high_score()
