import pygame, sys, time
from pygame.locals import *
from random import randint


class TankMain(object):
    """坦克大战的主窗口"""
    width = 800
    height = 600
    my_tank_missile_list = []
    my_tank = None
    # enemy_list = []
    enemy_list = pygame.sprite.Group()  # 敌方坦克的族群
    explode_list = []
    enemy_missile_list = pygame.sprite.Group()
    wall = None

    # 开始游戏的方法
    def startGame(self):
        # pygame模块初始化,加载系统的资源
        pygame.init()
        # 创建一个屏幕,屏幕窗口的大小,宽和高,窗口的特性,能否拉伸(0,resizeable,fullscreem),
        screem = pygame.display.set_mode((TankMain.width, TankMain.height), 0, 32)
        # 给窗口设置标题
        pygame.display.set_caption("坦克大战")
        TankMain.wall = Wall(screem, 80, 160, 30, 100)
        # 创建一个我方坦克,坦克显示在屏幕的仲夏部位置
        TankMain.my_tank = My_Tank(screem)
        if len(TankMain.enemy_list) == 0:
            for i in range(1, 6):  # 游戏开始时候初始化5个敌方坦克
                TankMain.enemy_list.add(Enemy_Tank(screem))  # 把敌方坦克放到族群里面
        while True:
            if len(TankMain.enemy_list) < 5:
                TankMain.enemy_list.add(Enemy_Tank(screem))
            # 设置屏幕的背景色为黑色
            screem.fill((0, 0, 0))
            # 显示左上角的文字
            for i, text in enumerate(self.write_text(), 1):
                screem.blit(text, (0, 5 + (15 * i)))
            # 创建游戏中的墙,并且对墙和其他对象进行检测
            TankMain.wall.display()
            TankMain.wall.hit_other()
            self.get_event(TankMain.my_tank, screem)  # 获取事件,根据获取的事件进行处理
            if TankMain.my_tank:
                TankMain.my_tank.hit_enemy_missile()  # 我方的坦克和敌方的炮弹进行碰撞检测
            if TankMain.my_tank and TankMain.my_tank.live:
                TankMain.my_tank.display()
                TankMain.my_tank.move()  # 在屏幕上移动我方坦克
            else:
                TankMain.my_tank = None
            # 显示所有的敌方坦克
            for enemy in TankMain.enemy_list:
                enemy.display()
                enemy.random_move()
                enemy.random_fire()
            # 显示所有的我方炮弹
            for m in TankMain.my_tank_missile_list:
                if m.live:
                    m.display()
                    m.hit_tank()  # 炮弹打中敌方坦克
                    m.move()
                else:
                    TankMain.my_tank_missile_list.remove(m)
            # 显示所有敌方炮弹
            for m in TankMain.enemy_missile_list:
                if m.live:
                    m.display()
                    m.move()
                else:
                    TankMain.enemy_missile_list.remove(m)
            for explode in TankMain.explode_list:
                explode.display()
            # 每次休眠0.05秒调到下一帧
            time.sleep(0.05)
            # 显示重置
            pygame.display.update()

    # 获取所有的时间(点击鼠标,敲击键盘)
    def get_event(self, my_tank, screem):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.stopGame()  # 程序退出
            if event.type == KEYDOWN and not my_tank and event.key == K_n:
                print("new a tank")
                TankMain.my_tank = My_Tank(screem)
            if event.type == KEYDOWN and my_tank:
                if event.key == K_LEFT:
                    my_tank.direction = "L"
                    my_tank.stop = False
                    # my_tank.move()
                if event.key == K_RIGHT:
                    my_tank.direction = "R"
                    my_tank.stop = False
                    # my_tank.move()
                if event.key == K_UP:
                    my_tank.direction = "U"
                    my_tank.stop = False
                    # my_tank.move()
                if event.key == K_DOWN:
                    my_tank.direction = "D"
                    my_tank.stop = False
                    # my_tank.move()
                if event.key == K_ESCAPE:
                    self.stopGame()
                if event.key == K_SPACE:
                    m = my_tank.fire()
                    m.good = True  # 我方坦克发射的炮弹,好炮弹
                    TankMain.my_tank_missile_list.append(m)
            if event.type == KEYUP and my_tank:
                if event.key == K_LEFT or event.key == K_RIGHT or event.key == K_UP or event.key == K_DOWN:
                    my_tank.stop = True

    # close game
    def stopGame(self):
        sys.exit()

    # set the game windows title
    def set_title(self):
        pass

    # 在屏幕的左上角显示文字内容
    def write_text(self):
        font = pygame.font.SysFont("simsunnsimsun", 20)
        text_sf1 = font.render("敌方坦克数量为:%d" % len(TankMain.enemy_list), True, (255, 0, 0))
        text_sf2 = font.render("我方炮弹数量为:%d" % len(TankMain.my_tank_missile_list), True, (255, 0, 0))
        return text_sf1, text_sf2


# 坦克大战游戏中所有对象的父类
class BaseItem(pygame.sprite.Sprite):
    def __init__(self, screem):
        pygame.sprite.Sprite.__init__(self)
        #         所有对象功能的属性
        self.screem = screem

    # 把坦克对对应图片显示在游戏窗口上
    def display(self):
        if self.live:
            self.image = self.images[self.direction]
            self.screem.blit(self.image, self.rect)


class Tank(BaseItem):
    # 坦克的高度和宽度,定义类属性,所有坦克对象高和宽都是一样的
    width = 50
    height = 50

    def __init__(self, screem, left, top):
        super().__init__(screem)
        # self.screem=screem#坦克在移动或者显示过程中需要用到当前游戏的屏幕上
        self.direction = "D"  # 坦克的方向,默认方向往下(上下左右)
        self.speed = 10  # 坦克移动的速度
        self.stop = False
        self.images = {}  # take的所有图片,key为方向,value为图片(surface)
        self.images["L"] = pygame.image.load("images/tankL.gif")
        self.images["R"] = pygame.image.load("images/tankR.gif")
        self.images["U"] = pygame.image.load("images/tankU.gif")
        self.images["D"] = pygame.image.load("images/tankD.gif")
        self.image = self.images[self.direction]  # 坦克的图片有方向决定
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.live = True  # 决定坦克是否消灭了
        self.oldtop = self.rect.top
        self.oldleft = self.rect.left

    def stay(self):
        self.rect.top = self.oldtop
        self.rect.left = self.oldleft

    def move(self):
        self.oldleft = self.rect.left
        self.oldtop = self.rect.top
        if not self.stop:
            if self.direction == "L":
                if self.rect.left > 0:  # 判断坦克是否在屏幕左边的边界上
                    self.rect.left -= self.speed
                else:
                    self.rect.left = 0
            elif self.direction == "R":
                if self.rect.right < TankMain.width:
                    self.rect.right += self.speed
                else:
                    self.rect.right = TankMain.width
            elif self.direction == "U":
                if self.rect.top > 0:
                    self.rect.top -= self.speed
                else:
                    self.rect.top = 0
            elif self.direction == "D":
                if self.rect.bottom < TankMain.height:
                    self.rect.bottom += self.speed
                else:
                    self.rect.bottom = TankMain.height

    def fire(self):
        m = Missile(self.screem, self)
        return m


class My_Tank(Tank):
    def __init__(self, screem):
        # 创建一个我方坦克,坦克显示在屏幕的仲夏部位置)
        super().__init__(screem, 275, 400)
        self.stop = True
        self.live = True

    def hit_enemy_missile(self):
        hit_list = pygame.sprite.spritecollide(self, TankMain.enemy_missile_list, False)
        for m in hit_list:  # 我方坦克中弹了
            m.live = False
            TankMain.enemy_missile_list.remove(m)
            self.live = False
            explode = Explode(self.screem, self.rect)
            TankMain.explode_list.append(explode)


class Enemy_Tank(Tank):

    def __init__(self, screem):
        super().__init__(screem, randint(1, 5 * 100), 200)
        self.speed = 4
        self.step = 10  # 坦克按照某个方向连续移动的步数
        self.get_random_direction()

    # 敌方坦克,按照一个确定的随机方向,连续移动6步,然后才能再次改变方向.
    def random_move(self):
        if self.live:
            if self.step == 0:
                self.get_random_direction()
                self.step = 6
            else:
                self.move()
                self.step -= 1

    def get_random_direction(self):
        r = randint(0, 4)  # 得到一个坦克移动方向和停止的随机数
        if r == 4:
            self.stop = True
        elif r == 1:
            self.direction = "L"
            self.stop = False
        elif r == 2:
            self.direction = "R"
            self.stop = False
        elif r == 3:
            self.direction = "U"
            self.stop = False
        elif r == 0:
            self.direction = "D"
            self.stop = False

    def random_fire(self):
        r = randint(0, 50)
        if r > 45:
            m = self.fire()
            TankMain.enemy_missile_list.add(m)
        else:
            return


class Missile(BaseItem):
    width = 12
    height = 12

    def __init__(self, screem, tank):
        super().__init__(screem)
        self.tank = tank
        self.direction = tank.direction  # 炮弹的方向由锁发射的坦克方向决定
        self.speed = 14  # 炮弹移动的速度
        self.stop = False
        # 炮弹的所有图片,key为方向,value为图片(surface)
        self.images = {}
        self.images["L"] = pygame.image.load("images/missileL.gif")
        self.images["R"] = pygame.image.load("images/missileR.gif")
        self.images["U"] = pygame.image.load("images/missileU.gif")
        self.images["D"] = pygame.image.load("images/missileD.gif")
        self.image = self.images[self.direction]  # 坦克的图片有方向决定
        self.rect = self.image.get_rect()
        self.rect.left = tank.rect.left + (tank.width - self.width) // 2
        self.rect.top = tank.rect.top + (tank.height - self.height) // 2
        self.live = True  # 炮弹是否消灭了
        self.good = False

    def move(self):
        if self.live:  # 如果炮弹还存在
            if self.direction == "L":
                if self.rect.left > 0:  # 判断坦克是否在屏幕左边的边界上
                    self.rect.left -= self.speed
                else:
                    self.live = False
            elif self.direction == "R":
                if self.rect.right < TankMain.width:
                    self.rect.right += self.speed
                else:
                    self.live = False
            elif self.direction == "U":
                if self.rect.top > 0:
                    self.rect.top -= self.speed
                else:
                    self.live = False
            elif self.direction == "D":
                if self.rect.bottom < TankMain.height:
                    self.rect.bottom += self.speed
                else:
                    self.live = False

    # 炮弹击中坦克,第一种,我方炮弹击中敌方坦克,敌方炮弹击中我方坦克,
    def hit_tank(self):
        if self.good:  # 如果炮弹是我方的炮弹
            hit_list = pygame.sprite.spritecollide(self, TankMain.enemy_list, False)
            for e in hit_list:
                e.live = False
                TankMain.enemy_list.remove(e)  # 如果敌方坦克被击中,从列表中删除敌方坦克
                self.live = False
                explode = Explode(self.screem, e.rect)  # 产生了一个爆炸对象
                TankMain.explode_list.append(explode)


# 爆炸类
class Explode(BaseItem):
    def __init__(self, screen, rect):
        super().__init__(screen)
        self.live = True
        self.images = [pygame.image.load("images/0.gif"), \
                       pygame.image.load("images/1.gif"), \
                       pygame.image.load("images/2.gif"), \
                       pygame.image.load("images/3.gif"), \
                       pygame.image.load("images/4.gif"), \
                       pygame.image.load("images/5.gif"), \
                       pygame.image.load("images/6.gif"), \
                       pygame.image.load("images/7.gif"), \
                       pygame.image.load("images/8.gif"), \
                       pygame.image.load("images/9.gif"), \
                       pygame.image.load("images/10.gif")]
        self.step = 0
        self.rect = rect  # 爆炸的位置和发生爆炸前,保单喷到的坦克位置一样,在构建爆炸的时候把坦克的rect传递进来

    # dispaly方法在整个游戏运行过程中,循环调用,每个0.1秒调用一次
    def display(self):
        if self.live:
            if self.step == len(self.images):  # 最后一张爆炸图片已经显示了
                self.live = False
            else:
                self.image = self.images[self.step]
                self.screem.blit(self.image, self.rect)
                self.step += 1
        else:
            pass  # 删除该对象


# 游戏中的障碍物
class Wall(BaseItem):
    def __init__(self, screen, left, top, width, height):
        super().__init__(screen)
        self.rect = Rect(left, top, width, height)
        self.color = (255, 0, 0)

    def display(self):
        self.screem.fill(self.color, self.rect)

    # 针对墙和其他坦克或者炮弹的碰撞检测
    def hit_other(self):
        if TankMain.my_tank:
            is_hit = pygame.sprite.collide_rect(self, TankMain.my_tank)
            if is_hit:
                TankMain.my_tank.stop = True
                TankMain.my_tank.stay()
        if TankMain.enemy_list:
            hits_list = pygame.sprite.spritecollide(self, TankMain.enemy_list, False)
            for e in hits_list:
                e.stop = True
                e.stay()
        if TankMain.my_tank_missile_list:
            hit_missile_list = pygame.sprite.spritecollide(self, TankMain.my_tank_missile_list,False)
            for m in hit_missile_list:
                m.live=False
        if TankMain.enemy_missile_list:
            hit_enemy_missile_list = pygame.sprite.spritecollide(self, TankMain.enemy_missile_list,False)
            for m in hit_enemy_missile_list:
                m.live = False

if __name__ == '__main__':
    game = TankMain()
    game.startGame()
