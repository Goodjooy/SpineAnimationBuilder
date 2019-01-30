import json
import os
import re

import pygame


def build_part_model(tex: pygame.Surface, file: str):
    mod_pattern = re.compile(r'^[^\n]+')
    rotate_pattern = re.compile(r'rotate:\s.+')
    xy_pattern = re.compile(r'xy:\s\d+,\s\d+')
    size_patter = re.compile(r'size:\s\d+,\s\d+')

    group = {}

    img = tex

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

    for var in group.keys():

        xy = group[var]['xy']
        size = group[var]['size']

        if group[var]['rotate'] == 'true':

            val = img.subsurface(pygame.Rect(xy, size[::-1]))
            val = pygame.transform.rotate(val, -90)
        else:
            val = img.subsurface(pygame.Rect(xy, size))

        group[var]['pic'] = val

    return name, group


if __name__ == '__main__':
    import math

    print(math.degrees(math.atan(0.75)))
