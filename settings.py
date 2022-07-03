class Settings:
    '''This class will store all the settings for the alien invasion'''

    def __init__(self):
        '''Initialize the game's settings '''
        #Screen settings
        self.screen_width = 1370
        self.screen_height = 705
        self.bg_color = (230, 230, 230)

        #Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        #Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        #Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 6
        #fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
