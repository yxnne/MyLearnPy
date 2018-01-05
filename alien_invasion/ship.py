import pygame


class Ship():
    """飞船类"""
    def __init__(self, screen):
        """初始化飞船设置位置"""
        self.screen = screen

        # 加载飞船图像
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 放置飞船
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """绘制飞船"""
        self.screen.blit(self.image, self.rect)
