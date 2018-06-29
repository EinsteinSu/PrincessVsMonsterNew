import pygame
from game_helper import GameHelper
from game_stats import GameStats
from settings import Settings
from princess import Princess
from pygame.sprite import Group

from stats_board import StatsBoard


def run_game():
    pygame.init()

    settings = Settings()
    pygame.display.set_caption("Pincess VS Monster")
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    princess = Princess(settings, screen)
    magics = Group()
    monsters = Group()
    stats = GameStats(settings)
    statsBoard = StatsBoard(settings, screen, stats)
    game_helper = GameHelper(settings, screen, stats, princess, monsters, magics, None, statsBoard)
    game_helper.create_fleet()
    while True:
        game_helper.check_events()
        princess.update()
        magics.update()
        game_helper.update_magic()
        game_helper.update_monster()
        game_helper.update_screen()


run_game()
