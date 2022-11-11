from ship import Ship
from settings import Settings
import pygame


class AlienInvasion:
    def __init__(self):
        self.settings = Settings()
        if self.settings.screen_with > 0 and self.settings.screen_height > 0:
            self.screen = pygame.display.set_mode((self.settings.screen_with, self.settings.screen_height))
        else:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.bg_color = self.settings.bg_color
        self.ship = Ship(self)
        self.running = True
        pygame.init()
        pygame.display.set_caption(self.settings.title)

    def run_game(self):
        print(self)
        while self.running:
            self._update_screen()
            self.ship.update()
            self._check_events()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.right_flag = True
                elif event.key == pygame.K_LEFT:
                    self.ship.left_flag = True
                elif event.key == pygame.K_UP:
                    self.ship.up_flag = True
                elif event.key == pygame.K_DOWN:
                    self.ship.down_flag = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.right_flag = False
                elif event.key == pygame.K_LEFT:
                    self.ship.left_flag = False
                elif event.key == pygame.K_UP:
                    self.ship.up_flag = False
                elif event.key == pygame.K_DOWN:
                    self.ship.down_flag = False
                elif event.key == pygame.K_q:
                    self.running = False

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        pygame.display.flip()

    @classmethod
    def test(cls):
        print(cls)


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
    AlienInvasion.test()

