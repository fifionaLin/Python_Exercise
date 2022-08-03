#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 20:43:52 2020

@author: fiona
"""

# Practice 1
"""
假設你現在有一些電影的資訊，包含： 片名、發行年、導演、票房
將電影視為一個 Class，每部電影會擁有自己的資訊

1.請試著建立 class Movie 和它的 __init__()
必須包含:
▪ name:片名(str)
▪ year:發行年(int)
▪ director:導演(str)
▪ box:票房(list of int)

2.請試著為 class Movie 定義兩個 methods
▪box_office()回傳總票房
▪is_earlier_than(other_movie) 判斷該電影是否較早發行
"""

class Movie:
    
    def __init__(self, name, year, director, box):
        self.name = str(name)
        self.year = int(year)
        self.director = str(director)
        self.box = list(box)
        
    def box_office(self):
        sum_box = 0
        for box in self.box:
            sum_box += int(box)
        return "$" + str(sum_box) + " millions"
    
    def is_earlier_than(self, other_movie):
        if self.year < other_movie.year:
            return True
        else:
            return False
        

frozen = Movie('Frozen', 2013, 'Jennifer', [1000, 200])
lionKing = Movie('Lion King', 1994, 'Robert Ralph', [4000, 500])
print(frozen.year) # 2013
print(frozen.box) # [1000, 200]
print(lionKing.director)
print(frozen.box_office()) # $1200 millions
print(lionKing.box_office())
print(frozen.is_earlier_than(lionKing)) # False
print(lionKing.is_earlier_than(frozen))


# Practice 2
"""
根據資料，請畫出各地一週降雨機率折線圖
            Mon. Tues. Wed. Thur. Fri. Sat. Sun.
Taipei      80   60    70   30    30   40   30
Taichung    60   50    30   10    20   10   40
Tainan      20   10     0   10    10   20   30
"""
import matplotlib.pyplot as py

month = ['Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
taipei = [80, 60, 70, 30, 30, 40, 30]
taichung = [60, 50, 30, 10, 20, 10, 40]
tainan = [20, 10, 0, 10, 10, 20, 30]

py.plot(month, taipei, label='Taipei')
py.plot(month, taichung, label='Taichung')
py.plot(month, tainan, label='Tainan')
py.xlabel("Day")
py.ylabel("Probability(%)")
py.title("Probability of Raining")
py.legend(loc="upper right")

py.show()

