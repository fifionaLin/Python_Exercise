#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 21:13:38 2020

@author: fiona
"""
# HW5_2 測試圖形與旋轉量

import math

# 表示圖形的方式: 把所有的線段座標印出來
def printlines(linelist):
    for i, aline in enumerate(linelist):
        print("Line%d: %0.3f %0.3f %0.3f %0.3f" % (i, aline[0], aline[1], aline[2], aline[3]))

# 將所有linelist中的點逆時鐘旋轉degree度
def rotate(linelist, degree=0):
    for item in linelist:
        cp_item = []
        for i in range(len(item)):
            cp_item.append(item[i])
        item[0] = cp_item[0] * (math.cos(degree)) + cp_item[1] * -(math.sin(degree))
        item[1] = cp_item[0] * (math.sin(degree)) + cp_item[1] * (math.cos(degree))
        item[2] = cp_item[2] * (math.cos(degree)) + cp_item[3] * -(math.sin(degree))
        item[3] = cp_item[2] * (math.sin(degree)) + cp_item[3] * (math.cos(degree))
    return printlines(linelist)

# main
fig = []
while True:
    str1 = input()
    if str1 == "LINESTOP":
        break
    else:
        figlist = str1.split(',')
        tmp = []
        for item in figlist:
            tmp.append(float(item))
        fig.append(tmp)
#print(fig)
r = math.radians(int(input()))
#print(r)
rotate(fig, degree=r)