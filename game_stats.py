class GameStats:
    # Tract Game Stats
    def __init__(self, ai_settings):
        # Initilize Stats
        self.ai_settings = ai_settings
        self.reset_stats()

        # start aliens in active state
        self.game_active = True

    def reset_stats(self):
        # Changing stats
        self.ships_left = self.ai_settings.ship_limit
