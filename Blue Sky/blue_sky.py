import pygame

import sys

from settings import Settings
from character import Character

class BlueSky:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Blue Sky")
        self.bg_color = (196, 217, 255)
        self.character = Character(self)

    def run_display(self):
        while True:

            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond tp keypresses and mouse event"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    def _update_screen(self):
        """Update images on the screem, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.character.blitme()
        pygame.display.flip()


if __name__ == '__main__':
   bs =BlueSky()
   bs.run_display()
