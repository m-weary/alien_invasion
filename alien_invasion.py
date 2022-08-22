from curses import KEY_DOWN
import sys
import pygame
from settings import Settings
from samurai import Samurai

class AlienInvasion:
    """A general class to manage game assets and behaviour"""

    def __init__(self):
        """Initialize game and create game resources"""
        pygame.init()
        self.settings = Settings()
        #Set the screen size 
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        # Set the banner
        pygame.display.set_caption("Alien Invasion")
        self.samurai = Samurai(self)
    
    def run_game(self):
        """Begin the main loop"""
        while True:
            #Watch for keyboard and mouse events
            self._check_events()
            self.samurai.update()
            self._update_screen()
                    
    def _check_events(self):
        """Respond to keypress and mouse events"""
        for event in pygame.event.get():
            #Add an event to quit
            if event.type == pygame.QUIT:
                    sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)    
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
            
    def _check_keydown_events(self,event):
        """Responds to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.samurai.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.samurai.moving_left = True  
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self,event):
        """Responds to key releases""" 
        if event.key == pygame.K_RIGHT:
            self.samurai.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.samurai.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        #Redraw the screen suring each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.samurai.blitme()
        #Make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    #Make game instance and run the game
    ai = AlienInvasion()
    ai.run_game()