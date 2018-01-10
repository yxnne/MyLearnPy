import sys

import pygame


def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # pygame.QUIT 其实就是小叉叉
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # 向右
                ship.rect.centerx += 1


def update_screen(ai_settings, screen, ship):
    """更新屏幕图像并绘制"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    pygame.display.flip()