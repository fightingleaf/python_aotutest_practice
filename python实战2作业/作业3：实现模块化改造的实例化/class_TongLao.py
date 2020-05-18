class TongLao:  # 定义一个名为“TongLao”的类
    def __init__(self, hp, power):  # 初始化属性，定义两个属性
        self.hp = hp
        self.power = power

    def see_people(self, name):
        if name == 'WYZ':  # 判断看到的是无崖子
            print("师弟！！！！")
        elif name == '李秋水':  # 判断看到的是李秋水
            print("呸，贱人")
        elif name == '丁春秋':  # 判断看到的是丁春秋
            print("叛徒！我杀了你")
        else:  # 判断看到的是其他人
            print("和你不熟")

    def fight_zms(self, enemy_hp, enemy_power):  # 定义fight_zms方法，使用天山折梅手并且与预设的一个敌人进行一回合战斗
        hp = self.hp / 2  # hp变为一半
        power = self.power * 10  # power变为10倍
        if (hp - enemy_power) > (enemy_hp - power):  # 一轮打斗后，童姥本人血量为减去敌人攻击值，敌人血量为减去童姥攻击值，比较两者，如果童姥打斗后血量大于敌人
            print("童姥赢了")  # 打印我赢了
        elif (hp - enemy_power) < (enemy_hp - power):  # 如果一轮打斗后，童姥打斗后血量小于敌人
            print("童姥输了")  # 打印再来一局
        else:  # 如果一轮打斗后，血量相等
            print("平局")
