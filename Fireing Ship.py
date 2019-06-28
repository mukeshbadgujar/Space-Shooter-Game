import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Initializing Game and Create Screen Object
    pygame.init()
    ai_settings = Settings()
    # Initializing Gaming Window
    screen = pygame.display.set_mode((ai_settings.screenWidth, ai_settings.screenHeight))
    pygame.display.set_caption("Alien Attack")

    # Make a Ship
    ship = Ship(ai_settings, screen)

    # Starting Main Loop
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)




run_game()
