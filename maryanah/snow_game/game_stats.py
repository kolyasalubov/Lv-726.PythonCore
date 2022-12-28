class GameStats:
    """Checking game statistic."""

    def __init__(self, sg_game):
        """Initialize of statistic."""
        self.settings = sg_game.settings
        self.reset_stats()

        # Start the game in the inactive status.
        self.game_active = False

        # The record is not being reset.
        self.high_score = 0

    def reset_stats(self):
        """Initialize of statistic that can change during the game."""
        self.hero_left = self.settings.hero_limit
        self.score = 0
        self.level = 1