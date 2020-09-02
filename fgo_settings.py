#!/usr/bin/python

"""general settings for fgo"""

import random
import sys
import time
import xlrd

import win32gui

import basic_function

"""dictionary of button"""
button_dict = {
    'A': 0x41,  # first character first skill
    'B': 0x42,  # first character second skill
    'C': 0x43,  # first character third skill
    'D': 0x44,  # second character first skill
    'E': 0x45,  # second character second skill
    'F': 0x46,  # second character third skill
    'G': 0x47,  # third character first skill
    'H': 0x48,  # third character second skill
    'I': 0x49,  # third character third skill
    'J': 0x4A,  # attack
    'K': 0x4B,  # first character noble phantasm
    'L': 0x4C,  # second character noble phantasm
    'M': 0x4D,  # third character noble phantasm
    'N': 0x4E,  # first card
    'O': 0x4F,  # second card
    'P': 0x50,  # third card
    'Q': 0x51,  # forth card
    'R': 0x52,  # fifth card
    'S': 0x53,  # master skill menu
    'T': 0x54,  # first master skill
    'U': 0x55,  # second master skill
    'V': 0x56,  # third master skill
    '1': 0x31,  # first enemy
    '2': 0x32,  # second enemy
    '3': 0x33,  # third enemy
    '4': 0x34,  # enter (right bottom)
    '5': 0x35,  # refresh list
    'up': 0x26,  # draw up
}


def rand_card(handle, delay_num):
    """choose 2 cards in 5 cards"""
    a = [button_dict['N'], button_dict['O'], button_dict['P'], button_dict['Q'], button_dict['R']]
    choice = random.sample(a, 2)
    basic_function.press_keyboard(handle, choice[0], 0.5 + delay_num)
    basic_function.press_keyboard(handle, choice[1], 1 + delay_num)
    return None


def continue_attack(handle, action, delay_num):
    """check whether continue attacking"""
    if not action:
        basic_function.press_keyboard(handle, button_dict['E'], 3 + delay_num)
    else:
        basic_function.press_keyboard(handle, button_dict['H'], 3 + delay_num)
    return None


def check_fight(handle, width, height, resolution):
    """check which side of the fight"""
    basic_function.get_bitmap(handle, width, height, resolution)
    basic_function.save_sliced_binarization_pic("img_check.bmp", (1280, 720), [5, 45, 860, 890])
    [min_val, max_val1, min_loc, max_loc, th, tw] = basic_function.template_matching('img_binarization.jpg',
                                                                                     'source/1.jpg',
                                                                                     0, 0)
    [min_val, max_val2, min_loc, max_loc, th, tw] = basic_function.template_matching('img_binarization.jpg',
                                                                                     'source/2.jpg',
                                                                                     0, 0)
    [min_val, max_val3, min_loc, max_loc, th, tw] = basic_function.template_matching('img_binarization.jpg',
                                                                                     'source/3.jpg',
                                                                                     0, 0)
    result = max(max_val1, max_val2, max_val3)
    if result < 0.75:
        print('Failed to enter the any side')
        sys.exit()
    else:
        if result == max_val1:
            return 1
        if result == max_val2:
            return 2
        if result == max_val3:
            return 3
        else:
            print('error occurred')
            return None


def check_apple(handle, width, height, resolution, state, delay_num):
    """check whether eat apple"""
    print('Checking whether to eat apple')
    basic_function.get_bitmap(handle, width, height, resolution)
    [min_val1, max_val1, min_loc1, max_loc1, th, tw] = basic_function.template_matching('img_check.bmp',
                                                                                        'source/apple.jpg',
                                                                                        (1280, 720), 0)
    [min_val2, max_val2, min_loc2, max_loc2, th, tw] = basic_function.template_matching('img_check.bmp',
                                                                                        'source/assist.jpg',
                                                                                        (1280, 720), 0)
    if max_val1 > 0.95:
        print("eat apple")
        if state:
            basic_function.press_keyboard(handle, button_dict['T'], 1 + delay_num)
            basic_function.press_keyboard(handle, button_dict['H'], 2 + delay_num)
        else:
            print("end loop")
            sys.exit()
    elif max_val2 > 0.95:
        print("don't need to eat apple")
        return None
    else:
        print("error occurred")
        sys.exit()

    return None


def check_character(handle, width, height, character, equipment, resolution, delay_num):
    """find character in assist"""
    basic_function.get_bitmap(handle, width, height, resolution)
    if character == str(0):
        print("don't need to find character")
        if equipment == str(0):
            print("don't need to find equipment")
            basic_function.press_keyboard(handle, button_dict['N'], 3 + delay_num)
            basic_function.press_keyboard(handle, button_dict['4'], 3 + delay_num)
            return None
        else:
            print("finding " + equipment)
            [min_val, max_val, min_loc, max_loc, th, tw] = basic_function.template_matching('img_check.bmp',
                                                                                            'source/' + equipment + '.jpg',
                                                                                            (1280, 720), 0)
            while 1:
                count = 0
                while max_val < 0.95 and count < 10:
                    count += 1
                    basic_function.press_keyboard(handle, button_dict['up'], 1.5 + delay_num)
                    basic_function.get_bitmap(handle, width, height, resolution)
                    [min_val, max_val, min_loc, max_loc, th, tw] = basic_function.template_matching('img_check.bmp',
                                                                                                    'source/' + equipment + '.jpg',
                                                                                                    (1280, 720), 0)
                if max_val >= 0.95:
                    break
                else:
                    time.sleep(10)
                    print('could not find ' + equipment + ', refresh')
                    basic_function.press_keyboard(handle, button_dict['5'], 1 + delay_num)
                    basic_function.press_keyboard(handle, button_dict['H'], 1 + delay_num)
            print('OK')
    else:
        print('finding ' + character)
        [min_val, max_val, min_loc, max_loc, th, tw] = basic_function.template_matching('img_check.bmp',
                                                                                        'source/' + character + '.jpg',
                                                                                        (1280, 720), 0)

        while 1:
            count = 0
            while max_val < 0.95 and count < 10:
                count += 1
                basic_function.press_keyboard(handle, button_dict['up'], 1.5 + delay_num)
                basic_function.get_bitmap(handle, width, height, resolution)
                [min_val, max_val, min_loc, max_loc, th, tw] = basic_function.template_matching('img_check.bmp',
                                                                                                'source/' + character + '.jpg',
                                                                                                (1280, 720), 0)
            if max_val >= 0.95:
                print('OK')
                if equipment == str(0):
                    print("don't need to find equipment")
                    break
                else:
                    print("checking " + equipment)
                    if max_loc[1] + th + 70 > 720:
                        print("equipment did not match")
                        continue
                    [min_val1, max_val1, min_loc1, max_loc1, th1, tw1] = basic_function.template_matching(
                        'img_check.bmp',
                        'source/' + equipment + '.jpg',
                        (1280, 720),
                        [max_loc[1] + th,
                         max_loc[
                             1] + th + 70,
                         max_loc[0] - 20,
                         max_loc[
                             0] + tw + 20])
                    if max_val1 >= 0.95:
                        break
                    else:
                        print("equipment did not match")
            else:
                time.sleep(10)
                print('could not find ' + character + ', refresh')
                basic_function.press_keyboard(handle, button_dict['5'], 1 + delay_num)
                basic_function.press_keyboard(handle, button_dict['H'], 1 + delay_num)
        print('OK')

    tl = max_loc
    br = (tl[0] + tw, tl[1] + th)

    point = [0, 0]
    point[0] = int((tl[0] + br[0]) / 2 / 1280 * width)
    point[1] = int((tl[1] + br[1]) / 2 / 720 * height)

    basic_function.press_mouse(handle, point, 3 + delay_num)
    basic_function.press_keyboard(handle, button_dict['4'], 3 + delay_num)
    return None


def read_strategy(handle, width, height, resolution, delay_num):
    wb = xlrd.open_workbook('strategy.xlsx')
    for battle in range(3):
        """
        if battle != check_fight(handle, width, height, resolution)-1:
            print("error occurred in fight " + str(battle+1))
            sys.exit()
        else:
            print("Start fight in side " + str(battle+1))
        """
        side = wb.sheet_by_name('Side' + str(battle + 1))
        for repeat in range(9):
            if side.cell(2 + repeat, 1).value != 1:
                continue
            else:
                if side.cell(2 + repeat, 2).value == 0:
                    basic_function.press_keyboard(handle, button_dict[chr(65 + repeat)], 3 + delay_num)
                elif side.cell(2 + repeat, 2).value > 6 or side.cell(2 + repeat, 2).value < 0:
                    print("error input")
                    sys.exit()
                elif side.cell(2 + repeat, 2).value < 4:
                    basic_function.press_keyboard(handle, button_dict[chr(65 + repeat)], 0.5 + delay_num)
                    basic_function.press_keyboard(handle, button_dict[chr(78 + int(side.cell(2 + repeat, 2).value))],
                                                  3 + delay_num)
                else:
                    basic_function.press_keyboard(handle, button_dict[chr(57 + int(side.cell(2 + repeat, 2).value))],
                                                  0.5 + delay_num)
                    basic_function.press_keyboard(handle, button_dict[chr(65 + repeat)], 3 + delay_num)

        for repeat in range(3):
            if side.cell(11 + repeat, 1).value != 1:
                continue
            else:
                basic_function.press_keyboard(handle, button_dict['S'], 0.5 + delay_num)
                if side.cell(11 + repeat, 2).value == 0:
                    basic_function.press_keyboard(handle, button_dict[chr(84 + repeat)], 3 + delay_num)
                elif side.cell(11 + repeat, 2).value > 4 or side.cell(11 + repeat, 2).value < 0:
                    print("error input")
                    sys.exit()
                else:
                    basic_function.press_keyboard(handle, button_dict[chr(84 + repeat)], 0.5 + delay_num)
                    basic_function.press_keyboard(handle, button_dict[chr(78 + int(side.cell(11 + repeat, 2).value))],
                                                  3 + delay_num)

        basic_function.press_keyboard(handle, button_dict['J'], 3 + delay_num)
        for repeat in range(3):
            if side.cell(15 + repeat, 1).value != 1:
                continue
            else:
                if side.cell(15 + repeat, 2).value == 0:
                    basic_function.press_keyboard(handle, button_dict[chr(75 + repeat)], 0.5 + delay_num)
                elif side.cell(15 + repeat, 2).value > 4 or side.cell(15 + repeat, 2).value < 0:
                    print("error input")
                    sys.exit()
                else:
                    basic_function.press_keyboard(handle, button_dict[chr(60 + int(side.cell(15 + repeat, 2).value))],
                                                  0.5 + delay_num)
                    basic_function.press_keyboard(handle, button_dict[chr(75 + repeat)], 0.5 + delay_num)

        rand_card(hwnd, delay_num)
        time.sleep(side.cell(18, 1).value)

    for repeat in range(5):
        basic_function.press_keyboard(handle, button_dict['4'], 1 + delay_num)
    print('battle finish')
    return None


if __name__ == '__main__':
    print('This script is based on "网易MuMu模拟器“')
    print('可以通过修改strategy.xlsx来实现刷本策略的改变，默认为满破宝石+冲莫豆爸')
    hwnd = basic_function.get_handle('命运-冠位指定 - MuMu模拟器')
    resolution = float(input("请先输入显示-缩放与布局-更改文本、应用等项目的大小下的分辨率比例大小（比如125%即输入1.25）："))
    left, bottom, right, top = win32gui.GetWindowRect(hwnd)
    hwnd_width = right - left
    hwnd_height = top - bottom

    repeat_num = int(input('请输入重复刷本的次数：'))
    apple = int(input('是否需要吃苹果？（1代表是，0代表不是）：'))

    character = input('请输入需要寻找的助战角色(现在提供的有CBA, kongming, merlin, nero, fox，不需要输入0)：')
    equipment = input('请输入助战角色身上带的概念礼装（现在提供的有贝拉丽莎（QP），红茶学妹（bondage），不需要输入0）：')

    wait_time = int(input('请输入从选人结束至第一面开始的预计时间（s）：'))
    delay_num = int(input('请输入释放技能延迟时间（由于有的模拟器存在卡顿，按键策略有时候会出错，若不存在卡顿可以设置为0，推荐存在一定卡顿的设置为1（s））：'))

    for i in range(repeat_num):
        check_character(hwnd, hwnd_width, hwnd_height, character, equipment, resolution, delay_num)
        time.sleep(wait_time)
        read_strategy(hwnd, hwnd_width, hwnd_height, resolution, delay_num)
        if i < repeat_num - 1:
            continue_attack(hwnd, True, delay_num)
            if apple == 1:
                check_apple(hwnd, hwnd_width, hwnd_height, resolution, True, delay_num)
            else:
                check_apple(hwnd, hwnd_width, hwnd_height, resolution, False, delay_num)
            time.sleep(6)
            print("···············")
        else:
            continue_attack(hwnd, False, delay_num)
            print("Loop terminated")
    sys.exit()
