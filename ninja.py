import pygame
import sys
from settings import Settings
from hero import Hero
from asteroid import Asteroid
from player import Player
from platforms import Platform



class Ninja:
    """Overall calss to manage game assets and behavior"""
    def __init__(self):
       """Initialize the game, and create game resources"""
       pygame.init()
       self.settings = Settings()
       self.clock = self.settings.clock
       self.screen = pygame.display.set_mode((self.settings.screen_width, 
       self.settings.screen_height))
       self.title = pygame.display.set_caption(self.settings.title)
       self.all_sprites = pygame.sprite.Group()
       self.platforms = pygame.sprite.Group()
       self._add_sprites()
       self.player = Player()
       


    def run_game(self):
        """Start the main loop for the game"""
        self.playing = True # delete this later
        while self.playing: # delete while self.playing:
            self.settings.clock
            self._check_events()
            self.update_sprites()
            self.update_screen()
            

         
            
    def _check_events(self):  
        """Check for user keyboard and mouse events"""

        # Quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN 
            and event.key == pygame.K_ESCAPE): 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()

    def update_sprites(self):
            """Run update method for all sprites"""
            self.all_sprites.update() 
            
            hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.position.y = hits[0].rect.top
         
    def update_screen(self):
        """Draw game's background and all sprites"""
        # Draw background
        self.screen.blit(self.settings.background_image, (0,0))
        # Draw sprites 
        self.all_sprites.draw(self.screen)

        # *AFTER* drawing everything, flip the display.
        pygame.display.flip()

    def _add_sprites(self):
        player = Player()
        self.all_sprites.add(player)
        p1 = Platform(0,self.settings.screen_height -40, self.settings.screen_width, 40)
        self.all_sprites.add(p1)
        self.platforms.add(p1)
        # asteroid = Asteroid()
        # self.all_sprites.add(asteroid)
        

    def _update_asteroids(self):
        """Control astroid movement"""
        self._update_asteroids()




    

if __name__ == '__main__':
    # Make instance, and run the game
    ninja = Ninja()
    ninja.run_game()