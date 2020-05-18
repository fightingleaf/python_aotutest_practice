from class_TongLao import TongLao

class XuZhu(TongLao):  # 创建XuZhu类
    def __init__(self, hp, power):  # 初始化属性
        super().__init__(hp, power)  # 继承父类TongLao的属性

    def read(self):  # 创建read方法
        print("罪过罪过")


