#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 11:00:27 2020

@author: fiona
"""

# PBC 109-1 TA Lab 7 

# Practice 1
"""
請定義一個函數 countCharacter(str_)，接收一個字串參數。
找出字串中重複出現最多次的字元，並印出其出現次數及其字元。
重複出現最多次的字元只會有一個。
若沒有重複出現的字元，則印出 N。
"""
def countCharacter(str_):
    char_list = []
    for char in str_: # 將字元加入一個list
        if char_list.count(char) == 0: # 沒出現過才加
            char_list.append(char)
            
    # 記錄最多次
    max_count = 0
    max_character = ""
    for character in char_list: # 找出現最多次的字元
        if str_.count(character) > max_count:
            max_count = str_.count(character)
            max_character = character
    if max_count == 1: # 最多次數是1即是沒有重複
        print("N")
    else:
        print(max_count, max_character, sep=",")

print("-Practice 1-")        
countCharacter(input("輸入一字串，將會找出重複出現最多次的字元："))


# Practice 2
"""
所謂凱薩密碼，就是將原本的文字母對應到偏移過後的英文字母。
舉例而言，若偏移量為 3，則 A->D，B->E，X則對應回到 A。
請定義一個函數caesar(str_, n)，輸入為一字串以及偏移量，輸出為加密過後的字串。
Hint: ord() 和 chr()
"""
def caesar(str_, n):
    result = ""
    for i in range(len(str_)):
        char = str_[i]
        if char.isupper():
            shift = (ord(char) + n - ord('A')) % 26 + ord('A')
            result += chr(shift)
        else:
            shift = (ord(char) + n - ord('a')) % 26 + ord('a')
            result += chr(shift)
    return result

print()
print("-Practice 2-")
print("輸入一字串以及偏移量，輸出為加密過後的字串。")
str_ = input("輸入一字串(英文字母)：")
n = int(input("輸入偏移量(正整數)："))
print(caesar(str_, n))


# Practice 3
"""
定義一個函數 myPalindrome，接收一個字串參數。
用遞迴的方式檢查此字串是否為對稱。
效果等於 s == s[::-1]。
"""
def myPalindrome(string):
    if len(string) <= 1:
        return True
    else:
        if string[0] == string[-1]:
            return myPalindrome(string[1:-1])
        else:
            return False

print()
print("-Practice 3-")
print(myPalindrome(input("輸入一字串，將會判斷是否為對稱：")))