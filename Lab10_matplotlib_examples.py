#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 17:57:29 2020

@author: fiona
"""

"""
matplotlib
只要很簡單的 import 就可以畫圖了!
import matplotlib.pyplot as py
// draw
py.show()
"""

import matplotlib.pyplot as py


midterm_1 = [10,15,15,15,30,35,40,40,40,40,55,55,65,65,65,70,80,80,85,85,90,90,100]
midterm_2 = [20,20,20,30,30,30,30,40,40,50,60,60,60,60,60,60,60,60,80,80,90,100,100]

# matplotlib histogram example
n_bins = range(0, 110, 10)
py.hist(midterm_1, bins=n_bins, alpha=0.5, label="MT1")
py.hist(midterm_2, bins=n_bins, alpha=0.5, label="MT2")
py.xlabel("Score")
py.ylabel("Number of students")
py.title("Midterms of PBC")
py.legend(loc="upper right")
py.xticks(range(0, 110, 10))
py.yticks(range(0, 10, 1))
py.show()


# matplotlib pie chart example
m1_pass_cnt = 0
m1_fail_cnt = 0
for score in midterm_1:
    if score >= 60:
        m1_pass_cnt += 1
    else:
        m1_fail_cnt += 1

m2_pass_cnt = 0
m2_fail_cnt = 0
for score in midterm_2:
    if score >= 60:
        m2_pass_cnt += 1
    else:
        m2_fail_cnt += 1
        
# create a figure with two subplots
fig, (ax1, ax2) = py.subplots(1, 2)

ax1.set_title("Midterm 1")
ax1.pie([m1_pass_cnt, m1_fail_cnt], labels=['pass', 'fail'], autopct='%.2f%%')
ax2.set_title("Midterm 2")
ax2.pie([m2_pass_cnt, m2_fail_cnt], labels=['pass', 'fail'], autopct='%.2f%%')
py.show()
