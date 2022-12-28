import pygame.font

class Button:

    def __init__(self, sg_game, msg):
        """Initialize attributes of the button."""
        self.screen = sg_game.screen
        self.screen_rect = self.screen.get_rect()

        # Specify size and characteristics of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Create object rect button and place it on the center.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Message on the button should be shown one time.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Convert text to the image and place it on the button center."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw an empty button, and than the text.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)