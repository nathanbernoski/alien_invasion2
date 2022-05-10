import pygame
import sys
from bullets import Bullets
from alien import Alien
from time import sleep

# something
def check_events(ship, settings, screen, bullets):
    # checks for key/mouse events and responds
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
            if event.key == pygame.K_UP:
                ship.moving_up = True
            if event.key == pygame.K_DOWN:
                ship.moving_down = True
            if event.key == pygame.K_SPACE:
                new_bullet = Bullets(settings, screen, ship)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False
            if event.key == pygame.K_UP:
                ship.moving_up = False
            if event.key == pygame.K_DOWN:
                ship.moving_down = False


def check_collision(bullets, aliens):
    pygame.sprite.groupcollide(bullets, aliens, bullets, aliens)


def collision_check(bullets, shields):
    pygame.sprite.groupcollide(bullets, shields, bullets, shields)


def update_screen(settings, screen, ship, bullets, aliens):
    # color the screen with background color
    screen.fill(settings.bg_color)
    # update the ship
    ship.update()
    aliens.update()
    # draw the ship on screen
    ship.blit()
    check_collision(bullets, aliens)
    # draw alien ship
    aliens.draw(screen)
    print_text(settings, screen)
    check_fleet(aliens, settings)
    check_ship(settings, screen, ship, aliens, bullets)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # update display
    pygame.display.flip()


def create_fleet(settings, screen, ship, aliens):
    # creates a fleet of aliens
    alien = Alien(settings, screen)
    number_of_aliens = get_number_of_aliens(settings, alien.rect.width)
    number_of_rows = get_number_rows(settings, alien.rect.height, ship.rect.height)

    for row_number in range(number_of_rows):
        for alien_number in range(number_of_aliens):
            create_alien(settings, screen, aliens, alien_number, row_number)


def get_number_of_aliens(settings, alien_width):
    # Determine the number of aliens that fit in a row
    available_space_x = settings.screen_width - 2 * alien_width
    number_of_aliens = int(available_space_x/(2*alien_width))
    return number_of_aliens


def get_number_rows(settings, alien_height, ship_height):
    available_space_y = settings.screen_height - 17 * alien_height - ship_height
    number_of_rows = int(available_space_y/(2 * alien_height))
    return number_of_rows


def create_alien(settings, screen, aliens, alien_number, row_number):
    # create an alien and place it in a row
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = 2 * alien_width * alien_number
    alien.rect.x = alien.x

    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def print_text(settings, screen):
    surface = settings.font.render("Score: " + str(settings.score), True, (0, 255, 0))
    screen.blit(surface, (50, 540))
    surface2 = settings.font.render("Lives: " + str(settings.lives), True, (0, 255, 0))
    screen.blit(surface2, (50, 565))


def check_ship(settings, screen, ship, aliens, bullets):
    for alien in aliens:
        if pygame.sprite.spritecollideany(ship, aliens):
            settings.lives -= 1
            settings.score -= 100
            reset_wave(settings, screen, ship, aliens, bullets)
            return True


def check_fleet(aliens, settings):
    if len(aliens) == 0:
        settings.score += 100
        settings.fleet_lim += 1

        return True
    else:
        return False


def new_wave(settings, screen, ship, aliens):
    if len(aliens) == 0:
        create_fleet(settings, screen, ship, aliens)


def reset_wave(settings, screen, ship, aliens, bullets):
    aliens.empty()
    bullets.empty()
    create_fleet(settings, screen, ship, aliens)


def alien_invasion(settings, screen, ship, aliens, bullets):
    for alien in aliens:
        if alien.rect.bottom > settings.screen_height:
            settings.score -= int(settings.points*len(aliens)/2)
            reset_wave(settings, screen, ship, aliens, bullets)


def game_end(settings):
    if settings.fleet_lim == 20:
        print("You Won")
        print("Your score was " + str(settings.score))
        return True
    elif settings.lives == 0:
        print("You Lost")
        print("Your score was " + str(settings.score))
        return True
    else:
        return False


def close_game(settings):
    if game_end(settings) == True:
        sys.exit()
