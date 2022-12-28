import pygame
from pygame.sprite import Sprite

class Snowman(Sprite):
    """Class, that represents one snowman."""
    def __init__(self, sg_game):
        """Initialize snowman and set his starting position."""
        super().__init__()
        self.screen = sg_game.screen
        self.settings = sg_game.settings

        # Load the snowman image and set its rect atribute.
        self.image = pygame.image.load('images/snowman.bmp')
        self.rect = self.image.get_rect()

        # Start each new snowman near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the snowman exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True, if snowman is on the edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move snowman to the right or left."""
        self.x += (self.settings.snowman_speed * self.settings.crowd_direction)
        self.rect.x = self.x