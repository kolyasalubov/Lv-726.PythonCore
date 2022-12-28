class Settings:
    """Class for saving all game settings."""

    def __init__(self):
        """Initialize permanent game settings."""

        # Screen settings.
        self.screen_widht = 1200
        self.screen_height = 600
        self.bg_color = (8, 176, 206)

        # Hero settings.
        self.hero_limit = 3

        # Snow settings.
        self.snow_allowed = 5

        # Snowman settings.
        self.crowd_drop_speed = 10

        # How quickly game should speed up.
        self.speedup_scale = 1.1

        # How quickly speed up scores for snowmans.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize variable settings."""
        self.hero_speed = 3
        self.snow_speed = 20
        self.snowman_speed = 1

        # crowd_direction 1 means moving to the right; -1 - to the left.
        self.crowd_direction = 1

        # Scores getting.
        self.snowman_points = 50

    def increase_speed(self):
        """Increase speed settings and value of snowman."""
        self.hero_speed *= self.speedup_scale
        self.snow_speed *= self.speedup_scale
        self.snowman_speed *= self.speedup_scale

        self.snowman_points = int(self.snowman_points * self.score_scale)

