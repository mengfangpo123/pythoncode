class Axe(object):
    def __init__(self,name):
        self.name=name
    def cut_tree(self):
        print("使用"+self.name+"砍树")


class StoneAxe(Axe):
    def cut_tree(self):
        print("使用石斧砍树")

class SteelAxe(Axe):
    def cut_tree(self):
        print("使用钢砍树")

class Factory(object):
    @staticmethod
    def getAxe(type):
        if "stone"==type:
            return StoneAxe(type)
        elif "steel"==type:
            return SteelAxe(type)
        else :
            print("参数错误")

class People(object):
    def __init__(self,name):
        self.name=name
    def work(self,type):
        print(self.name+"开始工作")
        axe=Factory.getAxe(type)
        axe.cut_tree()
p=People("zhangsan")
p.work("stone")