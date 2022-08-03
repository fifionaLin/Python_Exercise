#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# HW3_4

n = int(input())
set_list = input().split(',')
price_list = input().split(',')
amount_list = input().split(',')
#print(n, set_list, price_list, amount_list)

is_set = []
for i in range(n):
    is_set.append(0)

for i in range(len(set_list)):
    for j in range(n):
        if int(set_list[i]) == (j+1):
            is_set[j] = 1
#print(is_set)

discount_list = []
five_set_num = 20
for i in range(n):
    discount_list.append([])
    if is_set[i] == 0:
        discount_list[i].append(0)
        discount_list[i].append(0)
    elif is_set[i] == 1:
        q = int(amount_list[i]) // 5
        r = int(amount_list[i]) % 5
        if q < five_set_num:
            five_set_num = q
        discount_list[i].append(q)
        discount_list[i].append(r)
#print(discount_list, five_set_num)

one_set_num = 5
for i in range(n):
    if is_set[i] == 1:
        diff = discount_list[i][0] - five_set_num
        discount_list[i][0] = 0
        discount_list[i][1] += diff*5
        if discount_list[i][1] < one_set_num:
            one_set_num = discount_list[i][1]
#print(discount_list, one_set_num)

for i in range(n):
    if is_set[i] == 1:
        diff = discount_list[i][1] - one_set_num
        discount_list[i][1] = diff
#print(discount_list)

original_total = 0
non_discount_total = 0
set_price = 0
for i in range(n):
    original_total += int(price_list[i]) * int(amount_list[i])
    if is_set[i] == 0:
        non_discount_total += int(price_list[i]) * int(amount_list[i])
    elif is_set[i] == 1:
        non_discount_total += int(price_list[i]) * int(discount_list[i][1])
        set_price += int(price_list[i])

discount_total = (five_set_num*5*set_price*0.8) + (one_set_num*set_price*0.9)
new_total = non_discount_total + discount_total
#print(set_price)
#print(original_total, non_discount_total, discount_total, new_total)

save = float(original_total) - float(new_total)
#print(save)
new_hire = int(save / 1000)
#print(new_hire)

if new_hire == 0:
    print('So sad. I messed up.')
else:
    print('%d,%d' % (new_total, new_hire))
