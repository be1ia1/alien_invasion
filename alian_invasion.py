import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    '''Загальний клас, що керує ресурсами та поведінкою гри'''

    def __init__(self) -> None:
        '''Ініціалізувати гру, створити ресурси гри'''
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_haight))
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)


    def run_game(self):
        '''Розпочати головний цикл гри'''
        while True:
            # Слідкувати за подіями миші та клавіатури
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Наново перемальовувати екран на кожній ітерації циклу
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            # Показати останній намальований екран
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()