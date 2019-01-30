import math

import pygame

from mod_act.method import mod_load


class Model(object):
    def __init__(self):
        self.__rotate_center = 0,
        self.__rotate_link_pos = 1

        self._name = ''
        self._info_dict = {}
        self.bilt_sort = []

    @staticmethod
    def open(tex_file, spilt_file):
        """
        加载Q版小人的贴图，分割文件，返回一个Model类实例
        :param tex_file: 贴图文件
        :param spilt_file: 分割文件
        :return: Model
        ：:rtype Model
        """

        image = pygame.image.load(tex_file)

        name, val = mod_load.build_part_model(image, spilt_file)

        var = Model()

        var.load_from_dict(val)
        var.name = name

        return var

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def load_from_dict(self, val: dict):
        for var in val.keys():
            self._info_dict[var] = SubModel(var, val[var])
            self.bilt_sort.append(var)


class SubModel(pygame.sprite.Sprite):
    def __init__(self, name, val: dict):
        super(SubModel, self).__init__()
        self.pic: pygame.Surface = val['pic']

        self.rect: pygame.Rect = self.pic.get_rect()

        self.bilt_rect: pygame.Rect = self.rect.move(0, 0)
        self.center_pos = self.bilt_rect.center

        self.name: str = name
        self.link_to: SubModel = None
        self._link_to_pos = [0, 0]
        self._links = {}

    @property
    def link_to_pos(self):
        return self._link_to_pos

    @link_to_pos.setter
    def link_to_pos(self, val):
        self._link_to_pos = val

    def update(self, angle: float, link_rotate: bool = False, move_time: float = 0.0, bilt_short: int = 0,
               rotate_by: int = 0, move_pos: list = None, *args):
        """
        进行操作时使用的方法


        :param move_pos: 相对移动的距离
        :param angle: 旋转角度，使用角度制
        :param link_rotate: 连接部分是否需要旋转
            -> False -->连接部分不跟随旋转
            -> True -->连接部分跟随旋转
        :param move_time: 旋转所持续的时间，以秒计算
        :param bilt_short: 所处的绘制顺序
        :param rotate_by: 基于的旋转中心
            -> 0 -->基于自身中心的旋转
            -> 1 -->基于连接点旋转
        :param args: 其他参数
        :return:
        """
        if move_pos is None:
            move_pos = [0, 0]
        pass

    def move(self, x, y):
        """
        对自身进行不旋转的移动
        :param x:
        :param y:
        :return:
        """
        self.link_to_pos = (x, y)

    def add_link_on(self, pos: list, model):
        """
        添加连接于自身的子模块
        :param pos: 相对于自身初始态的连接坐标点
        :param model: 子模块本身
        :return:
        """
        if isinstance(model, SubModel):
            self._links[model.name] = [model, pos]

    def add_link_to(self, pos: list):
        """
        为自身添加旋转环绕点

        :param pos:旋转环绕点相对于自身初始态的相对坐标
        :return:
        """
        pass

    def rotate(self, angle: int):
        """
        绕连接关节旋转，先计算相对图片的中心的距离，和相对x,y,距离，计算夹角。
        将总相对水平的旋转角计算出来，计算出相对图片中心的距离。
        将旋转后的矩形和旋转前的矩形的中心对齐，计算旋转后的相对的连接点的距离，调整绘制坐标点的位置
        :param angle: 旋转角，->使用角度制
        :return: None
        """
        abs_pos = [self.link_to_pos[0] - self.center_pos[0], self.link_to_pos[1] - self.center_pos[1]]
        tan_val = math.atan(abs_pos[1] / abs_pos[0])
        rad = math.radians(angle)

        distance = math.sqrt(abs_pos[0] ** 2 + abs_pos[1] ** 2)

        rotate_angle = tan_val + rad
        rotate_pic = pygame.transform.rotate(self.pic, angle)
        rotate_rect = rotate_pic.get_rect()
        rotate_rect.center = self.center_pos

        abs_x = math.cos(rotate_angle) * distance
        abs_y = math.sin(rotate_angle) * distance

        abs_pos = [rotate_rect.centerx + abs_x, rotate_rect.centery + abs_y]

        self.bilt_rect.x -= (abs_pos[0] - self.link_to_pos[0])
        self.bilt_rect.y += (abs_pos[1] - self.link_to_pos[1])

    def link_rotate(self, angle):
        """
        旋转后，连接的部分也跟随旋转，连接坐标也相应改变，绘制的坐标也相应改变。
        :param angle:
        :return:
        """
        for val in self._links.keys():
            pos = self._links[val][1]
            model: SubModel = self._links[val][0]

            abs_pos = [pos[0] - self.center_pos[0], pos[1] - self.center_pos[1]]
            tan_val = math.atan(abs_pos[1] / abs_pos[0])
            rad = math.radians(angle)

            distance = math.sqrt(abs_pos[0] ** 2 + abs_pos[1] ** 2)

            rotate_angle = tan_val + rad
            rotate_pic = pygame.transform.rotate(self.pic, angle)
            rotate_rect = rotate_pic.get_rect()
            rotate_rect.center = self.center_pos

            abs_x = math.cos(rotate_angle) * distance
            abs_y = math.sin(rotate_angle) * distance

            abs_pos = [rotate_rect.centerx + abs_x, rotate_rect.centery + abs_y]

            model.move(*abs_pos)
