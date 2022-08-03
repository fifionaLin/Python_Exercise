#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 04:38:48 2020

@author: fiona
"""

# PBC 109-1 TA Lab6
# Problem 1
"""
#請設計一支簡易計算機程式，一開始可以選擇模式，接著輸入數字 A 及數字 B。若輸入 1 可以算出 A+B，若輸入 2 可以算出 A-B，若輸入 3 則可以算出 A*B。
在本程式中，使用者必須可以輸入計算模式 t 以及想要計算的數字 A 與數字 B，輸出則為計算結果。
#請顯示提示語，並用自訂 function 判斷計算模式，產生不同答案。
-----
Input
Enter the type: t
Enter A: A
Enter B: B

Output
計算結果
"""
# function1
def add_two_num(n1, n2):
    return n1+n2
# function2
def subtract_two_num(n1, n2):
    return n1-n2
# function3
def multiple_two_num(n1, n2):
    return n1*n2

print("Problem 1")
_type = input("Enter the type (1,2,3): ")
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

if _type == "1":
    print(add_two_num(n1=num1, n2=num2))
elif _type == "2":
    print(subtract_two_num(n1=num1, n2=num2))
elif _type == "3":
    print(multiple_two_num(n1=num1, n2=num2))
else:
    print("Not the right type! ")
    
    
# Problem 2
"""
#請設計一支簡易計算機程式，一開始可以選擇模式，若輸入 1 可以算出以 2 為底的對數值，若輸入 2 可以算出以 e 為底的對數值，若輸入 3 則可以算出平方值。
在本程式中，使用者輸入計算模式 t 以及想要計算的數字 n，輸出則為計算結果。
#請顯示提示語，並用自訂 function 判斷計算模式，產生不同答案。
#Hint: 使用 library - math: math.log(x[, base])
-----
Input
Enter the type: t
Enter a number: n

Output
計算結果
"""
import math

def log_base_two(n):
    result = math.log2(n)
    return result

def log_base_e(n):
    result = math.log(n)
    return result

def square(n):
    result = math.pow(n, 2)
    return result

print("\nProblem 2")
_type = input("Enter the type (1,2,3): ")
num = float(input("Enter a number: "))

if _type == "1":
    print(log_base_two(num))
elif _type == "2":
    print(log_base_e(num))
elif _type == "3":
    print(square(num))
else:
    print("Not the right type! ")
    

# Problem 3
"""
#已知費氏數列為 0,1,1,2,3,5,8,13,......
其數學定義為 F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)
#輸入 n，請求出 F(n) 的值，請利用一個遞迴 function 計算。
-----
Input
n

Output
F(n)
"""
def F(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = F(n-1) + F(n-2)
    return result

print("\nProblem 3")
num = int(input("Enter a number: "))
print(F(num))


# Problem 4
"""
#要將 p 顆蘋果及 q 顆橘子分給小朋友，每個小朋友拿到的每種水果個數都要一樣，水果不能被分割，請問最多可以分給幾個小朋友呢?
#請顯示提示語，並利用一個遞迴 function 計算。
#Hint: 輾轉相除法，兩個整數的最大公因數等於其中較小的數和兩數相除餘數的最大公因數。
-----
Input
Apple: p
Orange: q

Output
小朋友數
"""
# 求最大公因數
def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

print("\nProblem 4")
p = int(input("Apple: "))
q = int(input("Orange: "))
print(gcd(p, q))
