import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from hero import Hero
from snow import Snow, SuperSnow
from snowman import Snowman


class SnowGame:
    """General class, that manage resourses and game behavior."""

    def __init__(self):
        """Initialize game, create resourses of game."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.infoObject = pygame.display.Info()
        self.bg_img = pygame.image.load('images/winter.bmp')
        self.bg_img = pygame.transform.scale(self.bg_img, (self.infoObject.current_w, self.infoObject.current_h))

        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("My first game")

        # Create instance for saving game statistic and table on the screen
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.hero = Hero(self)
        self.snow = pygame.sprite.Group()
        self.snowmans = pygame.sprite.Group()

        self._create_crowd()

        # Create button Play.
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start main cycle of game."""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.hero.update()
                self._update_snow()
                self._update_snowmans()

            self._update_screen()

    def _check_events(self):
        """Monitor mouse and keyboard actions."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start new game when user press button Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset game statistic.
            self.settings.initialize_dynamic_settings()
            self._start_game()

            # Hide mouse cursor.
            pygame.mouse.set_visible(False)
    def _check_keydown_events(self, event):
        """Respond to button press."""
        if event.key == pygame.K_RIGHT:
            self.hero.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.hero.moving_left = True
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._throw_snow()
        elif event.key == pygame.K_p:
            self._start_game()

    def _check_keyup_events(self, event):
        """Respond when button is no longer pressed."""
        if event.key == pygame.K_RIGHT:
            self.hero.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.hero.moving_left = False

    def _start_game(self):
        """Initialize new game."""
        # Cancel game stats.
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_heroes()

        # Remove all snowmans and snowballs.
        self.snowmans.empty()
        self.snow.empty()

        # Create new crowd and place the hero in the center.
        self._create_crowd()
        self.hero.center_hero()

    def _throw_snow(self):
        """Create new snowball and add it to group of snowballs."""
        if len(self.snow) < self.settings.snow_allowed:
            if self.stats.level >= 10:
                new_snow = SuperSnow(self)
                self.snow.add(new_snow)
            else:
                new_snow = Snow(self)
                self.snow.add(new_snow)

    def _update_snow(self):
        """Update snowballs position and remove old snowballs."""
        # Update snowballs position.
        self.snow.update()

        for snow in self.snow.copy():
            if snow.rect.bottom <= 0:
                self.snow.remove(snow)

        self._check_snow_snowman_collisions()

    def _check_snow_snowman_collisions(self):
        """Reaction on collision snow and snowman."""
        # Remove all snow and snowmans that collided.
        collisions = pygame.sprite.groupcollide(self.snow, self.snowmans, True, True)

        if collisions:
            for snowmans in collisions.values():
                self.stats.score += self.settings.snowman_points * len(snowmans)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.snowmans:
            # Remove existing snow and create new crowd of snowmans.
            self.snow.empty()
            self._create_crowd()
            self.settings.increase_speed()

            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()

    def _update_snowmans(self):
        """Check, if crowd is on the edge of the screen
        and update positions of all snowmans."""
        self._check_crowd_edges()
        self.snowmans.update()

        # Check collision of snowman with hero.
        if pygame.sprite.spritecollideany(self.hero, self.snowmans):
            self._hero_hit()

        # Check if one of the snowmans touch the bottom of the screen.
        self._check_snowmans_bottom()

    def _create_crowd(self):
        """Create crowd of snowmans."""
        # Create snowmans and calculate number of snowmans in one line.
        # Distance between snowmans are equal to width of one snowman.
        snowman = Snowman(self)
        snowman_width, snowman_height = snowman.rect.size
        available_space_x = self.settings.screen_width - (2 * snowman_width)
        number_snowmans_x = available_space_x // (2 * snowman_width)

        # Calculate how many lines of snowmans can be placed on the screen.
        hero_height = self.hero.rect.height
        available_space_y = (self.settings.screen_height - (3 * snowman_height) - hero_height)
        number_rows = available_space_y // (2 * snowman_height)

        # Create crowd of snowmans.
        for row_number in range(number_rows):
            for snowman_number in range(number_snowmans_x):
                self._create_snowman(snowman_number, row_number)

    def _create_snowman(self, snowman_number, row_number):
        # Create snowman and place him to line.
        snowman = Snowman(self)
        snowman_width, snowman_height = snowman.rect.size
        snowman.x = snowman_width + 2 * snowman_width * snowman_number
        snowman.rect.x = snowman.x
        snowman.rect.y = snowman.rect.height + 2 * snowman.rect.height * row_number
        self.snowmans.add(snowman)

    def _check_crowd_edges(self):
        """React according to the event when one of
        snowmans reaches edge of the screen."""
        for snowman in self.snowmans.sprites():
            if snowman.check_edges():
                self._change_crowd_direction()
                break

    def _change_crowd_direction(self):
        """Move down entire crowd and change its direction."""
        for snowman in self.snowmans.sprites():
            snowman.rect.y += self.settings.crowd_drop_speed
        self.settings.crowd_direction *= -1

    def _hero_hit(self):
        """React on the collision between hero and snowman."""
        if self.stats.hero_left > 0:
            # Reduce hero_left and update the scoreboard.
            self.stats.hero_left -= 1
            self.sb.prep_heroes()

            # Remove existing snowmans and snow.
            self.snowmans.empty()
            self.snow.empty()

            # Create new crowd and place hero in the centre.
            self._create_crowd()
            self.hero.center_hero()

            # Pause the game.
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_snowmans_bottom(self):
        """Check if snowman does not touch the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for snowman in self.snowmans.sprites():
            if snowman.rect.bottom >= screen_rect.bottom:
                # React as the hero was hit.
                self._hero_hit()
                break

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.blit(self.bg_img, (0, 0))
        self.hero.blitme()
        for snow in self.snow.sprites():
            snow.draw_snow()
        self.snowmans.draw(self.screen)

        # Draw information about scores.
        self.sb.show_score()

        # Draw button 'Play' if game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Show the last drawn screen.
        pygame.display.flip()


if __name__ == '__main__':
    # Create game and run the game.
    sg = SnowGame()
    sg.run_game()
