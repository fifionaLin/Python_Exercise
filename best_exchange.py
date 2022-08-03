#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 04:24:43 2020

@author: fiona
"""
# 自己練習的

"""
如果你在一家零售店幫消費的客人結帳，你可能需要快速地挑出合適且數量正確的鈔票與零錢。 
假設客人的消費金 𝑎 一定是 1 到 1000 之間的整數，而你有無限量的 500、100、50、10、5、1 這些面額的鈔票和零錢，
我們希望你能依照下面的規則找錢:
    你找的錢的總額要是 1000 − 𝑎 。與其給客人五張 10 個 50 元，不如給他一張 100 元......依此類推。
-----
Sample Input
286
Sample Output
500, 1; 100, 2; 10, 1; 1, 4
"""

pay = int(input())
change = 1000 - pay
money_list = [500, 100, 50, 10, 5, 1]

# 將最終的答案儲存在一個字串裡面
answer = str()

for m in money_list:
    if change // m >= 1:
        answer += (str(m) + ", " + str(change//m))
        change -= (change//m) * m
        if change != 0:
            answer += "; "
            
print(answer)