from class_TongLao import TongLao
from class_XuZhu import XuZhu

print("下面是实例化TongLao测试")
tongtao_1 = TongLao(200, 2)  # 实例化tonglao_1
print("遇到李秋水时的反应：")
tongtao_1.see_people('李秋水')  # 对tonglao_1调用see_people方法，参数为“李秋水”
print("使用天山折梅手与预设的敌人战斗的模拟：")
tongtao_1.fight_zms(100, 20)  # 对tonglao_1调用fight_zms方法，通过参数设定一个敌人并进行战斗

print("-------分割线-------")

print("下面是实例化XuZhu测试")
xuzhu = XuZhu(1000, 100)  # 实例化xuzhu
print("下面打印hp属性，证明成功继承父类TongLao的属性")
print(xuzhu.hp)  # 打印hp属性，证明成功继承父类TongLao的属性
print("下面打印hp属性，证明成功继承父类TongLao的属性")
print(xuzhu.power)  # 打印power属性，证明成功继承父类TongLao的属性
print("调用read念经的方法")
xuzhu.read()  # 调用read方法
