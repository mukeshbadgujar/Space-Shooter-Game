import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    # Class For Managing Bullets
    def __init__(self, ai_settings, screen, ship):
        # Creating Bullet Object at Ship Current Position
        super(Bullet, self).__init__()
        # super().__init__()

        self.screen = screen

        # Create Bullet Rect At (0, 0) then Correct The Position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store Bullet Postion as Decimal Value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        # Moving Bullet to Up
        # Updating Decimal position of bullet
        self.y -= self.speed_factor
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        # Drawing Bullet
        pygame.draw.rect(self.screen, self.color, self.rect)