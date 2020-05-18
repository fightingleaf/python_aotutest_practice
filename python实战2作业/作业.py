# 作业2
# 用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个
#
#
class Car:  # 定义一个车的类
    def __init__(self, brand, color, dynamics, odometer):  # 初始化车类的实例
        self.brand = brand  # 初始化‘品牌’
        self.color = color  # 初始化‘颜色’
        self.dynamics = dynamics  # 初始化‘动力类型’
        self.odometer = odometer  # 初始化‘里程表’

    def get_descriptive(self):
        print("展示车类信息：")  # 提示“展示车辆信息”
        descriptive = "汽车品牌：" + str(self.brand) + "\n车身颜色：" + str(self.color) + "\n动力类型：" + \
                      str(self.dynamics) + "\n里程表：" + str(self.odometer)  # 讲车类信息聚合赋值给变量“descriptive”
        print(descriptive)  # 打印出“descriptive”来介绍车类信息

    def set_odometer(self, odometer):  # 创建一个可以设置汽车里程表的里程记录的方法
        self.odometer = odometer  # 通过参数odometer修改车辆“里程表”信息
        print("里程表已经设置为：" + (self.odometer))  # 提示已经更新了“里程表”信息


byd = Car('比亚迪', '白色', '纯电', '0km')  # 实例化“byd”
byd.get_descriptive()  # 调用Car类的get_descriptive()方法来展示车辆信息
print("\n")
byd.set_odometer('50km')  # 调用Car类的set_odometer()方法来更新“里程表”信息
print("\n")
byd.get_descriptive()  # 调用Car类的get_descriptive()方法来展示车辆信息


class Cup:  # 定义一个杯子的类
    def __init__(self, color, cubage):  # 初始化对象
        self.color = color  # 初始化杯子颜色属性
        self.cubage = cubage  # 初始化杯子容积属性

    def use_drink(self):  # 创建use_drink方法，打印出自己的用途
        print("杯子可以用来喝水")


cup_1 = Cup('白色', '500ml')  # 实例化杯子cup_1
print(cup_1.color)  # 打印杯子cup_1颜色属性
print(cup_1.cubage)  # 打印杯子cup_1容积属性
cup_1.use_drink()  # 调用use_drink方法


class Shoes:  # 定义一个鞋子的类型
    def __init__(self, color, use):
        self.color = color
        self.use = use

    def useful(self):
        print("不同的鞋子有不同的用途")


shoes_1 = Shoes('黑色', '羽毛球')  # 实例化shoes_1
print(shoes_1.color)
print(shoes_1.use)
shoes_1.useful()  # 调用useful方法

class Cat: # 创建一个猫类
    def __init__(self,color,sex): # 初始化猫的属性
        self.color = color # 初始化猫的颜色属性
        self.sex = sex # 初始化猫的性别属性

    def catch_the_mouse(self): # 定义catch_the_mouse方法
        print("派出猫猫去抓老鼠")


cat_1 = Cat('白色', '雄性') # 实例化cat_1
print(cat_1.color) # 打印猫的颜色属性
print(cat_1.sex) # 打印猫的性别属性
cat_1.catch_the_mouse() # 调用catch_the_mouse方法

class PostalCode:
    def __init__(self, city, code):
        self.city = city
        self.code = code

    def ues(self):
        print("必须要有邮政编码才能判断信件要送达的城市")


guangzhou = PostalCode("广州", '510000') # 实例化guangzhou
print(guangzhou.city) # 打印guangzhou的城市属性
print(guangzhou.code) # 打印guangzhou的邮政编码属性
guangzhou.ues() # 调用ues方法

# 作业3
# 定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
# see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”
# fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
# 定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
# 加入模块化改造
# 希望各位同学在此基础上可以添加自己的“freestyle”哦
#
#
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


tongtao_1 = TongLao(200, 2)  # 实例化tonglao_1
tongtao_1.see_people('李秋水')  # 对tonglao_1调用see_people方法，参数为“李秋水”
tongtao_1.fight_zms(100, 20)  # 对tonglao_1调用fight_zms方法，通过参数设定一个敌人并进行战斗


class XuZhu(TongLao):  # 创建XuZhu类
    def __init__(self, hp, power):  # 初始化属性
        super().__init__(hp, power)  # 继承父类TongLao的属性

    def read(self):  # 创建read方法
        print("罪过罪过")


xuzhu = XuZhu(1000, 100)  # 实例化xuzhu
print(xuzhu.hp)  # 打印hp属性，证明成功继承父类TongLao的属性
print(xuzhu.power)  # 打印power属性，证明成功继承父类TongLao的属性
xuzhu.read()  # 调用read方法

# 作业4
# 使用列表推导式写下面这个算法题
# 给定一个按非递减顺序排序的整数数组A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
#
# 示例
# 1：
# 输入：[-4, -1, 0, 3, 10]
# 输出：[0, 1, 9, 16, 100]
#
# 示例
# 2：
# 输入：[-7, -3, 2, 3, 11]
# 输出：[4, 9, 9, 49, 121]
#
# 提示：
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A
# 已按非递减顺序排序。


# 创建一个能够实现元素为原来列表中每个元素的平方组成的新列表的函数
def new_list(list):
    new_list = [] # 创建一个空白的新列表
    for i in list: # 创建for循环，构成新列表
        i = i**2
        new_list.append(i)
    return new_list # 返回新列表

# 创建一个实现冒泡排序函数
def bubble_sort(list):
    for i in range(1,len(list)): # 排序测试
        print("这是第{}次排序".format(i))
        for j in range(len(list) - i): # 对比次数
            print("这是第{}次对比".format(j)) # 提示这是第几次排序
            if list[j]<list[j+1]: # if语句实现排序
                list[j],list[j+1] = list[j+1],list[j]
    return list


list_original_1= [-4, -1, 0, 3, 10]
print("\n这是原来的列表："+str(list_original_1))# 构建一个乱序列表

list_new_1 = new_list(list_original_1)
print("\n这是原列表元素平方后的新列表："+str(list_new_1))

print("\n开始进行排序：")
print("\n这是重新排序后的新列表："+str(bubble_sort(list_new_1)))
