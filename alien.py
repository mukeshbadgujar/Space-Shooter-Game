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

    def check_edges(self):
        # return true if alien is at the edge of screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        # Move Alien to Right or left
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x






