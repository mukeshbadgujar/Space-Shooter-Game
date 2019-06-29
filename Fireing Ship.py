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
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Attack")

    # Make a Ship
    ship = Ship(ai_settings, screen)

    # Make group to store bullets
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)
    # Make Alien
    # alien = Alien(ai_settings, screen)

    # Starting Main Loop
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
