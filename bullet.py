import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired"""
    def __init__(self, ai_game):
        """create a bullet object at the samurai's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Create a bullet rect at (0,0) then set correct position
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.samurai.rect.midtop

        #Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """move the bullet up the screen"""
        #Update the decimal position
        self.y -= self.settings.bullet_speed
        #Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
