import pygame

class Ship:
    """A class to manage ship, """

    def __init__(self, ai_game):
        """Initialize the ship and set its"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a float for the ship's exact horizontal posotopn.
        self.x = float(self.rect.x)
        #Moving flags; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update the ship's position based on the movement flag."""
        #Update the ship's x value, not the rect.
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x
    def blitme(self):
        """Draw the ship at its current location. """
        self.screen.blit(self.image, self.rect)
#pygame treat all the game element like rectangle
#