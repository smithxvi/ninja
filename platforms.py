
import pygame
from settings import Settings
from pygame.sprite import Sprite
vector = pygame.math.Vector2


class Platform(Sprite):
    """A class to manage platforms"""
    def __init__(self, x, y, width, height):
        super().__init__()
        self.settings = Settings()
        self.image = pygame.Surface((width,height))
        self.image.fill(self.settings.red)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


