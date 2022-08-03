#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:11:51 2020

@author: fiona
"""
# HW8_2 撲克牌遊戲:多組牌計算分數

class Card: # 類別Card：花色suit、點數rank、數字版點數int_rank
    
    def __init__(self, suit, rank): # 初始化
        self.suit = suit
        self.rank = rank
        if rank == 'A':
            self.int_rank = 1
        elif rank == 'J':
            self.int_rank = 11
        elif rank == 'Q':
            self.int_rank = 12
        elif rank == 'K':
            self.int_rank = 13
        else:
            self.int_rank = int(rank)
        
    def is_A(self): # 是否為Ａ
        if self.rank == 'A':
            return True
        else:
            return False


class Deck: # 類別Deck：一個人所拿到的牌組叫做 Deck，一個 Deck 中會有許多張 Card
    
    def __init__(self): # 初始化
        self.cards = [] # cards為Deck的attribute
        
    def add_card(self, card): # 增加Card
        self.cards.append(card)
        
    def is_almost_five(self): # 是否已滿五張牌
        if len(self.cards) == 5:
            return True
        else:
            return False
        
    def is_conform_the_rules(self, new_suit, new_int_rank): # 新牌經過規則檢查，判斷是否能加入
        # 當新牌點數為1時，把點數改成14，方便減一的計算
        if new_int_rank == 1:
            new_int_rank = 14
        for i in range(len(self.cards)):
            if self.cards[i].suit == new_suit and self.cards[i].int_rank == new_int_rank-1:
                self.cards.pop(i) # 不合規定，拿掉此張牌
                #print("skip")
                return False # 新牌不能加入
            else:
                if i == len(self.cards)-1:
                    return True # 新牌可以加入
    
    def is_flush(self): # 是否為同花
        if len(self.cards) < 5:
            return False       
        standard_suit = self.cards[0].suit
        for i in range(1,5):
            if self.cards[i].suit != standard_suit:
                return False
            else:
                if i == 4:
                    return True
            
    def is_straight(self): # 是否為順子
        if len(self.cards) < 5:
            return False   
        ranks_in_int = []
        for card in deck.cards: # 拿到數字版的rank list
            ranks_in_int.append(card.int_rank)
        ranks_in_int.sort() # 小到大排序
        for i in range(1,5):
            difference = ranks_in_int[i] - ranks_in_int[i-1] # 此項與前項之差
            if difference != 1 and difference != 9:
                return False
            else:
                if i == 4:
                    return True

    def is_four_of_a_king(self): # 是否為四條
        if len(self.cards) < 4:
            return False
        ranks_in_int = []
        for card in deck.cards: # 拿到數字版的rank list
            ranks_in_int.append(card.int_rank)
        for i in range(2):
            if ranks_in_int.count(ranks_in_int[i]) == 4:
                return True
            else:
                if i == 1:
                    return False
            
    def is_full_house(self): # 是否為葫蘆
        if len(self.cards) < 5:
            return False    
        ranks_in_int = []
        for card in deck.cards: # 拿到數字版的rank list
            ranks_in_int.append(card.int_rank)
        for i in range(5):
            if ranks_in_int.count(ranks_in_int[i]) != 2 and ranks_in_int.count(ranks_in_int[i]) != 3:
                return False
            else:
                if i == 4:
                    return True
                
    def how_many_pairs(self): # 有幾對（不包含四條跟葫蘆）
        if len(self.cards) < 2:
            return False    
        ranks_in_int = []
        for card in deck.cards: # 拿到數字版的rank list
            ranks_in_int.append(card.int_rank)            
        count_list = [] # rank的出現次數
        result = 0 # 結果有幾對初始0
        for i in range(len(ranks_in_int)):
            count_list.append(ranks_in_int.count(ranks_in_int[i]))
        if count_list.count(2) == 4:
            result = 2 # 兩對
        elif count_list.count(3) == 3 and count_list.count(2) != 2:
            result = 1 # 一對
        elif count_list.count(2) == 2 and count_list.count(3) != 3:
            result = 1 # 一對
        return result
    
    def count_A(self): # 計算此組牌Ａ有幾張
        count = 0
        for card in self.cards:
            if card.is_A():
                count += 1
        return count
    
    def count_points(self):
        point = 0
        if self.is_flush() and self.is_straight():
            point = 100
        elif self.is_four_of_a_king():
            point = 20
            if self.count_A() == 1:
                point += 1
        elif self.is_full_house():
            point = 10
        elif self.is_straight():
            point = 5
        elif self.is_flush():
            point = 3
        else:
            point += self.how_many_pairs()*2
            if self.count_A() == 3 or self.count_A() == 1:
                point += 1
        return point
    
    
        
# main
# 輸入資料
player_num = int(input()) # 玩家數

answer = [] # 結果list
for i in range(player_num):
    deck = Deck() # 創建一個玩家牌組
    
    input_cards = input().split(',') # 輸入的資料先存成一個list
    
    for input_card in input_cards:
        card = Card(input_card[0], input_card[1]) # 創建一張牌
        
        if len(deck.cards) == 0: # 若為第一張牌，直接加入
            deck.add_card(card)
            #print("first")
        else:
            if deck.is_almost_five(): # 牌組已滿跳出迴圈
                #print("almost five")
                break
            else:
                if deck.is_conform_the_rules(card.suit, card.int_rank):
                    deck.add_card(card) # 符合規定，增加新牌
                    #print("add")
                
    #print(len(deck.cards))
    answer.append(str(deck.count_points()))

# 輸出結果
print(','.join(answer))
