#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 07:50:49 2020

@author: fiona
"""

#Practice 1
"""
我們想知道在歌詞中有那些頻繁出現的字，請你計算每個字出現的次數並輸出。
"""

lyrics = input("輸入一串文字，將會列出各個字元出現次數：")
d = dict()

for i in lyrics:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
 
print(d)
print(sorted(d, key=lambda x: d[x], reverse=True))

print()

#Practice 2
"""
黑色星期五是 13 號的星期五
請輸入年份，然後輸出當年度黑色星期五是哪幾天，若無則輸出 None。
Hint: .date().weekday()
-----
input:
    year
output:
    year-month-day
"""

import datetime

year = int(input("輸入一年份，將列出所有黑色星期五："))

answer = []
for i in range(1, 13):
    date = datetime.datetime(year, i, 13)
    if date.date().weekday() == 4:
        answer.append(date)
        
if len(answer) > 0:
    for i in answer:
        print(i.strftime("%Y-%m-%d"))
else:
    print("None")
    
print()

#Practice 3
"""
有一段順序被打亂的歌詞（下載網址：https://bit.ly/2r8v08m），
已知每行歌詞前都會註記歌詞是第幾行，請讀入檔案後重新排序，並將結果寫入另一個檔案，
輸出檔案如同： https//bit.ly/2NyOVEZ。
"""
lines = []

with open(file='lyrics.txt', mode='r', encoding='utf-8') as f:
    for line in f:
        info = line.split('@')
        lines.append([int(info[0]), info[1]])
        
lines.sort(key=lambda line:line[0])

with open(file='ordered_lyrics.txt', mode='w', encoding='utf-8') as f:
    for line in lines:
        f.write(line[1])