class GameStats():
    def __init__(self, settings):
        self.settings = settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        self.princess_left = self.settings.princess_limit
        self.score = 0
        self.high_score = 0
        self.level = 1
