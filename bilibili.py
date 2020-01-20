# -*- coding: utf-8 -*-
import math
import random
import threading
import wave

import pyaudio
import pygame
from pygame.locals import *

from color_matching_table import Ctrl, Shift, Alt, Space
from color_matching_table import color_table

RGB = [(47, 79, 79), (84, 225, 159), (106, 90, 205), (0, 225, 225)]
# 定义数据流块
CHUNK = 1024
# 闪烁频率
FREQUENCY = 0.01
# 电视以及文本颜色
COLOR = (255, 255, 255)

# 文本
TXT = "bilibili"
# 跑马灯颜色
MARQUEE_COLOR = (255, 255, 255)


def get_color():
    random.shuffle(RGB)
    return random.sample(RGB, 1)[0]


def arc(*args, **kwargs):
    screen, color, pos = args
    pygame.draw.arc(screen, color, pos, math.pi, math.pi * 2, 5)


def line(*args, **kwargs):
    screen, color, pos = args
    pygame.draw.line(screen, color, pos[0], pos[1], 5)


def get_cofing(*args, **kwargs):
    key, = args
    return color_table[key]


def play(*args, **kwargs):
    pt = PlayThread((r"Music/{}.wav".format(args[0])))
    pt.start()


class PlayThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(PlayThread, self).__init__()
        self.__args = args

    def run(self):
        file_name, = self.__args
        wf = wave.open(file_name, 'rb')
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
        data = wf.readframes(CHUNK)
        while data != b'':
            stream.write(data)
            data = wf.readframes(CHUNK)
        stream.stop_stream()
        stream.close()
        p.terminate()


class Marquee(object):
    def __init__(self):
        self.length = 15
        self.group = []
        self.flash_group = [0, 4, 8, 12]
        '''初始化边框位置'''
        # 上边框
        for i in range(12, 780, 20):
            start_pos = (i, 5)
            end_pos = (i + self.length, 5)
            self.group.append((start_pos, end_pos))
        # 右边框
        for i in range(3, 400, 20):
            start_pos = (792, i)
            end_pos = (792, i + self.length)
            self.group.append((start_pos, end_pos))
        # 下边框
        for i in range(780, 19, -20):
            start_pos = (i, 395)
            end_pos = (i - self.length, 395)
            self.group.append((start_pos, end_pos))
        # 左边框
        for i in range(400, 3, -20):
            start_pos = (7, i)
            end_pos = (7, i - self.length)
            self.group.append((start_pos, end_pos))

    def set_flash(self, *args, **kwargs):
        for i in xrange(len(self.flash_group)):
            self.flash_group[i] = self.flash_group[i] + FREQUENCY
            if int(self.flash_group[i]) != len(self.group) - 1:
                continue
            self.flash_group[i] = 0

    def draw(self, *args, **kwargs):
        screen, bar_color = args
        for index, pos in enumerate(self.group):
            tag = True
            for flash_index in self.flash_group:
                if index == int(flash_index):
                    tag = False
                    line(screen, bar_color, pos)
                    break
            if tag:
                line(screen, MARQUEE_COLOR, pos)


class TV(object):
    def __init__(self):
        self.border_pos = (screen.get_width() / 2 - 300, screen.get_height() / 2 - 50, 150, 100)
        self.face_left_pos = (154, 190, 25, 25)
        self.face_right_pos = (174, 190, 25, 25)

        self.leg_left_pos = (120, 240, 25, 25)
        self.leg_right_pos = (205, 240, 25, 25)

        self.eye_left_pos = ((125, 175), (155, 170))
        self.eye_right_pos = (195, 170), (227, 175)

        self.antenna_left_pos = ((155, 150), (145, 135))
        self.antenna_right_pos = ((195, 150), (205, 135))

    def draw(self, *args, **kwargs):
        screen, color = args
        pygame.draw.rect(screen, color, self.border_pos, 5)
        arc(screen, color, self.face_left_pos)
        arc(screen, color, self.face_right_pos)

        arc(screen, color, self.leg_left_pos)
        arc(screen, color, self.leg_right_pos)

        line(screen, color, self.eye_left_pos)
        line(screen, color, self.eye_right_pos)

        line(screen, color, self.antenna_left_pos)
        line(screen, color, self.antenna_right_pos)


class Text(object):
    def __init__(self, font_type=""):
        self.font_type = font_type

    def create(self, *args, **kwargs):
        return pygame.font.SysFont(self.font_type, 200)


if __name__ == '__main__':
    # 初始框架
    pygame.init()
    screen = pygame.display.set_mode((800, 400), 0, 32)
    pygame.display.set_caption("蹦迪小电视1.0".decode('utf-8'))

    # 初始化游戏
    txt = Text()
    txt_obj = txt.create()
    tv = TV()
    marquee = Marquee()

    # 主循环
    while True:
        color = COLOR
        bar_color = get_color()
        marquee.draw(screen, bar_color)
        marquee.set_flash()
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                print event.key
                # A
                if event.key == 54:
                    if Shift:
                        # A2
                        print "2"
                        play("a54")
                    elif Ctrl:
                        # A3
                        print "3"
                        play("a69")
                    elif Alt:
                        # A5
                        play("74")
                    elif Space:
                        # A6
                        play("66")
                    else:
                        print 4
                        # A4
                        play("a80")

                # B
                if event.key == 55:
                    if Shift:
                        # B2
                        print "2"
                        play("a55")
                    elif Ctrl:
                        # B3
                        print "3"
                        play("a82")
                    elif Alt:
                        # B5
                        play("75")
                    elif Space:
                        # B6
                        play("78")
                    else:
                        print 4
                        # B4
                        play("a65")
                # C
                if event.key == 49:
                    if Shift:
                        # C2
                        print "2"
                        play("a49")
                    elif Ctrl:
                        # C3
                        print "3"
                        play("a56")
                    elif Alt:
                        # C5
                        play("a83")
                    elif Space:
                        # C6
                        play("76")
                    else:
                        print 4
                        # C4
                        play("a84")
                # D2
                if event.key == 50:
                    if Shift:
                        # D2
                        print "2"
                        play("a50")
                    elif Ctrl:
                        # D3
                        print "3"
                        play("a57")
                    elif Alt:
                        # D5
                        play("a68")
                    elif Space:
                        # D6
                        play("90")
                    else:
                        print 4
                        # D4
                        play("a89")
                # E2
                if event.key == 51:
                    if Shift:
                        # E2
                        print "2"
                        play("a51")
                    elif Ctrl:
                        # E3
                        print "3"
                        play("a48")
                    elif Alt:
                        # E5
                        play("a70")
                    elif Space:
                        # E6
                        play("88")
                    else:
                        print 4
                        # E4
                        play("a85")
                # F2
                if event.key == 52:
                    if Shift:
                        # F2
                        print "2"
                        play("a52")
                    elif Ctrl:
                        # F3
                        print "3"
                        play("a81")
                    elif Alt:
                        # F5
                        play("a71")
                    elif Space:
                        # F6
                        play("67")
                    else:
                        print 4
                        # F4
                        play("a73")
                # G2
                if event.key == 53:
                    if Shift:
                        # G2
                        print "2"
                        play("a53")
                    elif Ctrl:
                        # G3
                        print "3"
                        play("a87")
                    elif Alt:
                        # G5
                        play("a72")
                    elif Space:
                        # G6
                        play("86")
                    else:
                        print 4
                        # G4
                        play("a79")

                if event.key ==pygame.K_LSHIFT:
                    Ctrl= False
                    Alt = False
                    Shift = True
                if event.key == 306:
                    Shift =False
                    Alt = False
                    Ctrl = True
                if event.key == 308:
                    Shift = False
                    Ctrl = False
                    Alt = True
                if event.key == 32:
                    Space = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT:
                    Shift = False
                if event.key == 306:
                    Ctrl = False
                if event.key == 308:
                    Alt = False
                if event.key == 32:
                    Space = False
            tv.draw(screen, color)
            txt_surface = txt_obj.render(TXT, True, color)
            screen.blit(txt_surface, (screen.get_width() / 2 - 80, screen.get_height() / 2 - 60))
        pygame.display.update()
