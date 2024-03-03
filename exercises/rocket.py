import pygame

class Rocket():
    def __init__(self, ex_game) -> None:
        """Initialize the rocket and set its starting position"""
        self.screen = ex_game.screen
        self.screen_rect = ex_game.screen.get_rect()
        self.image = pygame.image.load('exercises/images/rocket.bmp')
        self.rocket_speed = 5.5

        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        # move right
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.rocket_speed
        # move left
        if self.moving_left and self.rect.left > 0:
            self.x -= self.rocket_speed
        # move up
        if self.moving_up and self.rect.top > 0:
            self.y -= self.rocket_speed
        # move down
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.rocket_speed
            
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the rocket at its current location"""
        self.screen.blit(self.image, self.rect)