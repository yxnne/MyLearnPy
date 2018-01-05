# 这是一个外星人入侵的小游戏
import sys
import pygame

from settings import Settings
from ship import Ship


def run_game():
    # 初始化游戏，创建屏幕对象
    pygame.init()

    # 使用引入设置
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("外星人入侵啦")

    # 创建飞船
    ship = Ship(screen)

    # 开始游戏的主循环
    while True:

        # 设置背景色
        # bg_color = (230, 230, 230)

        # 监听键盘和鼠标
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # pygame.QUIT 其实就是小叉叉
                sys.exit()

        # 绘制最新更新屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        pygame.display.flip()


run_game()
