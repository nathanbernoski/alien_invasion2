class Settings():
    # Class to store all settings for game
    def __init__(self):

        # Screen Settings
        self.bg_color = (0, 0, 0)
        self.screen_width = 900
        self.screen_height = 600

        # Bullet Settings
        self.bullet_speed = 1
        self.bullet_width = 4
        self.bullet_length = 10
        self.bullet_color = (255, 255, 0)

        # Player Settings
        self.lives = 3
        self.score = 0