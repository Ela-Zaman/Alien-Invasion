import pygame

# Find a bitmap image of a game character you like or
# convert an image to a bitmap. Make a class that draws the character at the
# center of the screen, then match the background color of the image to the background 
# color of the screen or vice versa

class Character:
    def __init__(self, blue_sky):
        self.screen = blue_sky.screen
        self.screen_rect = blue_sky.screen.get_rect()
        self.image = pygame.image.load("images\ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
    
    def blitme(self):
        """draw the ship at its current location. """
        self.screen.blit(self.image, self.rect)