#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 10:47:15 2020

@author: fiona
"""
# HW7_1 在資料集中找出關鍵字的前後文
# /Users/fiona/Python_exercise/Gossiping-QA-Dataset.txt

import operator

# 接收輸入
file_rute = input()
keyword = input()

words = [] # 把檔案中的資料分段並去除空格存進words
with open(file=file_rute, mode='r', encoding='utf-8') as f:
    for line in f:
        _strs = line.split('\t')
        for _str in _strs:
            words.append(_str.strip())            


d_front = dict() # 以前一個字對應到其數量
d_back = dict() # 以後一個字對應到其數量
for word in words:
    word_f = '' # 搜尋過的
    word_b = word[0:] # 還沒搜尋過的
    check = word_b.find(keyword) # 在還沒搜尋過的部分找關鍵字
      
    while check != -1:
        position = len(word_f) + check # 關鍵字的確切index
            
        if position != 0: # 關鍵字不再開頭
            front = word[position-1:position]
            if front not in d_front:
                d_front[front] = 1
            else:
                d_front[front] += 1
        
        if position+len(keyword) != len(word): # 關鍵字不再結尾
            back = word[position+len(keyword):position+len(keyword)+1]
            if back not in d_back:
                d_back[back] = 1
            else:
                d_back[back] += 1
                
        word_f = word[0:position+1] # 更新搜尋過的
        word_b = word[position+1:] # 更新還沒搜尋過的     
        check = word_b.find(keyword) # 在還沒搜尋過的部分繼續找關鍵字


d_front_amount = dict() # 以出現頻率對應到前個字
d_back_amount = dict() # 以出現頻率對應到後個字
for key in d_front.keys():
    if d_front[key] not in d_front_amount:
        d_front_amount[d_front[key]] = []
    d_front_amount[d_front[key]].append(key)
for key in d_back.keys():
    if d_back[key] not in d_back_amount:
        d_back_amount[d_back[key]] = []
    d_back_amount[d_back[key]].append(key)

# 將頻率相同的字以字的內碼由大到小來排序
for value in d_front_amount.values():
    value.sort(reverse=True)
for value in d_back_amount.values():
    value.sort(reverse=True)

# 把頻率dict轉換成tuples，用tuples中第0項(頻率)由大到小排序
sorted_front_amount = sorted(d_front_amount.items(), key=operator.itemgetter(0), reverse=True)
sorted_back_amount = sorted(d_back_amount.items(), key=operator.itemgetter(0), reverse=True)

# 取出排序過後所有的‘前一個字’跟‘後一個字’
final_front_list = []
final_back_list = []
for item in sorted_front_amount:
    for i in range(len(item[1])):
        final_front_list.append(item[1][i])
for item in sorted_back_amount:
    for i in range(len(item[1])):
        final_back_list.append(item[1][i])

# 輸出結果
# 前一個字
print("熱門前一個字:")
if len(final_front_list) < 10: # 少於10個，輸出全部
    for front in final_front_list:
        print('{0}---{1}'.format(front, keyword))
else:
    for i in range(10): # 10個以上，只輸出10個
        print('{0}---{1}'.format(final_front_list[i], keyword))
# 後一個字
print("熱門下一個字:")
if len(final_back_list) < 10: # 少於10個，輸出全部
    for back in final_back_list:
        print('{0}---{1}'.format(keyword, back))
else:
    for i in range(10): # 10個以上，只輸出10個
        print('{0}---{1}'.format(keyword, final_back_list[i]))

