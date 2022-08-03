#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 00:42:20 2020

@author: fiona
"""
# HW7_2 電影及種類分析
# /Users/fiona/Python_exercise/u.item
# /Users/fiona/Python_exercise/u.genre

# 接收輸入
item_rute = input()
genre_rute = input()
movie_id = input()

item_list = []
genre_list = []
# 把檔案中的電影資料一行一行存進item_list
with open(file=item_rute, mode='r', encoding='ISO-8859-1') as f:
    for line in f:
        this_list = line.strip().split('|')
        item_list.append(this_list)

# 把檔案中的電影種類資料一行一行存進genre_list
with open(file=genre_rute, mode='r', encoding='utf-8') as f:
    for line in f:
        this_list = line.strip().split('|')
        genre_list.append(this_list)


movie_title = '' # 所要的電影名稱
get_genre_list = [] # 所要電影的種類

for item in item_list:
    if movie_id == item[0]:
        movie_title = item[1] # 用movie_id找到電影名稱
        
        for i in range(5,24):
            if item[i] == '1': # 找到所屬種類的編號
                genre_id = str(i-5)
                
                for genre in genre_list: 
                    if genre_id == genre[1]: # 找出此種類編號的名稱
                        get_genre_list.append(genre[0])


# 印出所要結果
if len(movie_title) == 0:
    print("No movie found.")
else:
    print('{0}: {1}'.format(movie_title, ', '.join(get_genre_list)))