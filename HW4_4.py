#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 01:09:53 2020

@author: fiona
"""
# HW4_4 選擇投資方案􏳶􏳷􏳸􏳹􏱼􏳫􏳬􏳶􏳷􏳸􏳹􏱼􏳫􏳬（權衡預期報酬及風險）

list1 = input().split(',')
item = int(list1[0])
budget = int(list1[1])
risk_factor = int(list1[2])
price = input().split(',')
reward = input().split(',')
price2 = []
for i in range(item):
    price2.append(price[i])

risk_var_cov = []
var = []
price_sort = sorted(price2)
price_tmp = []
for i in range(item):
    price_tmp.append(price2[i])
    tmp = input().split(',')
    var.append(tmp[i])
    risk_var_cov.append(tmp)

item_list = []
for i in range(item):
    get_index = price_tmp.index(price_sort[i])
    item_list.append(get_index)
    price_tmp[get_index] = 0
#print(item_list)
#print(risk_var_cov, var)

#first run
record_list = []
final_invest = []
remain_budget = budget
best_goal = 0
firstrecord_index = -1
for i in range(item):
    get_index = item_list[i]
    get_goal = int(reward[get_index]) - (risk_factor*int(var[get_index]))
    if remain_budget >= int(price[get_index]):
        if get_goal > best_goal:
            best_goal = get_goal
            firstrecord_index = get_index
#print(best_goal, firstrecord_index)

if firstrecord_index != -1:
    remain_budget -= int(price[firstrecord_index])
    item_list.remove(firstrecord_index)    
    record_list.append(firstrecord_index)
    final_invest.append(firstrecord_index + 1)
    #print(remain_budget, item_list)

    #others run
    total_cov = 0   
    for i in range(item - 1):
        best_goal = 0
        record_index = -1
        #print(record_list)
        for j in range(len(item_list)):
            get_index = item_list[j]
            
            for k in range(len(record_list)):
                a = record_list[k]
                total_cov += int(risk_var_cov[get_index][a])
            #print(total_cov)
           
            get_goal = int(reward[get_index]) - (risk_factor * (int(var[get_index]) + 2*total_cov))
            total_cov = 0
            
            if remain_budget >= int(price[get_index]):
                if get_goal > best_goal:
                    best_goal = get_goal
                    record_index = get_index
        #print(best_goal, record_index)

        if record_index != -1:
            remain_budget -= int(price[record_index])
            item_list.remove(record_index)
            record_list.append(record_index)
            final_invest.append(record_index + 1)
            #print(remain_budget, item_list)
        else:
            break

    final_invest.sort()
    for i in range(len(final_invest)):
        if i == len(final_invest) - 1:
            print(final_invest[i])
        else:
            print(final_invest[i], end=',')

else:
    print("0")
