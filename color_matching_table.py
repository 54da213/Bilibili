# -*- coding: utf-8 -*-

'''
key  键盘码
valeu 0 颜色码 1音符码
'''
color_table = {49: ((255, 255, 0), 14),
               97: ((84, 225, 159), 21),
               100: ((106, 90, 205), 22),
               115: ((0, 225, 225), 31)}

# 1-7 Do	Re	Mi	Fa	Sol	La	Si
note = {1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False}

Shift = False
Ctrl = False
Alt = False
Space = False

minor = {"q": False, "w": False, "e": False, "r": False, "t": False}
