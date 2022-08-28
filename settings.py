class Settings:
    """A class to store all the settings for the game, Alien Invasion"""

    def __init__(self):
        """Initialize the settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (194, 211, 213)
        self.samurai_speed = 3

        #Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 5


