import pygame
import sys

class Rocket():
    pass


class BlueSky():
    
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        self.bg_color = (135, 206, 250)
        pygame.display.set_caption('Blue Sky')
    
    def _update_screen(self):
        # Update images on the screen, and flip to the new screen
        self.screen.fill(self.bg_color)
        pygame.display.flip()

    def _check_events(self):
        # Respond to keypresses and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

if __name__ == '__main__':
    bs = BlueSky()
    bs.run_game()