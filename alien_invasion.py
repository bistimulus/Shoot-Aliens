#Started on June 19th
import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    '''Class to manage game assets and behavior'''
    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Shoot Aliens")

        self.ship = Ship(self)

        #set the background color
        self.bg_color = (230,230,230)

    def run_game(self):
        '''Here we start the main loop for the game'''
        while True:
            self._check_events()
            self._update_screen()


    def _check_events(self): #helper method ~ will not be called using instance
        '''Respond to keypresses and mouse events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


    def _update_screen(self): #helper method 
        '''Update images on the screen and flip to the new screen'''
        #redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        #Make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    #Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()

