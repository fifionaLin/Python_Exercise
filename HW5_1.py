#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 20:33:11 2020

@author: fiona
"""
# HW5_1 測試圖形與平移量

# 表示圖形的方式: 把所有的線段座標印出來
def printlines(linelist):
    for i, aline in enumerate(linelist):
        print("Line%d: %0.3f %0.3f %0.3f %0.3f" % (i, aline[0], aline[1], aline[2], aline[3]))

# 圖形左右與上下平移
def plotshift(linelist, xshift=0, yshift=0):
    for item in linelist:
        item[0] += xshift
        item[1] += yshift
        item[2] += xshift
        item[3] += yshift
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
shift = input().split(',')
x = float(shift[0])
y = float(shift[1])
#print(x, y)
#print(plotshift(fig, xshift=x, yshift=y))
plotshift(fig, xshift=x, yshift=y)