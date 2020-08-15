"""
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”
fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。

加入模块化改造
在此基础上可以添加自己的“freestyle”哦
"""
class TongLao:
    #构造方法中定义两个实例属性，血量和武力值，整个类中都可以用这个属性
    def __init__(self,hp,power):
        self.hp=hp
        self.power=power
    #定义一个see_people方法，传入name参数
    def see_people(self,name):
        #定义一个普通属性
        name=name
        #根据题目中的条件，打印不同的内容，如果不是这三个人，则打印放肆
        if name == "无崖子":
            print("师弟！！！！")
        elif name == "李秋水":
            print("呸，贱人")
        elif name == "丁春秋":
            print("叛徒！我杀了你")
        else:
            print("放肆")

    #fight_zms方法（天山折梅手）
    # 需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
    def fight_zms(self,enemy_hp,enemy_power):
        #用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍
        my_power =self.power*10
        my_hp =self.hp/2
        #传入并接收敌人的hp和power
        enemy_hp=enemy_hp
        enemy_power=enemy_power

        #进行一回合制对打
        my_hp=my_hp-enemy_power
        enemy_hp=enemy_hp-my_power
        #打完之后，比较双方血量。血多的一方获胜。
        if my_hp >enemy_hp:
            print("尊主，你赢了，为手下报仇")
        elif my_hp <enemy_hp:
            print("尊主，这有酒，用生死符反败为胜")
        else:
            print("尊主，这有九转熊蛇丸，快补充一下")
#实例化TongLao类，并传入参数
tl=TongLao(hp=100,power=10)
#调用fight_zms类
tl.see_people("李秋水")
tl.fight_zms(50,50)