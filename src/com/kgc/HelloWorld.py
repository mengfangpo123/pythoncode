#coding=utf-8
"""

"""
# print("helloWorld",end="\t")
# a="\"abc\""
# print(a)
# print('''line1
# line2
# line3''')
# b=int("100")
# print(b)
# print(type(b))
# print(2**3)
# import keyword
# print(keyword.kwlist)
# print("shsohs","asdffas")
# print('hi,%s,you have $%d.'%('Michael',1000))
# print('%2d-%04d'%(3,1))
# print('%s'%1999999999)
# print('Age: %s. Gender: %s' % (25, True))
# print('chengzhangyu %d%%'%7)
# b="asd"
# a=input("请输入")
# print(a)
# print(10//3)
# a,b=1,2
# print(a,b)
# age = 3
# if age >= 18:
#     print('your age is', age)
#     print('adult')
# else:
#     print('your age is', age)
#     print('teenager')
# i=1
# while i<10:
#     j=1
#     while j<=i:
#         print('%d*%d=%d'%(j,i,i*j),end="\t")
#         if j==i:
#             print()
#         j += 1
#     i+=1
# name="abcdefg"
#
# print(name[::-2])
# mystr = 'hello world and bjsxt yunshuxueyuan sxt beijing'
# print(mystr.find("asd"))
# print(mystr.index("hello"))
# print(mystr.count("sxt"))
# print(mystr.replace("sxt", "kgc",  mystr.count("hello")))
# print(mystr.split(" ", 2))
# print(mystr.capitalize())
# print(mystr.title())
# print(mystr.startswith("hello"))
# print(mystr.center(100,"*"))
# print(mystr.strip())
# print(mystr.partition("sxt"))
# print(mystr.rpartition("sxt"))
# print(mystr.splitlines())
# print(mystr.isalpha())
# print(mystr.isdigit())
# b='fang'
# print(mystr.join(b))
# classmates = ['Michael', 'Bob', 'Tracy']
# print(len(classmates))
# print(classmates[0])
# print(classmates[-1])
# classmates.append("hello")
# print(classmates)
# a = [1, 2]
# b = [3, 4]
# a.append(b)
# print(a)
# a.extend(b)
# print(a)
# a = [0, 1, 2]
# a.insert(1, 3)
# print(a)
# a = ['a', 'b', 'c', 'a', 'b']
# print(a.index('a', 0, 3))
# print(a.count('b'))
# l=['abcdef', ['aaa', 'bb', 'ccc'], 'ddd', 'fff']
# del l[0]
# print(l)
# l.pop()
# print(l)
# l.remove(['aaa', 'bb', 'ccc'])
# print(l)

# a = [1, 4, 2, 3]
# a.reverse()
# print(a)
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
# chars = ['a', 'b', 'c', 'd']
# for i,cha in enumerate(chars):
#     print(i,cha)
#
# t = (1,)
# print(t)
# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# print(d["Michael"])
# info = {'name':'班长', 'id':100, 'sex':'f', 'address':'地球亚洲中国北京'}
# print(info.get("age",11))
# newId = input('请输入新的学号')
# info["age"]=int(newId)
# print(info)
# del info["age"]
# print(info)
# info.clear()
# print(info)


# info = {'name':'班长', 'id':100, 'sex':'f', 'address':'地球亚洲中国北京'}
# print(len(info))
# key=info.keys()
# print(key)
# value=info.values()
# print(value)
# i = info.items()
# print(i)
# print()
# def add2num(a, b,c):
#     d=a+b-c
#     print(d)
# add2num(10,20,2)

#
# def fun(a, b, *args, **kwargs):
#     print(a)
#     print(b)
#     print(args)
#     for key,value in kwargs.items():
#         print(key,value)
# # fun(1, 2, 3, 4, 5, m=6, n=7, p=8)
#
# c = (3, 4, 5)
# d = {"m":6, "n":7, "p":8}
# fun(1, 2, c, d)


# def selfAdd(a):
#     a += a
# a_int = 1
# selfAdd(a_int)
# print(a_int)

# a=200
# def test1():
#
#     a=30
#     print(a)
# test1()
# def test2():
#     global a
#     a=10
#     a +=100
#     print(a)
# test2()

# a = 1
# def f():
#
#     a +=10
#     print(a)
# f()

# li = [1,]
# print(li)
# def f2():
#     global li
#     li.append(1)
#     print(li)
# f2()

# n=4
# result=1
# i=1
# while i<=4:
#     result=result*i
#     i+=1
# print(result)

# def test1(n):
#     if n==1:
#         return 1
#     else:
#         return n*test1(n-1)
# print(test1(5))
# def test1(x):
#     if(x<=2):
#         return 1
#     else:
#         return test1(x-1)+test1(x-2)
# print(test1(6))
# sum = lambda arg1, arg2: arg1 + arg2
# print(sum(10,20))
# def fun(a, b, opt):
#     print(a)
#     print(b)
#     print(opt(a,b))
# fun(1,2,lambda x,y:x+y)

# def test1(a,b,func):
#     return func(a,b)
# func_new=input("input")
# print(test1(22,22,func_new))

# stus = [ {"name":"zhangsan", "age":18}, {"name":"lisi", "age":19}, {"name":"wangwu", "age":17} ]
# stus.sort(key = lambda x:x['age'])
# print(stus)
# f = open(r'F:\hive2.txt', 'r')
# # f.write("asdfasdfasdfa\nsdafsdfasdfasdf")
# # print(f.readline())#读取所有文件
# # print(f.tell())
# str = f.read(3)
# print(str)
# f.seek(5,1)
# print(f.tell())
# # f.seek(10,1)
#
# print(f.read())
# # print("-"*30)
# # content = f.read()
# # print(content)
# f.close()
# import os
# print(os.name)
# print(os.listdir())
# print(os.getcwd())
# os.remove("f://hive2.txt")
class Person(object):
    def __init__(self,name="abcd",age=20):
        # print(name)
        self.name=name
        print(self.name)
        self.age=20
    def __new__(cls, name,age):
        print("我爱你")
        cls.name=name
        cls.age=age
        return object.__new__(cls)
    def __del__(self):
        print(self.name+"删除了")
p=Person("芳芳",22)
p1=Person("凯凯",23)
p2=p
p3=p
del p















