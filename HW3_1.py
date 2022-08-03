#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# HW3_1

current_num = int(input())
result_str = ''

for i in range(100):
    units_digit = current_num % 10
    tens_digit = current_num // 10 % 10
    hundreds_digit = current_num // 100 % 10
    thousands_digit = current_num // 1000 % 10


    if thousands_digit < hundreds_digit:
        first = hundreds_digit
        second = thousands_digit
    else:
        first = thousands_digit
        second = hundreds_digit

    if tens_digit < units_digit:
        third = units_digit
        forth = tens_digit
    else:
        third = tens_digit
        forth = units_digit

    thousands_digit = first
    hundreds_digit = second
    tens_digit = third
    units_digit = forth

    if hundreds_digit < tens_digit:
        second = tens_digit
        third = hundreds_digit

        hundreds_digit = second
        tens_digit = third

        if thousands_digit < hundreds_digit:
            first = hundreds_digit
            second = thousands_digit
        else:
            first = thousands_digit
            second = hundreds_digit

        if tens_digit < units_digit:
            third = units_digit
            forth = tens_digit
        else:
            third = tens_digit
            forth = units_digit

        thousands_digit = first
        hundreds_digit = second
        tens_digit = third
        units_digit = forth

        if hundreds_digit < tens_digit:
            second = tens_digit
            third = hundreds_digit

            hundreds_digit = second
            tens_digit = third
        #else:

    #else:

    num_from_max_to_min = ((thousands_digit*1000) + (hundreds_digit*100) + (tens_digit*10) + (units_digit*1))
    num_from_min_to_max = ((units_digit*1000) + (tens_digit*100) + (hundreds_digit*10) + (thousands_digit*1))

    #print(num_from_max_to_min, num_from_min_to_max)

    current_num = num_from_max_to_min - num_from_min_to_max

    #print(current_num)
    
    if str(current_num) == '6174':
        result_str += str(current_num)
        break

    result_str += str(current_num) + ","

print(result_str)
