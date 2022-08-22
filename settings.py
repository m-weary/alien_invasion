class Settings:
    """A class to store all the settings for the game, Alien Invasion"""

    def __init__(self):
        """Initialize the settings"""
        #Screen settings
        self.screen_width = 1600
        self.screen_height = 1000
        self.bg_color = (194, 211, 213)
        self.samurai_speed = 4

        #Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)


