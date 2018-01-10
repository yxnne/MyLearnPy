# 这是一个外星人入侵的小游戏
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化游戏，创建屏幕对象
    pygame.init()

    # 使用引入设置
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("外星人入侵啦")

    # 创建飞船
    ship = Ship(ai_settings, screen)

    # 开始游戏的主循环
    while True:

        # 设置背景色
        # bg_color = (230, 230, 230)

        # 监听键盘和鼠标
        gf.check_events(ship)
        # ship更新下自己的状态
        ship.update()
        # 绘制最新更新屏幕
        gf.update_screen(ai_settings, screen, ship)


# 调用程序入口函数
run_game()
