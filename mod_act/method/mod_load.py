import os
import re
import math

import pygame


def rotate(tex_rect: pygame.Rect, link_pos:list, rotated_image: pygame.Surface, angle: float):
    """
    1）先计算相对图片的中心的距离，和相对x,y,距离，计算夹角。
    2）将总相对水平的旋转角计算出来，计算出相对图片中心的距离。
    将旋转后的矩形和旋转前的矩形的中心对齐，计算旋转后的相对的连接点的距离，调整绘制坐标点的位置

    :param rotated_image: 旋转后的图片
    :param tex_rect:要旋转的对象的矩形
    :param link_pos:旋转点
    :param angle: 旋转角，->使用角度制
    :return: 旋转点旋转后的位置
    """
    center_pos = tex_rect.center
    # 计算相对中心点的坐标
    abs_pos = [link_pos[0] - center_pos[0], link_pos[1] - center_pos[1]]
    # 计算相对过中心点的水平线的夹角
    if abs_pos[0] < 0 and -abs_pos[1] > 0:
        tan_val = math.atan(-abs_pos[1] / abs_pos[0]) + math.pi
    elif abs_pos[0] < 0 and -abs_pos[1] < 0:
        tan_val = math.atan(-abs_pos[1] / abs_pos[0]) + math.pi
    elif abs_pos[0] == 0:
        tan_val = 0.5 * math.pi
    else:
        tan_val = math.atan(abs_pos[1] / -abs_pos[0])

    # 计算对应的弧度
    rad = math.radians(angle)

    # 计算相对中心点的距离
    distance = math.sqrt(abs_pos[0] ** 2 + abs_pos[1] ** 2)

    # 计算旋转后的夹角
    rotate_angle = tan_val + rad

    degree = math.degrees(rotate_angle)
    # 旋转图片
    rotate_rect = rotated_image.get_rect()
    # 对齐旋转后的中心点
    rotate_rect.center = center_pos

    # 计算旋转后的点的相对坐标
    abs_x = math.cos(rotate_angle) * distance
    abs_y = math.sin(rotate_angle) * distance
    abs_pos = [rotate_rect.centerx + abs_x, rotate_rect.centery - abs_y]

    return_pos = (link_pos[0] + rotate_rect.x-abs_pos[0]  ,  link_pos[1] +rotate_rect.y-abs_pos[1] )

    return return_pos


def spilt_tex(tex, group):
    img = tex

    for var in group.keys():

        xy = group[var]['xy']
        size = group[var]['size']

        if group[var]['rotate'] == 'true':

            val = img.subsurface(pygame.Rect(xy, size[::-1]))
            val = pygame.transform.rotate(val, -90)
        else:
            val = img.subsurface(pygame.Rect(xy, size))

        group[var]['pic'] = val

    return group


def pos_spilt(file: str):
    mod_pattern = re.compile(r'^[^\n]+')
    rotate_pattern = re.compile(r'rotate:\s.+')
    xy_pattern = re.compile(r'xy:\s\d+,\s\d+')
    size_patter = re.compile(r'size:\s\d+,\s\d+')

    group = {}

    # 加载分割文件
    with open(file, 'r')as files:
        file_work = files.read()

    # 找出文件头，并去除
    pattern = re.compile(r'.+?\.png\nsize: \d+,\d+\nformat: \w+\nfilter: Linear,Linear\nrepeat: none')

    cuter = pattern.findall(file_work)

    cuter = cuter[0].replace('\\n', '\n')

    name = re.findall(r'.+\.png', cuter)[0]

    name = os.path.splitext(name)[0]

    file_work = file_work.replace(cuter, '')

    pattern = re.compile(r'\w+\n\s\s[ \S,]+\n\s\s[ \S,]+\n\s\s[ \S,]+\n\s\s[ \S,]+\n\s\s[ \S,]+\n\s\s[ \S,]+')

    bodies = pattern.findall(file_work)

    for body in bodies:
        mod_name = mod_pattern.findall(body)[0]
        group[mod_name] = {}
        group[mod_name]['rotate'] = rotate_pattern.findall(body)[0].replace('rotate: ', '')
        group[mod_name]['xy'] = [int(val) for val in re.findall(r'\d+', xy_pattern.findall(body)[0])]
        group[mod_name]['size'] = [int(val) for val in re.findall(r'\d+', size_patter.findall(body)[0])]

    return name, group


def build_part_model(tex: pygame.Surface, file: str):
    name, group = pos_spilt(file)
    group = spilt_tex(tex, group)

    return name, group


if __name__ == '__main__':
    print(math.degrees(math.atan(0.75)))
