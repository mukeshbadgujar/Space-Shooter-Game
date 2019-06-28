import sys
import pygame


def check_events(ship):
    # Responding to Events K & M
    # getting Event from Keyboard and Mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move Ship Right
                # ship.rect.centerx += 1
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    # Updating Images on Screen and flip to new screen
    # Redraw the Screen for every loop passing
    screen.fill(ai_settings.bgColor)
    ship.blitme()

    # Managing Recently Drawing Screen To Show
    pygame.display.flip()