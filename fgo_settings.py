#!/usr/bin/python

"""general settings for fgo"""

import basic_function
import win32gui
import random
import time
import sys

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


def rand_card(handle):
    """choose 2 cards in 5 cards"""
    a = [button_dict['N'], button_dict['O'], button_dict['P'], button_dict['Q'], button_dict['R']]
    choice = random.sample(a, 2)
    basic_function.press_keyboard(handle, choice[0], 0.5)
    basic_function.press_keyboard(handle, choice[1], 1)
    return None


def fight_bone(handle):
    """battle process for bone hunting"""
    # first map
    basic_function.press_keyboard(handle, button_dict['A'], 3)
    basic_function.press_keyboard(handle, button_dict['J'], 3)
    basic_function.press_keyboard(handle, button_dict['K'], 0.5)
    rand_card(handle)
    time.sleep(27)

    # second map
    basic_function.press_keyboard(handle, button_dict['B'], 3)
    basic_function.press_keyboard(handle, button_dict['J'], 3)
    basic_function.press_keyboard(handle, button_dict['K'], 0.5)
    rand_card(handle)
    time.sleep(30)

    # third map
    basic_function.press_keyboard(handle, button_dict['2'], 0.5)
    basic_function.press_keyboard(handle, button_dict['E'], 3)
    basic_function.press_keyboard(handle, button_dict['F'], 3)
    basic_function.press_keyboard(handle, button_dict['G'], 0.5)
    basic_function.press_keyboard(handle, button_dict['P'], 3)
    basic_function.press_keyboard(handle, button_dict['H'], 3)
    basic_function.press_keyboard(handle, button_dict['I'], 0.5)
    basic_function.press_keyboard(handle, button_dict['P'], 3)
    basic_function.press_keyboard(handle, button_dict['S'], 0.5)
    basic_function.press_keyboard(handle, button_dict['U'], 0.5)
    basic_function.press_keyboard(handle, button_dict['P'], 3)
    basic_function.press_keyboard(handle, button_dict['J'], 3)
    basic_function.press_keyboard(handle, button_dict['L'], 0.5)
    rand_card(handle)
    time.sleep(25)
    for i in range(5):
        basic_function.press_keyboard(handle, button_dict['4'], 1)
    print('battle finish')
    return None


def lancelot_wcba(handle):
    """battle process for mad lancelot with 2 cba"""
    # first map
    basic_function.press_keyboard(handle, button_dict['D'], 0.5)
    basic_function.press_keyboard(handle, button_dict['O'], 3)
    basic_function.press_keyboard(handle, button_dict['G'], 0.5)
    basic_function.press_keyboard(handle, button_dict['O'], 3)
    basic_function.press_keyboard(handle, button_dict['S'], 0.5)
    basic_function.press_keyboard(handle, button_dict['V'], 0.5)
    basic_function.press_keyboard(handle, button_dict['O'], 3)
    basic_function.press_keyboard(handle, button_dict['J'], 3)
    basic_function.press_keyboard(handle, button_dict['K'], 0.5)
    rand_card(handle)
    time.sleep(27)

    # second map
    basic_function.press_keyboard(handle, button_dict['C'], 3)
    basic_function.press_keyboard(handle, button_dict['F'], 0.5)
    basic_function.press_keyboard(handle, button_dict['O'], 3)
    basic_function.press_keyboard(handle, button_dict['J'], 3)
    basic_function.press_keyboard(handle, button_dict['K'], 0.5)
    rand_card(handle)
    time.sleep(30)

    # third map
    basic_function.press_keyboard(handle, button_dict['I'], 0.5)
    basic_function.press_keyboard(handle, button_dict['O'], 3)
    basic_function.press_keyboard(handle, button_dict['E'], 3)
    basic_function.press_keyboard(handle, button_dict['H'], 3)
    basic_function.press_keyboard(handle, button_dict['S'], 0.5)
    basic_function.press_keyboard(handle, button_dict['T'], 0.5)
    basic_function.press_keyboard(handle, button_dict['O'], 3)
    basic_function.press_keyboard(handle, button_dict['J'], 3)
    basic_function.press_keyboard(handle, button_dict['K'], 0.5)
    rand_card(handle)
    time.sleep(25)
    for i in range(5):
        basic_function.press_keyboard(handle, button_dict['4'], 1)
    print('battle finish')
    return None


def atalanta_wcba(handle):
    """battle process for atalanta with 2 cba"""
    # first map
    basic_function.press_keyboard(handle, button_dict['D'], 0.5)
    basic_function.press_keyboard(handle, button_dict['O'], 3)
    basic_function.press_keyboard(handle, button_dict['G'], 0.5)
    basic_function.press_keyboard(handle, button_dict['O'], 3)
    basic_function.press_keyboard(handle, button_dict['C'], 3)
    basic_function.press_keyboard(handle, button_dict['J'], 3)
    basic_function.press_keyboard(handle, button_dict['K'], 0.5)
    rand_card(handle)
    time.sleep(24)

    # second map
    basic_function.press_keyboard(handle, button_dict['F'], 0.5)
    basic_function.press_keyboard(handle, button_dict['O'], 3)
    basic_function.press_keyboard(handle, button_dict['J'], 3)
    basic_function.press_keyboard(handle, button_dict['K'], 0.5)
    rand_card(handle)
    time.sleep(24)

    # third map
    basic_function.press_keyboard(handle, button_dict['A'], 3)
    basic_function.press_keyboard(handle, button_dict['I'], 0.5)
    basic_function.press_keyboard(handle, button_dict['O'], 3)
    basic_function.press_keyboard(handle, button_dict['E'], 3)
    basic_function.press_keyboard(handle, button_dict['H'], 3)
    basic_function.press_keyboard(handle, button_dict['S'], 0.5)
    basic_function.press_keyboard(handle, button_dict['U'], 0.5)
    basic_function.press_keyboard(handle, button_dict['O'], 3)
    basic_function.press_keyboard(handle, button_dict['J'], 3)
    basic_function.press_keyboard(handle, button_dict['K'], 0.5)
    rand_card(handle)
    time.sleep(22)
    for i in range(5):
        basic_function.press_keyboard(handle, button_dict['4'], 1)
    print('battle finish')
    return None


def charlotte(handle):
    """battle in charlotte to get dust"""
    # first map
    basic_function.press_keyboard(handle, button_dict['A'], 3)
    basic_function.press_keyboard(handle, button_dict['B'], 3)
    basic_function.press_keyboard(handle, button_dict['F'], 3)
    basic_function.press_keyboard(handle, button_dict['J'], 3)
    basic_function.press_keyboard(handle, button_dict['K'], 0.5)
    rand_card(handle)
    time.sleep(24)

    # second map
    basic_function.press_keyboard(handle, button_dict['C'], 3)
    basic_function.press_keyboard(handle, button_dict['G'], 0.5)
    basic_function.press_keyboard(handle, button_dict['O'], 3)
    basic_function.press_keyboard(handle, button_dict['H'], 3)
    basic_function.press_keyboard(handle, button_dict['I'], 3)
    basic_function.press_keyboard(handle, button_dict['J'], 3)
    basic_function.press_keyboard(handle, button_dict['K'], 0.5)
    rand_card(handle)
    time.sleep(24)

    # third map
    basic_function.press_keyboard(handle, button_dict['D'], 3)
    basic_function.press_keyboard(handle, button_dict['S'], 0.5)
    basic_function.press_keyboard(handle, button_dict['U'], 0.5)
    basic_function.press_keyboard(handle, button_dict['P'], 3)
    basic_function.press_keyboard(handle, button_dict['J'], 3)
    basic_function.press_keyboard(handle, button_dict['L'], 0.5)
    rand_card(handle)
    time.sleep(22)
    for i in range(5):
        basic_function.press_keyboard(handle, button_dict['4'], 1)
    print('battle finish')
    return None


def check_apple(handle, width, height):
    """check whether eat apple"""
    basic_function.press_keyboard(handle, button_dict['M'], 2)
    print('Checking whether to eat apple')
    basic_function.get_bitmap(handle, width, height)
    [min_val1, max_val1, min_loc1, max_loc1] = basic_function.template_matching(handle, width, height, 'apple.bmp',
                                                                                (821, 462))
    [min_val2, max_val2, min_loc2, max_loc2] = basic_function.template_matching(handle, width, height, 'assist.bmp',
                                                                                (821, 462))
    if max_val1 > 0.95:
        print("eat apple")
        basic_function.press_keyboard(handle, button_dict['T'], 1)
        basic_function.press_keyboard(handle, button_dict['H'], 2)
    elif max_val2 > 0.95:
        print("don't need to eat apple")
        return None
    else:
        print("error occurred")
        sys.exit()

    return None


def check_character(handle, width, height, character):
    """find CBA in assist"""
    basic_function.get_bitmap(handle, width, height)
    print('finding ' + character)
    [min_val, max_val, min_loc, max_loc] = basic_function.template_matching(handle, width, height,
                                                                            character, (821, 462))
    th = 91
    tw = 105

    while max_val < 0.95:
        count = 0
        while max_val < 0.95 and count < 10:
            count += 1
            basic_function.press_keyboard(handle, button_dict['up'], 1.5)
            basic_function.get_bitmap(handle, width, height)
            [min_val, max_val, min_loc, max_loc] = basic_function.template_matching(handle, width, height,
                                                                                    character, (821, 462))
        if max_val >= 0.95:
            break
        else:
            time.sleep(10)
            print('could not find ' + character + ', refresh')
            basic_function.press_keyboard(handle, button_dict['5'], 1)
            basic_function.press_keyboard(handle, button_dict['H'], 1)
    print('OK')

    tl = max_loc
    br = (tl[0] + tw, tl[1] + th)

    point = [0, 0]
    point[0] = int((tl[0] + br[0]) / 2 / 821 * width)
    point[1] = int((tl[1] + br[1]) / 2 / 462 * height)

    basic_function.press_mouse(handle, point, 3)
    basic_function.press_keyboard(handle, button_dict['4'], 22)
    return None


if __name__ == '__main__':
    hwnd = basic_function.get_handle('命运-冠位指定 - MuMu模拟器')
    left, bottom, right, top = win32gui.GetWindowRect(hwnd)
    width = right - left
    height = top - bottom

    basic_function.get_bitmap(hwnd, width, height)

    for i in range(5):
        check_apple(hwnd, width, height)
        check_character(hwnd, width, height, 'kongming_bondage.bmp')
        charlotte(hwnd)
        time.sleep(6)
        print("···············")
    sys.exit()
