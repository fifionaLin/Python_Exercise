#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 12:15:50 2020

@author: fiona
"""
# HW8_3 class練習：領養狗狗
import datetime

class Dog: # 類別Dog
    
    def __init__(self, name, height, weight, adopted_date): # 初始化
        self.name = name
        self.height = height
        self.weight = weight
        self.adopted_date = adopted_date # 用datetime形式
        self.dust = 0
        self.walk_count = 0
        self.longest_duration = 0
        self.last_walk_date = adopted_date # 用datetime形式
        self.is_small_dog = self.check_if_small_dog()
        
    def check_if_small_dog(self): # 判斷是否為小型犬，回傳 boolean 值
        if self.height > 60 or self.weight > 30: # 大型犬
            return False
        else: # 小型犬
            return True
    
    def walk(self, walk_date): # 散步過後，更新數據
        if self.is_small_dog:
            # 依據小型犬的灰塵累積效率更新累積灰塵量
            self.dust += 3
        else:
            # 依據大型犬的灰塵累積效率更新累積灰塵量
            self.dust += 2
        # 更新散步次數、最大散步間隔時間、最近散步日期
        self.walk_count += 1
        if (walk_date - self.last_walk_date).days > self.longest_duration:
            self.longest_duration = (walk_date - self.last_walk_date).days
        self.last_walk_date = walk_date
        
    def bathe(self): # 洗澡過後，更新數據
        # 更新累積灰塵量
        self.dust = 0
        
    def get_walk_frequency(self, today): # 計算散步頻率，並回傳頻率
        return self.walk_count / (today - self.adopted_date).days


class DogsHome: # 類別DogsHome：當前所擁有的狗們，一個 DogsHome 中有多隻 Dog
    
    def __init__(self): # 初始化
        self.dogs = []
        
    def add_dog(self, dog): # 增加Dog
        self.dogs.append(dog)
        
    def find_the_dog(self, name): # 用名字找到狗狗之家中你所要的狗
        for dog in self.dogs:
            if dog.name == name:
                return dog # 回傳此狗
            
    def remove_this_dog(self, name): # 狗換主人，移除此狗的資料
        for i in range(len(self.dogs)):
            if dog.name == name:
                self.dogs.pop(i)
                break
            
    def sort_by_priority(self): # 把狗狗之家中的狗依照優先序排
        self.dogs.sort(key=lambda x:x.name) # 名字開頭字母前的優先
        self.dogs.sort(key=lambda x:x.height, reverse=True) # 身高高的優先
        self.dogs.sort(key=lambda x:x.weight, reverse=True) # 體重重的優先
            
    def get_lowest_walk_frequency_dog(self, today): # 找出散步頻率最低的狗
        min_frequency = self.dogs[0].get_walk_frequency(today)
        get_index = 0
        for i in range(1,len(self.dogs)):
            # 散步頻率較低，則取代
            if self.dogs[i].get_walk_frequency(today) < min_frequency:
                min_frequency = self.dogs[i].get_walk_frequency(today)
                get_index = i
            elif self.dogs[i].get_walk_frequency(today) == min_frequency:
                # 散步頻率相同，大型犬優先
                if self.dogs[i].is_small_dog != self.dogs[get_index].is_small_dog:
                    if not self.dogs[i].is_small_dog:
                        min_frequency = self.dogs[i].get_walk_frequency(today)
                        get_index = i
        return self.dogs[get_index] # 回傳此狗
    
    def get_max_longest_duration_dog(self): # 找出最大散步間隔時間最長的狗
        max_longest_duration = self.dogs[0].longest_duration
        get_index = 0
        for i in range(1,len(self.dogs)):
            # 最大散步間隔較大，則取代
            if self.dogs[i].longest_duration > max_longest_duration:
                max_longest_duration = self.dogs[i].longest_duration
                get_index = i
            elif self.dogs[i].longest_duration == max_longest_duration:
                # 最大散步間隔相同，大型犬優先
                if self.dogs[i].is_small_dog != self.dogs[get_index].is_small_dog:
                    if not self.dogs[i].is_small_dog:
                        max_longest_duration = self.dogs[i].longest_duration
                        get_index = i
        return self.dogs[get_index] # 回傳此狗
    
    def get_max_dust_dog(self): # 找出累積灰塵量最多的狗
        max_dust = self.dogs[0].dust
        get_index = 0
        for i in range(1,len(self.dogs)):
            # 最大散步間隔較大，則取代
            if self.dogs[i].dust > max_dust:
                max_dust = self.dogs[i].dust
                get_index = i
            elif self.dogs[i].dust == max_dust:
                # 最大散步間隔相同，大型犬優先
                if self.dogs[i].is_small_dog != self.dogs[get_index].is_small_dog:
                    if not self.dogs[i].is_small_dog:
                        max_dust = self.dogs[i].dust
                        get_index = i
        return self.dogs[get_index] # 回傳此狗
        
        

# main
# 輸入資料
today_tmp = input().split('/')
today = datetime.datetime(int(today_tmp[0]), int(today_tmp[1]), int(today_tmp[2])) # 今日日期
task = input().split(',') # 指定的任務類別

dogshome = DogsHome() # 創建一個狗狗之家
while True:
    _str = input()
    if _str == "Done":
        break
    else:
        event = _str.split('|') # 要進行的事件
        # 領養新狗
        if event[0] == 'A':
            date = event[4].split('/') # 領養日期
            dog = Dog(event[1], int(event[2]), int(event[3]), datetime.datetime(int(date[0]), int(date[1]), int(date[2]))) # 創建一隻狗
            dogshome.add_dog(dog) # 新狗加入狗狗之家
        # 幫狗洗澡
        elif event[0] == 'B':
            dogshome.find_the_dog(event[1]).bathe() # 洗澡更改數據
        # 帶狗散步
        elif event[0] == 'W':
            date = event[2].split('/') # 散步日期
            dogshome.find_the_dog(event[1]).walk(datetime.datetime(int(date[0]), int(date[1]), int(date[2]))) # 散步更改數據
        # 狗換主人    
        elif event[0] == 'L':
            dogshome.remove_this_dog(event[1]) # 移除此狗的資料
    """        
    for d in dogshome.dogs:
        print(d.name, d.height, d.weight, d.dust, d.walk_count, d.longest_duration, d.last_walk_date.date())
        print(d.get_walk_frequency(today))"""

# 根據指定任務找出所要的狗狗
dogshome.sort_by_priority() # 先把狗狗之家中的狗依照優先序排好
if task[0] == 'TaskA': # 任務 a:找出名字為給定名稱的狗
    dog = dogshome.find_the_dog(task[1])
elif task[0] == 'TaskB': # 任務 b:找出散步頻率最低的狗
    dog = dogshome.get_lowest_walk_frequency_dog(today)    
elif task[0] == 'TaskC': # 任務 c:找出最大散步間隔時間最長的狗
    dog = dogshome.get_max_longest_duration_dog()    
elif task[0] == 'TaskD': # 任務 d:找出累積灰塵量最多的狗
    dog = dogshome.get_max_dust_dog()
# 輸出結果    
print(dog.name + "," + str(dog.height) + "," + str(dog.weight) + "," + str(dog.dust))
            
        
        