class Settings():
    # Storing All Settings For Game

    def __init__(self):
        # Initilize Game Settings

        # 1 Screen Settings
        self.screenWidth = 1000
        self.screenHeight = 600
        self.bgColor = (230, 230, 230)
        self.ship_speed_factor = 1.5

        # 2 Bullet Settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

