import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #Class to represent a single alien in an alien fleet

    def __init__(self, settings, screen):

        super(Alien, self).__init__()

        # define attributes of screen and settings
        self.screen = screen
        self.settings = settings

        # imports alien ship image
        self.image = pygame.image.load('images/alien ship.png')
        # scales image of ship
        self.image = pygame.transform.scale(self.image, (40, 20))
        # gives aliens rectangular properties
        self.rect = self.image.get_rect()

        # sets the starting location of alien
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

        self.speed = 1
        self.direction = 1

        # spacing for the fleet
        self.available_space_x = self.settings.screen_width - (2 * self.rect.width)
        self.number_of_aliens = int(self.available_space_x / (2 * self.rect.width))

    def blitme(self):
        # draws alien on the screen
        self.screen.blit(self.image, self.rect)

    def update(self):
        # moves_alien
        if self.check_screen() == True:
            self.direction *= -1
        self.x += self.speed * self.direction
        self.rect.x = self.x

    def check_screen(self):
        #return true if an alien is at the edge of the screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True