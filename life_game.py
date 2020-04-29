#!/usr/bin/env python3
# ­‐*­‐ coding: utf‐8 ­‐*-­

'''
@Author: Meyer
@Date: 2020-04-28 21:15:01
@LastEditTime: 2020-04-29 12:12:10
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /life_game/life_game.py
'''
import argparse
import time

from game_map import GameMap
from game_timer import GameTimer
from threading import Timer

class LifeGame(object):
    def __init__(self, map_rows, map_cols, life_init_ratio):
        """将在主程序中初始化实例""" 
        self.map_rows = map_rows
        self.map_cols = map_cols
        self.life_init_ratio = life_init_ratio
        self.game_map = GameMap(map_rows, map_rows)
        self.game_map.reset(life_init_ratio)

    def game_cycle(self):
        """
        进行一次游戏循环，将在此完成地图的更新
        将在计时器触发时被调用
        """ 
        temp = self.game_map
        (rows, cols) = temp.map.shape
        for i in range(rows):
            for j in range(cols):
                neighbors = temp.get_neighbor_count(i, j)
                if (neighbors >= 4 or neighbors == 1):
                    self.game_map.set(i, j, 0)
                elif (neighbors == 3):
                    self.game_map.set(i, j, 1)
                else:
                    continue
        self.print_map()

    
    def print_map(self):
        """由于暂时没有UI模块，因此先在逻辑模块进行地图的呈现"""
        # print(self.game_map)
        (rows, cols) = self.game_map.map.shape
        print("===================================================================================")
        for i in range(rows):
            for j in range(cols):
                print(self.game_map.map[i, j], end=' ')
            print("\n")



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--n_rows', type=int, default=5,
                        help='number of the rows of game map')
    parser.add_argument('--n_cols', type=int, default=5,
                        help='number of the column of game map')
    parser.add_argument('--int', type=int, default=1,
                        help='the interval of cycle of the game')
    parser.add_argument('--life_init_ratio', type=float, default=0.4,
                        help='the init_ratio  of the game')
    global args
    args = parser.parse_args()
    print(args)

    global game
    game = LifeGame(args.n_rows, args.n_cols, args.life_init_ratio)
    game.print_map()

    timer = GameTimer(args.int, game.game_cycle)
    timer.start()

