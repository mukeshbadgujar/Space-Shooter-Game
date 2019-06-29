import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    # Aliens
    def __init__(self, ai_settings, screen):
        # creating alien and postion
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load img and rect
        self.image = pygame.image.load('alien1.png')  # AAthe Img taka te error yes kab??
        self.rect = self.image.get_rect()

        # Creating Alien at top
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store Position of alien
        self.x = float(self.rect.x)




