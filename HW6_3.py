#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 14:46:53 2020

@author: fiona
"""
# HW6_3 在新聞標題中標示出多個關鍵字

c_list = input().split(',') #公司
d_list = input().split(',') #關鍵字

d_list.sort(key = lambda i:len(i), reverse=True)

t_list = [] #新聞
while True:
    s = input()
    if s == "INPUT_END":
        break
    else:
        s = s.replace(" ", "") #移除空格
        t_list.append(s)


for t in t_list:
    # company
    # 排序公司順序，出現次數多的放前面
    had_c_list = []
    count_c_list = []   
    for c in c_list:       
        check_c = t.find(c)
        count_c = t.count(c)       
        if check_c != -1:
            had_c_list.append(c)
            count_c_list.append(count_c)
    
    sort_had_c_list = []
    for i in range(len(had_c_list)):
        index = count_c_list.index(max(count_c_list))
        count_c_list[index] = 0
        sort_had_c_list.append(had_c_list[index])
    
    # token
    t_cp = t[0:]
    for d in d_list:
        check_d = t_cp.find(d)
        
        if check_d != -1:
            t_f = t[0:check_d]
            t_b = t[check_d+len(d):]
            t_cp_f = t_cp[0:check_d]
            t_cp_b = t_cp[check_d+len(d):]
            
            if t_f[-1:] == '/':
                t = t_f + d
                t_cp = t_cp_f + 'x'*len(d)
            else:
                t = t_f + '/' + d
                t_cp = t_cp_f + '/' + 'x'*len(d)

            if t_b[0:1] == '/':
                t = t + t_b
                t_cp = t_cp + t_cp_b 
            else:
                t = t + '/' + t_b
                t_cp = t_cp + '/' + t_cp_b


    if len(sort_had_c_list) == 0:
        print("NO_MATCH")
    else:
        print('{0};{1}'.format(','.join(sort_had_c_list), t))
    