from os import name
import sys
import pygame

from settings import Settings
from samurai import Samurai
from bullet import Bullet
from enemy import Enemy

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
        self.bullets = pygame.sprite.Group()
        self.enemy = pygame.sprite.Group()
        self._create_fleet()
    
    def run_game(self):
        """Begin the main loop"""
        while True:
            #Watch for keyboard and mouse events
            self._check_events()
            self.samurai.update()
            self._update_bullets()
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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet() 
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self,event):
        """Responds to key releases""" 
        if event.key == pygame.K_RIGHT:
            self.samurai.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.samurai.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        self.bullets.update()
        #Get rid of bullets once they are out of screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """Create the fleet of enemies"""
        #Make an enemy
        enemy = Enemy(self)
        #Calculate how many can fit on the screen
        enemy_width, enemy_height = enemy.rect.size
        available_space_x = self.settings.screen_width - (2 * enemy_width)
        number_enemies_x = available_space_x // (2 * enemy_width)
        #Determine the number of rows of enemies that fit on the screen
        samurai_height = self.samurai.rect.height
        available_space_y = (self.settings.screen_height - (2 * enemy_height) - samurai_height)
        number_rows = available_space_y // (2 * enemy_height)
        #Create full fleet
        for row_number in range(number_rows):
            for enemy_number in range(number_enemies_x):
                self._create_enemy(enemy_number, row_number)

    def _create_enemy(self, enemy_number, row_number):
        #Create an enemy and place it in the row
        enemy = Enemy(self)
        enemy_width, enemy_height = enemy.rect.size
        enemy.x = enemy_width + 2 * enemy_width * enemy_number
        enemy.rect.x = enemy.x
        enemy.rect.y = enemy.rect.height + 2 * enemy.rect.height * row_number
        self.enemy.add(enemy)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        #Redraw the screen suring each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.samurai.blitme()
        #Add the bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        #Add the enemy
        self.enemy.draw(self.screen)
        #Make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    #Make game instance and run the game
    ai = AlienInvasion()
    ai.run_game()