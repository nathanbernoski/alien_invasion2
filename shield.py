import pygame
from pygame.sprite import Sprite


class Shield(Sprite):
    # Class to represent a single alien in an alien fleet

    def __init__(self, settings, screen):

        super(Shield, self).__init__()

        self.screen = screen
        self.settings = settings

        self.color = (0, 255, 0)

        self.rect1 = pygame.Rect(100, 450, settings.shield_width, settings.shield_length)
        # self.rect = self.rect1.get_rect()
        # self.rect2 = pygame.Rect(300, 450, settings.shield_width, settings.shield_length)
        # self.rect3 = pygame.Rect(500, 450, settings.shield_width, settings.shield_length)
        # self.rect4 = pygame.Rect(700, 450, settings.shield_width, settings.shield_length)

    def blit(self):
        # draws alien on the screen
        self.screen.blit(self.rect1, self.rect)
        # screen_rect = self.screen.get_rect()

    def update(self):
        pygame.draw.rect(self.screen, self.color, self.rect1)
        # pygame.draw.rect(self.screen, self.color, self.rect2)
        # pygame.draw.rect(self.screen, self.color, self.rect3)
        # pygame.draw.rect(self.screen, self.color, self.rect4)
    # def update(self):
