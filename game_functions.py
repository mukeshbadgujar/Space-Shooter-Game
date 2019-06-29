import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

# getting Event from Keyboard and Mouse
def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # Move Ship Right
        # ship.rect.centerx += 1
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def fire_bullet(ai_settings, screen, ship, bullets):
    # Creating New Bullets And Adding in Group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, aliens, bullets):
    # Updating Images on Screen and flip to new screen
    # Redraw the Screen for every loop passing
    screen.fill(ai_settings.bgColor)

    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    aliens.draw(screen)
    #aliens.blitme()

    # Managing Recently Drawing Screen To Show
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    # Deleting Bullets that Passed Away From Screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))
    check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets):
    # Checking any bullet hitting alien
    # deleting bullets and aliens
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        # Destroy existing bullets and creat new fleet
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def create_fleet(ai_settings, screen, ship, aliens):
    # Creating Full Fleet Of Aliens
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # create the First row of aliens
    # New >> Create The Fleet of Aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    # Checking No. of  alienn fit in row
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # creating and placing alien in row
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
    # determining no of rows fit on screen
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return  number_rows


def check_fleet_edges(ai_settings, aliens):
    # Respond appropriately if any aliens have reached at edge
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    # drop full fleet and change direction
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    # Respond to ship hits

    if stats.ships_left > 0:
        # Decrease life of 3
        stats.ships_left -= 1

        # Empty The list of aliens and Bullets
        aliens.empty()
        bullets.empty()

        # Create new Fleet ANd Center the Ship
        create_fleet(ai_settings, screen, ship, aliens)
        #ship.center_ship()

        # Puse
        sleep(0.5)
    else:
        stats.game_active = False


def check_alien_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    # Gining bottom ship delet
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # treet same if ship got hit
            ship_hit(ai_settings, stats, screen, ship, alien, bullets)
            break


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    '''check if the fleet is at an edge,
    and then updates its positions'''
    check_fleet_edges(ai_settings, aliens)
    # update positions of aliens
    aliens.update()

    # Look for alien ship collision
    if pygame.sprite.spritecollideany(ship, aliens):
        #print("Ship Hits!!!!!!!")
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    # Look for ailin hitting bottom
    check_alien_bottom(ai_settings, stats, screen, ship, aliens, bullets)



