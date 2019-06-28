import pygame
import image

class Ship:
    def __init__(self, ai_settings, screen):  # screen is where to draw the ship
        # Initilize Ship and its Position
        self.screen = screen
        self.ai_settings = ai_settings
        # load ship img
        self.img = pygame.image.load('battelship.png')
        self.rect = self.img.get_rect()  # treating game elements as rectangle, its simple to know , Geometry shape
        self.screen_rect = screen.get_rect()

        # Start new ship at bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Store Decimal value for ship center
        self.center = float(self.rect.centerx)

        # Movement Flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # Update Ship position on basisc on flag
        # Update ship center value not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx += 1
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            # self.rect.centerx -= 1
            self.center -= self.ai_settings.ship_speed_factor
        # Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        # drawing ship on its currnt location
        self.screen.blit(self.img, self.rect)
