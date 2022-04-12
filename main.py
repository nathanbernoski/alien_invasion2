# Nathan Bernoski
import pygame
from ship import Ship
from settings import Settings
from alien import Alien
import game_functions as gf
from pygame.sprite import Group

def alien_invasion():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    # add ship
    ship = Ship(screen)
    alien = Alien(settings, screen)

    # make a group to store bullets in
    bullets = Group()

    # make a group of aliens
    aliens = Group()
    gf.create_fleet(settings, screen, ship, aliens)

    # loop to start animation
    while True:

        # access event handler
        gf.check_events(ship, settings, screen, bullets)
        gf.update_screen(settings, screen, ship, bullets, aliens)
        bullets.update()

        #Ship.check_ship

alien_invasion()
