import pygame.font
from pygame.sprite import Group
from pygame import Surface

from hero import Hero

class Scoreboard:
    """Class, that represents scores of the game."""

    def __init__(self, sg_game):
        """Initialize attributes, related to scores."""
        self.sg_game = sg_game
        self.screen = sg_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = sg_game.settings
        self.stats = sg_game.stats

        # Font settings.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare image with starting score.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_heroes()

    def check_high_score(self):
        """Check if the new record is get."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """Convert level to the image."""
        level_str = 'Level: ' + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color)

        # Place level under the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_score(self):
        """Convert score to the image."""
        rounded_score = round(self.stats.score, -1)
        score_str = 'Score: ' + "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color)

        # Show scores on the top right corner of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Generate record to the image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = 'High score: ' + "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)

        # To center records by horizontal
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_heroes(self):
        """Shows, how many heroes left."""
        hero_left = 'Heroes left: ' + str(self.stats.hero_left)
        self.hero_image = self.font.render(hero_left, True, self.text_color)

        # Show scores on the top right corner of the screen.
        self.hero_rect = self.hero_image.get_rect()
        self.hero_rect.left = self.screen_rect.left + 20
        self.hero_rect.top = 20

    def show_score(self):
        """Show on the screen scores, level and heroes."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.hero_image, self.hero_rect)
