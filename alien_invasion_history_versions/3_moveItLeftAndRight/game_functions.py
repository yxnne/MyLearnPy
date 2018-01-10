import sys

import pygame


def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # pygame.QUIT 其实就是小叉叉
            sys.exit()

        # 调整思路了，结合Key down 和 up 事件，实现连续不松手移动
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    """更新屏幕图像并绘制"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    pygame.display.flip()