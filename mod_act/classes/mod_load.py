import json
import math
import os
import shutil
import sys
import time

import pygame

from mod_act.method import mod_load


class Model(object):
    def __init__(self):
        self.counter = 0

        self.__rotate_center = 0,
        self.__rotate_link_pos = 1

        self.tex_path = ''

        self._name = ''
        self._info_dict = {}
        self.bilt_sort = []
        self.behaves = []

    def __getitem__(self, item):
        if isinstance(item, int):
            return self._info_dict[self.bilt_sort[item]]
        if isinstance(item, str):
            return self._info_dict[item]

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= len(self):
            raise StopIteration
        else:
            val = self.bilt_sort[self.counter]
            self.counter += 1

            return self._info_dict[val]

    def __len__(self):
        return len(self.bilt_sort)

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
        var.tex_path = tex_file
        var.name = name

        return var

    @staticmethod
    def load(filename: str):
        if os.path.isfile(filename):
            dir_path = os.path.split(filename)[0]

            with open(filename, 'r')as input_value:
                value = json.load(input_value, )

            var = Model()

            var.name = value['name']
            end_type = value['end_type']
            Sub_model_group = value['Sub_model_group']
            behaves_group = value['behaves_group']
            tex_address = value["tex_address"]
            div_address = value["div_address"]

            with open(os.path.join(dir_path, div_address), 'r')as file:
                div = json.load(file)
            group = mod_load.spilt_tex(pygame.image.load(os.path.join(dir_path, tex_address)), div)

            var.load_from_dict(group)

            for val in var.bilt_sort:
                with open(os.path.join(dir_path, Sub_model_group[val]), 'r')as file:
                    value = json.load(file)

                var[val].load_from_dict(value, var)

            return var
        else:
            raise FileNotFoundError(f'file {filename} not found')

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

    def save(self, dir_path):
        """
        --------------------------------
        生成的文件夹：
        model_name
            model_name.sp.json --file
            end_type.json  --file
            SubModel   --dir
                mod_1.json
                mod_2.json
            work_need
                model_name.atlas.json
                model_name.png
            behaves
                behave_1.json
                behave_2.json
                ...
            else
                bg.png
                else.json
        -----------------------------
        model_name.sp.json
        保存格式：
        {
        name:name,

        end_type:end_type.json

        Sub_model_group:sub models-->{SubModel/mod_1.json, SubModel/mod_.json, ...},

        behaves_group:model behaves -->[behaves/behave_1.json, behaves/behave_1.json, ...]

        tex_address:tex_path(相对路径),

        div_address:div_path(相对路径),
        }
        -----------------------------
        end_type.json
        保存格式:
        {
        sub_mod_1:{pos_x,pos_y,rotate_degree}
        sub_mod_2:{pos_x,pos_y,rotate_degree}
        sub_mod_3:{pos_x,pos_y,rotate_degree}
        ...
        }
        ----------------------------
        mod_%s.json %sub model_name
        保存格式：
        {
        name:name,
        link_pos:[x,y]
        link_mod:str-->link on the sub model
        link_type:0-->face;1-->rotatable;2-->body(nothing to link)
        link_groups:{#keep follow sub model}
        }
        ---------------------------
        model_name.atlas.json
        保存格式：
        {
        mod_x:{'xy':xy,size:size,rotate:rotate}
        mod_2:{'xy':xy,size:size,rotate:rotate}
        mod_3:{'xy':xy,size:size,rotate:rotate}
        mod_4:{'xy':xy,size:size,rotate:rotate}
        ...
        }
        ---------------------------
        behave_%d.json %num
        保存格式：

        {
        action_mod:mod_name,
        move_x:x
        move_y:y
        rotate_degree:degree
        keep_time:time
        is_loop:boolean
        }
        --------------------------
        else.json
        保存格式：
        {
        bg_path:path
        ...
        }
        -------------------------
        :return:None
        """
        save_path = os.path.join(dir_path, self.name)
        sub_mod = os.path.join(save_path, 'SubModel')
        work_need = os.path.join(save_path, 'work_need')
        behave = os.path.join(save_path, 'behaves')
        else_file = os.path.join(save_path, 'else')

        shutil.copyfile(self.tex_path, os.path.join(work_need, f"{self.name}.png"))

        os.makedirs(save_path, exist_ok=True)
        os.makedirs(sub_mod, exist_ok=True)
        os.makedirs(work_need, exist_ok=True)
        os.makedirs(behave, exist_ok=True)
        os.makedirs(else_file, exist_ok=True)

        model_sp = {
            "name": self.name,
            "end_type": "end_type.json",
            "Sub_model_group": {var: f'SubModel/mod_{var}.json' for var in self.bilt_sort},
            "behaves_group": [f'behaves/behave_{var}.json' for var in range(len(self.behaves))],
            "tex_address": f"work_need/{self.name}.png",
            "div_address": f"work_need/{self.name}.atlas.json",
        }

        end_type = {}
        for var in self.bilt_sort:
            per_mod: SubModel = self._info_dict[var]
            end_type[var] = {'pos_x': per_mod.bilt_rect.x, 'pos_y': per_mod.bilt_rect.y,
                             'rotate_degree': per_mod.rotate_angle}

        sub_mod_group = [(val.save(), val.get_value()) for val in self._info_dict.values()]

        save_value = {}
        for val in sub_mod_group:
            save_value[val[0]['name']] = val[1]

        main_path = os.path.join(save_path, f"{self.name}.sp.json")

        with open(main_path, 'w')as file:
            json.dump(model_sp, file)

        with open(os.path.join(save_path, "end_type.json"), 'w')as file:
            json.dump(end_type, file)

        with open(os.path.join(work_need, f"{self.name}.atlas.json"), 'w')as file:
            json.dump(save_value, file)

        for val in sub_mod_group:
            with open(os.path.join(sub_mod, f'mod_{val[0]["name"]}.json'), 'w')as file:
                json.dump(val[0], file)

        for index in range(len(self.behaves)):
            with open(os.path.join(behave, f'behave_{index}.json'), 'w')as file:
                json.dump(self.behaves[index], file)


class SubModel(pygame.sprite.Sprite):
    def __init__(self, name, val: dict):
        super(SubModel, self).__init__()
        self.pic: pygame.Surface = val['pic']

        self.values = val

        self.rect: pygame.Rect = self.pic.get_rect()

        self.bilt_rect: pygame.Rect = self.rect.copy()
        self.center_pos = self.bilt_rect.center

        self.name: str = name
        self.link_to: SubModel = None
        self._link_to_pos = [0, 0]
        self.new_link = [0, 0]
        self.link_type = 0
        self._links = {'body': [None, (1, 1)]}

        self.rotate_angle = 0
        self.rotated: pygame.Surface = None

    @property
    def link_to_pos(self):
        return self._link_to_pos

    @link_to_pos.setter
    def link_to_pos(self, val):

        self._link_to_pos = val

    def load_from_dict(self, val: dict, model):
        self.name = val['name']
        self._link_to_pos = val["link_pos"]
        self.link_to = val["link_mod"]
        if self.link_to is None:
            self.link_to = None
        else:
            self.link_to = model[self.link_to]
        self.link_type = val['link_type']
        link_group_string = val['link_group']
        for index in link_group_string:
            self._links[index[0]] = [model[index], index[1]]

    def save(self):
        """
        mod_%s.json %sub model_name
        保存格式：
        {
        name:name,
        link_pos:[x,y]
        link_mod:str-->link on the sub model
        link_type:
            0-->face;
            1-->rotatable;
            2-->body(nothing to link)
        link_groups:{#keep follow sub model}
        }
        :return:
        """
        if self.link_to is None:
            val = None
        else:
            val = self.link_to.name
        var = {
            "name": self.name,
            "link_pos": self._link_to_pos,
            "link_mod": val,
            "link_type": self.link_type,
            "link_group": list(zip(self._links.keys(), list(zip(*self._links.values()))[-1]))
        }
        return var

    def get_value(self):
        """
        mod_x:{'xy':xy,size:size,rotate:rotate},
        :return:
        """
        var = self.values.copy()
        del var['pic']
        return var

    def update(self, angle: float = 0, link_rotate: bool = False, move_time: float = 0.0,
               bilt_short_change: str = "move_0-time_0",
               rotate_by: int = 0, move_pos: list = None, *args, **values):
        """
        进行操作时使用的方法
        1）如果为非旋转，旋转角可为0，基于的旋转方法 无视

        2）修改绘制顺序，move+>0->上移，=0 不动，<0下移，time->相对开始时间的秒数，必须小于持续时间

        3）进行旋转，移动操作

        4）将命令传递到连接的所有子部件上（神经冲动（@_@））-link_rotate==True-->所有子部件同时以相同旋转角，相同时间进行旋转。
        否则不进行旋转，只随连接点移动

        5）先进行旋转——>保存为副本，所有的操作都不在原图上，所有的操作都基于原图。

        6)线程中进行——回调函数——》》当完成后调用，在线程中渲染完成全部帧后播放


        :param move_pos: 移动的距离 *只能由 《body》模块移动下发
        :param angle: 旋转角度，使用角度制
        :param link_rotate: 连接部分是否需要旋转
            -> False -->连接部分不跟随旋转
            -> True -->连接部分跟随旋转
        :param move_time: 旋转所持续的时间，以秒计算
        :param bilt_short_change: 所处的绘制顺序,上移，下移，隐藏等
        :param rotate_by: 基于的旋转中心
            -> 0 -->基于自身中心的旋转
            -> 1 -->基于连接点旋转
        :param args: 其他参数：
                    forever :bool =False ->不断循环
                    back :bool =False ->完成后相同旋转角，相反方向，相同时间，再来一次，回到起点算一个。
        :return:
        """
        if move_pos is None:
            move_pos = [0, 0]

        self.rotate_angle += angle

    def update_link_pos(self, x, y):
        self.new_link[0] += round(x)
        self.new_link[1] += round(y)
        # 新的连接点，

    def move(self, x, y):
        """
        对自身进行不旋转的移动
        :param x:
        :param y:
        :return:
        """
        self.bilt_rect.x = x - self._link_to_pos[0]
        self.bilt_rect.y = y - self.link_to_pos[1]

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

    def rotate(self, angle: float):
        """
        绕连接关节旋转，先计算相对图片的中心的距离，和相对x,y,距离，计算夹角。
        将总相对水平的旋转角计算出来，计算出相对图片中心的距离。
        将旋转后的矩形和旋转前的矩形的中心对齐，计算旋转后的相对的连接点的距离，调整绘制坐标点的位置
        :param angle: 旋转角，->使用角度制
        :return: None
        """
        self.rotated = pygame.transform.rotate(self.pic, angle)
        abs_pos = mod_load.rotate(self.rect, self.link_to_pos, self.rotated, angle)
        self.bilt_rect.x = round(self.bilt_rect.x + abs_pos[0])
        self.bilt_rect.y = round(self.bilt_rect.y + abs_pos[1])

        self.new_link[0] = round(self._link_to_pos[0] + abs_pos[0])
        self.new_link[1] = round(self._link_to_pos[1] + abs_pos[1])

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


if __name__ == '__main__':
    pic = pygame.image.load('..\\..\\text_dir\\eye_1_2.png')
    a = SubModel('a', {'pic': pic})
    a.link_to_pos = [10, 10]
    a.move(100, 100)

    degree = 0

    pygame.init()

    win = pygame.display.set_mode([500, 500])
    work = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    work = not work
                if event.key == pygame.K_q:
                    sys.exit()
        win.fill((255, 255, 255))
        if work:
            # abs_x, abs_y = mod_load.rotate(a.rect, a.link_to_pos, pygame.transform.rotate(a.pic, degree), degree)

            # a.update_link_pos(abs_x, abs_y)
            # print_x_x = (round(a.bilt_rect.x + abs_x), round(a.bilt_rect.y + abs_y))
            a.rotate(degree)
            r = win.blit(a.rotated, (a.bilt_rect.x, a.bilt_rect.y))
            pygame.draw.rect(win, (0, 0, 0), r, 1)

            # win.blit(a.pic, (a.bilt_rect.x, a.bilt_rect.y))
            degree += 15
            # time.sleep(0.125)

            pygame.mouse.set_pos(100, 100)

        pygame.display.flip()
