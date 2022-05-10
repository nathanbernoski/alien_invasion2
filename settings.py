import pygame


class Settings:
    # Class to store all settings for game
    def __init__(self):

        # Screen Settings
        self.bg_color = (0, 0, 0)
        self.screen_width = 900
        self.screen_height = 600

        # Bullet Settings
        self.bullet_speed = 2
        self.bullet_width = 4
        self.bullet_length = 10
        self.bullet_color = (255, 255, 0)

        # Shield Settings
        self.shield_length = 75
        self.shield_width = 100

        # Player Settings
        self.lives = 3
        self.score = 0
        self.wave_number = 1
        self.font = pygame.font.SysFont("Times New Roman", 25, True, False)
        self.fleet_lim = 0
