class Settings():
    # Storing All Settings For Game

    def __init__(self):
        # Initilize Game Settings

        # 1 Screen Settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bgColor = (230, 230, 230)


        # 2 Bullet Settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # 3 Alien Settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet direction 1 shows right and -1 shows left
        self.fleet_direction = 1

        # 4 Ship Settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

