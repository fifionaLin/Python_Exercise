#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 20:26:29 2020

@author: fiona
"""
# HW5_1

"""
要先在 Terminal安裝 matplotlib套件
"""

import matplotlib.pyplot as plt

def plotlines(linelist, canvas=[-2, 2, -2, 2], finalize=True):
    plt.figure(figsize=(5, 5))
    plt.axis(canvas)    
    for aline in linelist:
        plt.plot([aline[0], aline[2]], [aline[1], aline[3]], linestyle='-', marker='o', color='b')
    plt.draw()
    plt.pause(.01)
    if finalize:
        plt.show()
        
fig1 = [[0, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0]]
plotlines(fig1)