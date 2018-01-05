import sys

import pygame


def check_events():
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # pygame.QUIT 其实就是小叉叉
            sys.exit()


def update_screen(ai_settings, screen, ship):
    """更新屏幕图像并绘制"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    pygame.display.flip()