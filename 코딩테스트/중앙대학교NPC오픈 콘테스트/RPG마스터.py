# !/usr/bin/env Python
# coding=utf-8
import sys

hp_yong, atk_yong, hp_ma, atk_ma = map(int,sys.stdin.readline().rstrip().split())
p, s = map(int,sys.stdin.readline().rstrip().split())

count_ma = hp_yong // atk_ma if hp_yong % atk_ma == 0 else hp_yong // atk_ma + 1
count_yong = hp_ma // atk_yong if hp_ma % atk_yong == 0 else hp_ma // atk_yong + 1


if count_yong >= count_ma:
    print('gg')
else:

    cur_hp_yong = hp_yong - atk_ma * count_yong
    new_hp_ma = hp_ma - atk_yong * count_yong + s

    new_count_yong = new_hp_ma // atk_yong if new_hp_ma % atk_yong == 0 else new_hp_ma // atk_yong + 1
    new_count_ma = cur_hp_yong // atk_ma if cur_hp_yong % atk_ma == 0 else cur_hp_yong // atk_ma + 1

    if new_count_yong <= new_count_ma:
        print("Victory!")
    else:
        print("gg")



