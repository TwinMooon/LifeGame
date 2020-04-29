#!/usr/bin/env python3
# ­‐*­‐ coding: utf‐8 ­‐*-­

'''
@Author: Meyer
@Date: 2020-04-28 21:14:46
@LastEditTime: 2020-04-29 12:12:38
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /life_game/game_map.py
'''
import random
import math
import numpy as np


class GameMap(object):
    def __init__(self, rows, columns):
        """地图将在逻辑模块进行初始化"""
        self.rows = rows
        self.columns = columns
        self.map = np.zeros((rows, columns), dtype=int)

    def reset(self, life_ratio):
        """重置地图并按life_ratio随机地填充一些活细胞"""
        self.map[:,:] = 0
        counts = math.floor(life_ratio * self.rows * self.columns)
        for i in range(counts):
            x = random.randint(0, self.rows - 1)
            y = random.randint(0, self.columns - 1)
            self.set(x, y, 1)
            

    def get_neighbor_count(self, row, col):
        """地图上一个方格周围活细胞数是游戏逻辑里的重要数据"""
        # 首先在上下左右各加全0️行(列)
        v_extention_vector = np.zeros(self.map.shape[1], dtype=int)
        map_extention = np.vstack((self.map, v_extention_vector))
        map_extention = np.vstack((v_extention_vector, map_extention))
        
        h_extention_vector = np.zeros(map_extention.shape[0], dtype=int)
        h_extention_vector = np.expand_dims(h_extention_vector, axis=0)
        h_extention_vector = h_extention_vector.T
        map_extention = np.hstack((h_extention_vector, map_extention))
        map_extention = np.hstack((map_extention, h_extention_vector))
        
        # print(self.map)
        # print(map_extention)
        
        # 取出以row+1, col+1为核心的9个单元
        neighbor = map_extention[row : row + 3, col : col + 3]
        neighbor[1,1] = 0
        return neighbor.sum()

    def set(self, row, col, val):
        """当游戏进行中，需要常常更新地图上方格的状态"""
        self.map[row,col] = val
    
    def get(self, row, col):    
        """当需要将游戏状态呈现给用户时，就需要获取地图上方格的状态"""
        return self.map[row, col]

if __name__ == "__main__":
    game_map = GameMap(5, 5)
    game_map.reset(0.4)
    # print(game_map.map)
    print(game_map.get_neighbor_count(3,3))
