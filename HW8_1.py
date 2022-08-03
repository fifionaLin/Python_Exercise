#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 22:30:59 2020

@author: fiona
"""
# HW8_1 撲克牌遊戲:五張牌的組合

class Card: # 類別Card：花色suit、點數rank
    
    def __init__(self, suit, rank): # 初始化
        self.suit = suit
        self.rank = rank
        
    def is_A(self): # 是否為Ａ
        if self.rank == 'A':
            return True
        else:
            return False
        


def ranks_into_int(cards): # 把rank存成數字，A,J,Q,K換成數字1,11,12,13，回傳rank的list
    ranks_in_int = []
    for card in cards:
        if card.rank == 'A':
            ranks_in_int.append(1)
        elif card.rank == 'J':
            ranks_in_int.append(11)
        elif card.rank == 'Q':
            ranks_in_int.append(12)
        elif card.rank == 'K':
            ranks_in_int.append(13)
        else:
            ranks_in_int.append(int(card.rank))
    return ranks_in_int

def is_flush(cards): # 是否為同花
    standard_suit = cards[0].suit
    for i in range(1,5):
        if cards[i].suit != standard_suit:
            return False
        else:
            if i == 4:
                return True
            
def is_straight(cards): # 是否為順子
    ranks_in_int = ranks_into_int(cards) # 拿到數字版的rank list
    ranks_in_int.sort() # 小到大排序
    for i in range(1,5):
        difference = ranks_in_int[i] - ranks_in_int[i-1] # 此項與前項之差
        if difference != 1 and difference != 9:
            return False
        else:
            if i == 4:
                return True

def is_four_of_a_king(cards): # 是否為四條
    ranks_in_int = ranks_into_int(cards) # 拿到數字版的rank list
    for i in range(2):
        if ranks_in_int.count(ranks_in_int[i]) == 4:
            return True
        else:
            if i == 1:
                return False
            
def is_full_house(cards): # 是否為葫蘆
    ranks_in_int = ranks_into_int(cards) # 拿到數字版的rank list
    for i in range(5):
        if ranks_in_int.count(ranks_in_int[i]) != 2 and ranks_in_int.count(ranks_in_int[i]) != 3:
            return False
        else:
            if i == 4:
                return True
            
def how_many_pairs(cards): # 有幾對（不包含四條跟葫蘆）
    ranks_in_int = ranks_into_int(cards) # 拿到數字版的rank list
    count_list = [] # rank的出現次數
    result = 0 # 結果有幾對初始0
    for i in range(5):
        count_list.append(ranks_in_int.count(ranks_in_int[i]))
    if count_list.count(2) == 4:
        result = 2 # 兩對
    elif count_list.count(3) == 3 and count_list.count(2) != 2:
        result = 1 # 一對
    elif count_list.count(2) == 2 and count_list.count(3) != 3:
        result = 1 # 一對
    return result



# main
# 輸入資料
suits = input().split(',')
ranks = input().split(',')

# 存成五個 Card 資料
cards = []
count_A = 0 # Ａ初始0張
for i in range(5):
    cards.append(Card(suits[i], ranks[i]))
    
    if cards[i].is_A(): # 計算Ａ有幾張
        count_A += 1

# 計算此副牌的分數
point = 0
if is_flush(cards) and is_straight(cards):
    point = 100
elif is_four_of_a_king(cards):
    point = 20
    if count_A == 1:
        point += 1
elif is_full_house(cards):
    point = 10
elif is_straight(cards):
    point = 5
elif is_flush(cards):
    point = 3
else:
    point += how_many_pairs(cards)*2
    if count_A == 3 or count_A == 1:
        point += 1
# 輸出總分
print(point)
