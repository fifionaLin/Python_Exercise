#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 11:14:55 2020

@author: fiona
"""
# HW6_1 在文章中標示出一個關鍵字

k = str(input()) #關鍵字

s_str = ""
while True:
    s = str(input())
    if s == "INPUT_END":
        break
    else:
        s_str = s_str + s + " "
s_str = s_str.strip() #移除不該有的空格

check = s_str.find(k) #找匹配
if check == -1:
    print("NO_MATCH")

else:
    position = check #關鍵字的位置 
    while check != -1:
        position2 = position + len(k)
        if position < 8:
            answer = s_str[0:position] + '**' + str(k) + '**' + s_str[position2:position2+7]
        else:
            answer = s_str[position-7:position] + '**' + str(k) + '**' + s_str[position2:position2+7]
        print(answer)
        
        s_str_f = s_str[0:position+1] #已判斷過的字串前段
        s_str_b = s_str[position+1:] #尚未判斷的字串後段
    
        check = s_str_b.find(k) #找新的匹配
        position = len(s_str_f) + check #新的關鍵字的位置