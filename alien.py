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
        self.img = pygame.image.load('alien1.png')
        self.rect = self.img.get_rect()

        # Creating Alin at top
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store Position of alien
        self.x = float(self.rect.x)

    def blitme(self):
        #  Draw Alien
        self.screen.blit(self.img, self.rect)


