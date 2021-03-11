import pygame

import os
vector = pygame.math.Vector2




class Settings:
    """Settings for Ninja game"""
    def __init__(self):
        # screen settings
        self.screen_width = 1280
        self.screen_height = 720
        # Background settings
        self.background_image = pygame.image.load('/Users/sethalexander/Dropbox/vs_code/python/projects/ninja/images/mountain/forest.png')
        self.background_image = pygame.transform.scale(self.background_image, (1280,720))
        self.background_color = (255,0,0)
        self.title = "Ninja" 
        # FPS settings
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.clock.tick(self.fps) 
        # Game Physics
        self.gravity = 0.5
        self.player_position = vector(640, 360)
        self.player_velocity = vector(0,0)
        self.player_accelleration =vector(0,0)
        self.player_acceleration_speed = 0.1
        # Friction settings
        self.player_friction = -0.12
        # Asteroid Settings
        self.asteroid_speed = 1
        # Colors
        self.black = (0,0,0)
        self.red = (255,0,0)
        
        

