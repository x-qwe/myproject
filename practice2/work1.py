#用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个

class DaXia:
    #定义属性
    yanzhi=100
    power=100
    #定义绝学
    def juexue(self,jxmc):
        self.jxmc = jxmc
        print(f"看招,{self.jxmc}")
#实例化类
QianFeng=DaXia()
QianFeng.juexue("降龙十八掌")

LuXiaoFeng=DaXia()
LuXiaoFeng.juexue("灵犀一指")

class People:
    def zhiye(self,zy):
        if zy =="说书人":
            print("九河下梢天津卫，三道浮桥两道关")
        if zy =="相声演员":
            print("桃叶尖上尖，柳叶遮满了天，在其位那个明啊公，细听我来言~")
        if zy =="影视演员":
            print("其实我想做个好人")
#实例化类
people=People()
people.zhiye("相声演员")

class DLDL:
    hunhuan = 0
    huanli = 10
    def huobai(self,name):
        print(f"我的伙伴是{name}")
TanSan=DLDL()
TanSan.huobai("史莱克七怪")
