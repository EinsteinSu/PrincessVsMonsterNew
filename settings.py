class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 102, 204)

        self.princess_speed_factor = 0.5
        self.princess_image_path = 'images\elsa.png'
        self.princess_limit = 3

        self.magic_speed_factor = 1
        self.magic_allowed = 100
        self.magic_image_path = 'images\snow.png'

        self.monster_speed_factor = 1
        self.monster_image_path = 'images\monster_64.png'
        self.monster_fleet_direction = 1
        self.monster_fleet_moving_speed = 10
        self.monster_points = 100

        self.distance = 1
