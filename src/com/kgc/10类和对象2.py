# class Person(object):
#     def __init__(self,name,age):
#         self.__name=name
#         self.age=age
#     def show(self):
#         print(self.name)
#     def getName(self):
#         return self.__name
# p=Person("abc",20)
# p.show()
# class Animal(object):
#     def __init__(self,name):
#         self.name=name
#     def run(self):
#         print(self.name+"is running")
# class Cat(Animal):
#     def __init__(self,name,type):
#         # super().__init__(name)
#         Animal.__init__(self,name)
#         self.type=type
#
# cat=Cat("lele","cat")
# cat.run()
# class Person(object):
#     name="zhangsan"
#     __age=30
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p=Person("lisi",100)
# print(p.name)
# print(p.age)
# print(Person.__age)
# class People(object):
#     country = 'china'#类属性
# print(People.country)
# p = People()
# print(p.country)
# p.country = 'japan'
# print(p.country) #实例属性会屏蔽掉同名的类属性
# print(People.country)
# class People(object):
#     country = 'china'#类方法，用classmethod来进行修饰
#     @classmethod
#     def getCountry(cls):
#         return cls.country
# p = People()
# print(p.getCountry()) #可以用过实例对象引用
# print (People.getCountry()) #可以通过类对象引用
# class People(object):
#     country = 'china'#类方法，用classmethod来进行修饰 @classmethod
#     @classmethod
#     def getCountry(cls):
#         return cls.country
#     @classmethod
#     def setCountry(cls,country):
#         cls.country = country
# p = People()
# print(p.getCountry()) #可以用过实例对象引用
# print(People.getCountry()) #可以通过类对象引用
# People.setCountry('japan')
# print(p.getCountry())
# print(People.getCountry())
# class People(object):
#     country = 'china'
#     @staticmethod#静态方法
#     def getCountry():
#         return People.country
# print (People.getCountry())
# p=People()
# print(p.getCountry())
class Singleton:
    __instance=None
    __first_init=True
    def __init__(self,name):
        if self.__first_init:
            self.__first_init=False
            self.name=name
    def __new__(cls,name):
        if not cls.__instance:
            cls.__instance=object.__new__(cls)
        return cls.__instance
s=Singleton("zhangsan")
s1=Singleton("lisi")
print(s.name)
print(s1.name)
print(id(s))
print(id(s1))
