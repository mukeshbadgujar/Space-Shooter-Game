import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # Initializing Game and Create Screen Object
    pygame.init()
    ai_settings = Settings()
    # Initializing Gaming Window
    screen = pygame.display.set_mode((ai_settings.screenWidth, ai_settings.screenHeight))
    pygame.display.set_caption("Alien Attack")

    # Make a Ship
    ship = Ship(ai_settings, screen)

    # Make group to store bullets
    bullets = Group()


    # Starting Main Loop
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)




run_game()
