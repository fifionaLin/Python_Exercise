#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# HW3_3

list1 = input().split(',')
#print(list1)

n = int(list1[0])
x = int(list1[1])

list2 = input().split(',')

list_tr = []
for i in range(n):
    list_tr.append([])
    for j in range(2):
        if j == 0:
            list_tr[i].append(list2[i])
        else:
            list_tr[i].append(list2[i+n])

#print(list_tr)

x_remain = x
t_front = 0
money = 0

total_money = []
tmp = 0

for i in range(n):
    t = int(list_tr[i][0])
    r = int(list_tr[i][1])
    #print(t,r)

    total_money.append([])
    for j in range(2):
        if j == 0:
            total_money[i].append(t)
        else:
            total_money[i].append(((t - t_front)*r + tmp))
            tmp = int(total_money[i][1])

    if x <= t:
        money = x_remain*r + money
        x_remain = 0
        t_front = t

    else:
        money = (t - t_front)*r + money
        x_remain = x_remain - (t - t_front)
        t_front = t

    #print(tmp)

#print(total_money)
#print(int(money))

final_money = money
title = x
for i in range(n):
    if int(total_money[i][0]) >= x:
        if int(total_money[i][1]) <= int(final_money):
            final_money = total_money[i][1]
            title = total_money[i][0]
        #else:
    #else:

print('%d,%d' % (title, final_money))
