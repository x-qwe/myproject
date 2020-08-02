"""
一个回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
"""

#定义了一个fight 函数
def fight():
    #定义四个变量，存放你和我的 血量和攻击力
    my_hp = 1200
    my_power = 200
    your_hp = 1000
    your_power = 200
    # 对打多轮，谁的血量先小于等于0，谁就输了
    while True:
        # 根据回合制游戏规则，个人打斗之后的血量等于当前血量减去对方的攻击力
        my_hp=my_hp-your_power
        your_hp=your_hp-my_power
        # 谁的血量先为0，谁就输了
        if your_hp<=0:
            print("我的剩余血量为：",my_hp)
            print("你的剩余血量为：",your_hp)
            print("我赢了")
            break
        elif my_hp<=0:
            print("我的剩余血量为：", my_hp)
            print("你的剩余血量为：", your_hp)
            print("你赢了")
            break

###调用fight函数
fight()
