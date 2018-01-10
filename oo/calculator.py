class Calculator():
    """计算器"""
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def add(self):
        """add"""
        return self.__a + self.__b

    def minus(self):
        """minus"""
        return self.__a - self.__b

    def multiply(self):
        """ * """
        return self.__a * self.__b

    def info(self):
        add_nfo = "add is : " + str(self.add())
        m_info = "m is : " + str(self.minus())

        print(add_nfo)
        print(m_info)