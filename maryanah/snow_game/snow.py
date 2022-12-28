import pygame
from pygame.sprite import Sprite

class Snow(Sprite):
    """Class for snowballs managing."""

    def __init__(self, sg_game):
        """Create object snowball in current hero position."""
        super().__init__()
        self.screen = sg_game.screen
        self.settings = sg_game.settings

        # Download snow picture and get its rect.
        self.image = pygame.image.load('images/snow-12-12.bmp')
        self.rect = self.image.get_rect()
        self.rect.midtop = sg_game.hero.rect.midtop

        # Save snowball position as float value.
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        """Move snowball to the screen top."""
        # Update float position of the snowball.
        self.y -= self.settings.snow_speed

        # Update rect position.
        self.rect.y = self.y

    def draw_snow(self):
        """Draw snowball on the screen."""
        self.screen.blit(self.image, self.rect)


class SuperSnow(Snow):
    """Class for super snowballs managing."""
    def __init__(self, sg_game):
        super().__init__(sg_game)

        # Download snow picture and get its rect.
        self.image = pygame.image.load('images/snow-24-24.bmp')
        self.rect = self.image.get_rect()
        self.rect.midtop = sg_game.hero.rect.midtop


