import pygame
from pygame.sprite import Sprite


class Hero(Sprite):
    """Class for hero managing."""

    def __init__(self, sg_game):
        """Initialize hero and set his starting position."""
        super().__init__()
        self.screen = sg_game.screen
        self.settings = sg_game.settings
        self.screen_rect = sg_game.screen.get_rect()

        # Download hero picture and get its rect.
        self.image = pygame.image.load('images/girl.bmp')
        self.rect = self.image.get_rect()

        # Create each new hero at the bottom of screen, in the centre.
        self.rect.midbottom = self.screen_rect.midbottom

        # Save float value for hero position horizontally.
        self.x = float(self.rect.x)

        # Moving indicator.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update current hero position based on moving indicator."""
        # Update value hero.x, not rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.hero_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.hero_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw hero in his current position."""
        self.screen.blit(self.image, self.rect)

    def center_hero(self):
        """Place the hero on the center of the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)