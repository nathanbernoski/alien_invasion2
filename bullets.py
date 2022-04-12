import pygame
from pygame.sprite import Sprite

class Bullets(Sprite):
    # A subclass of bullets fired from the ship
    def __init__(self, settings, screen, ship):
        # INitializes a bullet object and tracks the position on screen
        super(Bullets, self).__init__()
        self.screen = screen

        # create bullet rectangle at 0, 0
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_length)
        #move the bullet to the top of the ship
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #store the bullets as a decimal value
        self.y = float(self.rect.y)

        # assign bullet color
        self.color = settings.bullet_color

        # assign the speed of the bullets
        self.speed = settings.bullet_speed

    def update(self):
        # move the bullet up the screen
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        # draw bullet on screen
        pygame.draw.rect(self.screen, self.color, self.rect)