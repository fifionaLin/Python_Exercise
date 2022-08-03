#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 23:44:59 2020

@author: fiona
"""
# HW4_2&3 用兩種方式(cp_value, value)來決定放入包包的物品
# Knapsack Problem

list1 = input().split(",")
item = int(list1[0])
amount = int(list1[1])
weight = input().split(",")
value = input().split(",")
#print(item, amount, weight, value)

weight2 = []
value2 = []
for i in range(item):
    weight2.append(int(weight[i]))
    value2.append(int(value[i]))

#cp value
cp_value = []
weight_tmp = []
for i in range(item):
    cp_value.append(float(value[i]) / float(weight[i]))
    weight_tmp.append(weight2[i])
cp_value_sort = sorted(cp_value, reverse = True)
#print(cp_value, cp_value_sort)

value_sort = sorted(value2, reverse = True)
weight_sort = sorted(weight2)
#print(weight_sort, value_sort)

#list index from weight
index_for_weight = []
index_list1 = []
index_list2 = []
for i in range(item):
    now_index = weight_tmp.index(weight_sort[i])
    index_for_weight.append(now_index)
    weight_tmp[now_index] = -1
    index_list1.append('')
    index_list2.append('')
#print(index_for_weight)

#list index from cp_value & value
for i in range(item):
    now_index = index_for_weight[i]
    #way one; cp value
    way1_index = cp_value_sort.index(cp_value[now_index])
    index_list1[way1_index] = now_index
    cp_value_sort[way1_index] = -1
    #way two: value
    way2_index = value_sort.index(value2[now_index])
    index_list2[way2_index] = now_index
    value_sort[way2_index] = -1
#print(index_list1, index_list2)

#find the final item list
total_weight1 = 0
total_value1 = 0
total_weight2 = 0
total_value2 = 0
real_index1 = []
real_index2 = []
for i in range(item):
    now_index1 = int(index_list1[i])
    now_index2 = int(index_list2[i])
    total_weight1 += int(weight[now_index1])
    total_weight2 += int(weight[now_index2])

    #way one: 
    if total_weight1 <= amount:
        real_index1.append(now_index1 + 1)
        total_value1 += int(value[now_index1])
    else:
        total_weight1 -= int(weight[now_index1])
    
    if total_weight2 <= amount:
        real_index2.append(now_index2 + 1)
        total_value2 += int(value[now_index2])
    else:
        total_weight2 -= int(weight[now_index2])
#print(total_value1, total_value2)

real_index1.sort()
real_index2.sort()

#compare with total value
if total_value1 >= total_value2:
    for i in range(len(real_index1)):
        if i < len(real_index1) - 1:
            print(real_index1[i], end=",")
        else:
            print(real_index1[i])
else:
    for i in range(len(real_index2)):
        if i < len(real_index2) - 1:
            print(real_index2[i], end=",")
        else:
            print(real_index2[i])