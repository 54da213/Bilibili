# -*- coding: utf-8 -*-
import random
import pygame
import math
from pygame.locals import *

RGB = [(47, 79, 79), (84, 225, 159), (106, 90, 205), (0, 225, 225)]


def get_color():
    random.shuffle(RGB)
    return random.sample(RGB, 1)[0]


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
    print(pygame.font.get_fonts())
    # 主循环
    while True:
        # 获取随机颜色
        tv_color = get_color()
        # 绘制小电视
        tv = TV()
        tv.draw(screen, tv_color)
        logo_color = get_color()
        logo_txt_surface = font.render("bilibili", True, logo_color)
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        screen.blit(logo_txt_surface, (screen.get_width() / 2 - 80, screen.get_height() / 2 - 60))
        pygame.display.update()
