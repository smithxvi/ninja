import pygame
from pygame.sprite import Sprite
from settings import Settings
vector = pygame.math.Vector2


class Player(Sprite):
    """A class to manage the player and player attributes"""
    def __init__(self):
        super().__init__()
        self.settings = Settings()
        self.screen = self.settings.background_image.get_rect()
        # self.image = pygame.surface((50,100))
        self.image = pygame.image.load('/Users/sethalexander/Dropbox/vs_code/python/projects/ninja/images/character/idle__000.png')
        self.image = pygame.transform.scale(self.image,(50,100))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen.midbottom
        self.position = self.settings.player_position
        self.velocity = self.settings.player_velocity
        self.acceleration = self.settings.player_accelleration
        self.friction = self.settings.player_friction
        self.gravity = self.settings.gravity
        
   
        
    def update(self):
        """Update the player"""
        # Acceleration
        self.acceleration = vector(0,self.gravity)
        # Pressed Keys
        keys = pygame.key.get_pressed()
        
        if self.rect.right < (self.screen.right -60):
            if keys[pygame.K_RIGHT]:
                self.acceleration.x += self.settings.player_acceleration_speed
        if self.rect.left > (self.screen.left + 60):
            if keys[pygame.K_LEFT]:
                self.acceleration.x -= self.settings.player_acceleration_speed

        self.game_physics()

    

    def game_physics(self):
    # Control acc, vel + friction
        self.acceleration.x += self.velocity.x * self.friction
        self.velocity += self.acceleration 
        self.position += self.velocity + 0.5 * self.acceleration

        self.rect.midbottom = self.position 
        print(self.velocity.y)
        # self.player_y_pos()

    


    def player_y_pos(self):
            
        self.position.y = 0
        self.velocity.y = 720

    
    def jump(self):
        self.velocity.y = -20

        
