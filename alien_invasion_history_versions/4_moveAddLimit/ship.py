import pygame


class Ship():
    """飞船类"""
    def __init__(self, ai_settings, screen):
        """初始化飞船设置位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 放置飞船
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 移动标志
        self.moving_right = False
        self.moving_left = False

        # center属性，存储center的值
        self.center = float(self.rect.centerx)

    def update(self):
        """根据标志位调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx += 1
            # 更新center
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            # self.rect.centerx -= 1
            self.center -= self.ai_settings.ship_speed_factor

        # 根据center，更新rect
        self.rect.centerx = self.center

    def blitme(self):
        """绘制飞船"""
        self.screen.blit(self.image, self.rect)
