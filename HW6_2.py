#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 12:31:24 2020

@author: fiona
"""
# HW6_2 在文章中標示出兩個關鍵字

w = int(input()) #距離參數
k1 = str(input()) #關鍵字1
k2 = str(input()) #關鍵字2

s_str = ""
while True:
    s = str(input())
    if s == "INPUT_END":
        break
    else:
        s_str = s_str + s + " "
s_str = s_str.strip() #移除不該有的空格

is_find = False #是否有找到答案

check1 = s_str.find(k1) #找關鍵字1的匹配
position1 = check1 #關鍵字1的位置    
while check1 != -1:
        
    s_str1_f = s_str[0:position1+len(k1)] #以關鍵字1把字串切斷(前段)
    s_str1_b = s_str[position1+len(k1):] #以關鍵字1把字串切斷(後段)
    check2 = s_str1_b.find(k2) #找關鍵字2的匹配
    position2 = len(s_str1_f) + check2 #關鍵字2的位置
        
    while check2 != -1:
            
        #判斷兩關鍵字之間的距離
        if position2 - (position1 + len(k1)) <= w:
            if position1 < 8:
                answer = s_str[0:position1] + '**' + str(k1) + '**' + s_str[position1+len(k1):position2] + '**' + str(k2) + '**' + s_str[position2+len(k2):position2+len(k2)+7]
        
            else:
                answer = s_str[position1-7:position1] + '**' + str(k1) + '**' + s_str[position1+len(k1):position2] + '**' + str(k2) + '**' + s_str[position2+len(k2):position2+len(k2)+7]
            print(answer)
                
            is_find = True #有找到答案
            
            s_str2_f = s_str[0:position2+1] #以關鍵字2把字串切斷(前段)
            s_str2_b = s_str[position2+1:] #以關鍵字2把字串切斷(後段)
            check2 = s_str2_b.find(k2) #找新的關鍵字2的匹配
            position2 = len(s_str2_f) + check2 #新的關鍵字2的位置
                
        else:
            break
    
    s_str1_f = s_str[0:position1+1] #以關鍵字1把字串切斷(前段)
    s_str1_b = s_str[position1+1:] #以關鍵字1把字串切斷(後段)    
    check1 = s_str1_b.find(k1) #找新的關鍵字1的匹配
    position1 = len(s_str1_f) + check1 #新的關鍵字1的位置
        
if not is_find:
    print("NO_MATCH")