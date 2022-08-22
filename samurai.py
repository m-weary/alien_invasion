import pygame

class Samurai:
    """A class to manage the samurai"""
    def __init__(self, ai_game):
        """"Initialize the samurai and set it's starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect() 
        #Load the image and get its rect
        self.image = pygame.image.load('images/samurai_idle.bmp')
        self.image = pygame.transform.smoothscale(self.image, (100,100))
        self.rect = self.image.get_rect()
        #Add settings
        self.settings = ai_game.settings
        #Start each new character at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        #Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)
        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the samurai's position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.samurai_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.samurai_speed
        #Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image, self.rect)

