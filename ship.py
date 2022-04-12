import pygame


class Ship():

    def __init__(self, screen):

        # load image of ship and access image data
        self.screen = screen
        self.image = pygame.image.load('images/img_1.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        # tells computer to interpret images and background as a rectangle
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # set starting location of each ship
        # makes the center of the ship at the center of the screen
        self.rect.centerx = self.screen_rect.centerx
        # makes the bottom of the ship at the bottom of the screen
        self.rect.bottom = self.screen_rect.bottom

        self.rect.bottom = self.screen_rect.bottom
        # stores centerx of ship as a decimal value
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

        # Create movement flag to determine if ship is moving
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        # draw the ship on the screen
        self.screen.blit(self.image, self.rect)

    def update(self):
        # updates image of ship left and right
        if self.moving_right:
            self.center_x += .5
        if self.moving_left:
            self.center_x -= .5
        if self.moving_up:
            self.center_y -= .5
        if self.moving_down:
            self.center_y += .5

        # Keeps the Ship on the screen from all 4 sides
        if self.center_x <= 20:
            self.center_x = 20
        if self.center_x >= 880:
            self.center_x = 880
        if self.center_y >= 575:
            self.center_y = 575
        if self.center_y <= 25:
            self.center_y = 25

        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y