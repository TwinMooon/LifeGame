#!/usr/bin/env python3
# ­‐*­‐ coding: utf‐8 ­‐*-­

'''
@Author: Meyer
@Date: 2020-04-28 21:15:15
@LastEditTime: 2020-04-29 12:12:26
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /life_game/game_timer.py
'''
from threading import Timer

class GameTimer(Timer):
#     def __init__(self, trigger, interval):
#         """将在主程序中初始化实例
#         计时器以interval秒的频率触发
#         trigger是个函数，计时器被触发时调用该函数                  
#         """ 
#         self.trigger = trigger
#         self.interval = interval
#         self.timer = Timer(self.interval, self.trigger)
    
    def run(self):
        try:
            while not self.finished.is_set():
                self.function(*self.args, **self.kwargs)
                self.finished.wait(self.interval)
        except KeyboardInterrupt:
            exit(0)
        

    # def start(self):
    #     """启动计时器，之后将以interval秒的间隔持续触发"""
    #     try :
    #         self.timer.start()
    #     except KeyboardInterrupt:
    #         exit(0)
