# -*- coding: utf-8 -*-
import random
import pygame
import math
from pygame.locals import *

RGB = [(47, 79, 79), (84, 225, 159), (106, 90, 205), (0, 225, 225)]


def get_color():
    random.shuffle(RGB)
    return random.sample(RGB, 1)[0]


class Marquee(object):
    def __init__(self):
        # 长度
        self.length = 15
        self.flash_index = 0
        self.h_flash_index = 0
        self.w_up_start_pos, self.w_down_start_pos = (5, 5), (5, 395)
        self.h_left_start_pos, self.h_right_start_pos = (5, 5), (795, 5)
        self.w_up_pos_group, self.w_down_pos_group, self.h_left_pos_group, self.h_right_pos_group = [
                                                                                                        self.w_up_start_pos], [
                                                                                                        self.w_down_start_pos], \
                                                                                                    [
                                                                                                        self.h_left_start_pos], [
                                                                                                        self.h_right_start_pos]

    def get_pos_group(self, *args, **kwargs):
        # 生成上边,下边框灯条坐标
        w_count = screen.get_width() / self.length
        for i in xrange(1, w_count - 1):
            self.w_up_pos_group.append((self.w_up_pos_group[i - 1][0] + self.length + 5 + 5, 5))
            self.w_down_pos_group.append((self.w_up_pos_group[i - 1][0] + self.length + 5 + 5, 395))
        # 生成左边,右边框灯条坐标
        h_count = screen.get_height() / self.length
        for i in xrange(1, h_count):
            self.h_left_pos_group.append((5, self.h_left_pos_group[i - 1][1] + self.length + 5))
            self.h_right_pos_group.append((795, self.h_right_pos_group[i - 1][1] + self.length + 5))

    def set_flash(self, *args, **kwargs):
        self.flash_index += 0.1
        self.h_flash_index += 0.1
        if int(self.flash_index) == screen.get_width() / self.length:
            self.flash_index = 0
        if int(self.h_flash_index) == screen.get_height() / self.length:
            self.h_flash_index = 0

    @staticmethod
    def get_color(*args, **kwargs):
        random.shuffle(RGB)
        return random.sample(RGB, 1)[0]

    def draw(self, *args, **kwargs):
        screen, bar_color, = args
        color = (255, 255, 255)
        for index, pos in enumerate(self.w_up_pos_group):
            if index == int(self.flash_index):
                color = bar_color
            # 上边框 每个间距5px
            pygame.draw.line(screen, color, pos, (pos[0] + 5, pos[1]), 5)
            # 下边框
            pygame.draw.line(screen, color, (self.w_down_pos_group[index][0], self.w_down_pos_group[index][1]),
                             (self.w_down_pos_group[index][0] + 5, self.w_down_pos_group[index][1]), 5)
        color = (255, 255, 255)
        # 开始绘制左边和右边的灯带
        for index, pos in enumerate(self.h_left_pos_group):
            if index == int(self.h_flash_index):
                color = bar_color
            pygame.draw.line(screen, color, pos, (pos[0], pos[1] + 5), 5)
            pygame.draw.line(screen, color, (self.h_right_pos_group[index][0], self.h_right_pos_group[index][1]),
                             (self.h_right_pos_group[index][0], self.h_right_pos_group[index][1] + 5), 5)


class TV(object):
    def __init__(self):
        pass

    def draw(self, *args, **kwargs):
        screen, tv_color = args
        pygame.draw.rect(screen, tv_color,
                         (screen.get_width() / 2 - 300, screen.get_height() / 2 - 50, 150, 100), 5)
        self.draw_face(screen, tv_color)
        self.draw_leg(screen, tv_color)
        self.draw_eyes(screen, tv_color)
        self.draw_antenna(screen, tv_color)

    def draw_face(self, *args, **kwargs):
        screen, tv_color = args
        pygame.draw.arc(screen, tv_color, (154, 190, 25, 25), math.pi, math.pi * 2, 5)
        pygame.draw.arc(screen, tv_color, (174, 190, 25, 25), math.pi, math.pi * 2, 5)

    def draw_leg(self, *args, **kwargs):
        screen, tv_color = args
        pygame.draw.arc(screen, tv_color, (120, 240, 25, 25), math.pi, math.pi * 2, 5)
        pygame.draw.arc(screen, tv_color, (205, 240, 25, 25), math.pi, math.pi * 2, 5)

    def draw_eyes(self, *args, **kwargs):
        screen, tv_color = args
        pygame.draw.line(screen, tv_color, (125, 175), (155, 170))
        pygame.draw.line(screen, tv_color, (195, 170), (227, 175))

    def draw_antenna(self, *args, **kwargs):
        screen, tv_color = args
        pygame.draw.line(screen, tv_color, (155, 150), (145, 135))
        pygame.draw.line(screen, tv_color, (195, 150), (205, 135))


class Logo(object):
    def __init__(self):
        self.font = ""

    # 绘画bilibili文字
    def draw(self, *args, **kwargs):
        font = pygame.font.SysFont(self.font, 200)
        return font


if __name__ == '__main__':
    # 初始框架
    pygame.init()
    screen = pygame.display.set_mode((800, 400), 0, 32)
    pygame.display.set_caption("蹦迪小电视1.0".decode('utf-8'))

    # 绘制文字
    logo = Logo()
    font = logo.draw()
    # 绘制小电视
    tv = TV()
    # 跑马灯
    marquee = Marquee()
    # 初始化灯条位置
    marquee.get_pos_group()
    # 主循环
    while True:
        # 渲染灯条
        # 为灯条选取一个随机颜色
        bar_color = Marquee.get_color()
        marquee.draw(screen, bar_color)
        marquee.set_flash()
        # 获取随机颜色
        tv_color = get_color()
        tv.draw(screen, tv_color)
        logo_color = get_color()
        logo_txt_surface = font.render("bilibili", True, logo_color)
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        screen.blit(logo_txt_surface, (screen.get_width() / 2 - 80, screen.get_height() / 2 - 60))
        pygame.display.update()
