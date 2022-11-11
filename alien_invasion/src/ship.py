import pygame.image


class Ship:
    """ 管理飞船的类 """

    def __init__(self, ai_game):
        """ 初始化飞船并设置其初始位置 """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.speed = ai_game.settings.ship_speed

        """ 飞船的左右上下移动 """
        self.up_flag = False
        self.down_flag = False
        self.right_flag = False
        self.left_flag = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.right_flag and self.rect.right < self.screen_rect.right:
            self.rect.x += self.speed
        if self.left_flag and self.rect.x > 0:
            self.rect.x -= self.speed
        if self.up_flag and self.rect.top > 0:
            self.rect.y -= self.speed
        if self.down_flag and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.speed
