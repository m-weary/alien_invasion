import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    """"A class to represent an enemy in the horde"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        #Load the image and set its rect attritbute
        self.image = pygame.image.load('images/dead_samurai.png')
        self.image = pygame.transform.smoothscale(self.image, (80,80))
        self.rect = self.image.get_rect()
        #Start each new enemy at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #Store the enemy's exact horizontal position
        self.x = float(self.rect.x)
    
