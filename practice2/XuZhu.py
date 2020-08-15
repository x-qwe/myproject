"""
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
"""
from practice2.TongLao import TongLao


class XuZhu(TongLao):
    def __init__(self):
        self.read()
    def read(self):
        print("罪过，罪过")

xz=XuZhu()
