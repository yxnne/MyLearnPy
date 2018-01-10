class Settings():
    """ 存放设置的地方"""
    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 飞船的速度
        self.ship_speed_factor = 1.5

