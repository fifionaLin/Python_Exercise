#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 22:47:24 2020

@author: fiona
"""
# HW5_3 對球員的打擊成績紀錄作分析

#Function_1
#計算指定球員在指定球季(一個或多個)的打擊率，計算方式則是將指定球員在指定球季的累加安打數，除以指定球季的累加打數，回傳值為一個數值。
def player_avg(seasons, records, player_number):
    H_sum, AB_sum = 0, 0
    for record in records:
        if record[1] == player_number:
            if record[2] in seasons:
                H_sum += record[4]
                AB_sum += record[3]
    result = H_sum/AB_sum
    return result

#Function_2
#計算指定球隊在指定球季的團隊打擊率，計算方式則是將所有屬於該球隊的球員的累加安打數，除以所有屬於該球隊的球員的累加打數，回傳值為一個數值。
def team_avg(seasons, records, team_name):
    H_sum, AB_sum = 0, 0
    for record in records:
        if record[0] == team_name:
            if record[2] in seasons:
                H_sum += record[4]
                AB_sum += record[3]
    result = H_sum/AB_sum
    return result

#Function_3
#計算各個指定球季中，所有球員的打擊率，並找出各個指定球季打擊率最高的球員，回傳值為一個 List。
#如果多名球員在某一季的打擊率相同，則選擇打數較少的那位球員， 若打數仍然相同，則選擇號碼數字較小的那位球員。
def best_player(seasons, records):
    N_list = []
    for season in seasons:
        bestHit = -1.0
        for record in records:
            if record[2] == season:
                hit = player_avg(seasons=season, records=records, player_number=record[1])
                if hit > bestHit:
                    # 紀錄
                    bestHit = hit
                    minAB = record[3]
                    minN = record[1]
                elif hit == bestHit:
                    if record[3] < minAB:
                        # 紀錄
                        bestHit = hit
                        minAB = record[3]
                        minN = record[1]
                    elif record[3] == minAB:
                        if record[1] < minN:
                            # 紀錄
                            bestHit = hit
                            minAB = record[3]
                            minN = record[1]
        N_list.append(minN)
    return N_list

#Function_4
#計算各個指定球季中，所有球隊的團隊打擊率，並找出各個指定球季團隊打擊率最高的球隊，回傳值為一個 List。
#如果多個球隊在某一季的團隊打擊率相同，則選擇打數較少的那個球隊，若打數仍然相同，則選擇英文字母排序較前(A最前，Z最後)的那個球隊。
def best_team(seasons, records):
    T_list = []
    for season in seasons:
        bestHit = -1.0
        for record in records:
            if record[2] == season:
                hit = team_avg(seasons=season, records=records, team_name=record[0])
                ABsum = team_avg_ABsum(season=season, records=records, team_name=record[0])
                if hit > bestHit:
                    # 紀錄
                    bestHit = hit
                    minABs = ABsum
                    minT = record[0]
                elif hit == bestHit:
                    if ABsum < minABs:
                        # 紀錄
                        bestHit = hit
                        minABs = ABsum
                        minT = record[0]
                    elif ABsum == minABs:
                        if record[0] < minT:
                            # 紀錄
                            bestHit = hit
                            minABs = ABsum
                            minT = record[0]
        T_list.append(minT)
    return T_list

#計算某球季中，某球隊的打擊數總和。
def team_avg_ABsum(season, records, team_name):
    AB_sum = 0
    for record in records:
        if record[2] == season and record[0] == team_name:
            AB_sum += record[3]
    return AB_sum

#打擊率經過無條件捨去到小數點第二位後，小數點後的尾數為零，請不要印出。
#經過無條件捨去到小數點第二位後計算出0.00，這時請印出0。
def chop(avg):
    avg = int(avg*100) / 100
    return avg if avg > 0 else 0

#把list中的用','隔開，一項一項print出來。
def print_list_onebyone(_list):
    for i in range(len(_list)):
        if i == len(_list)-1:
            print(_list[i])
        else:
            print(_list[i], end=",")


# main
records = []
while True:
    str1 = input()
    if str1 == "RECORDSTOP":
        break
    else:
        str1list = str1.split(',')
        tmp = []
        for i in range(len(str1list)):
            if i == 0 or i == 2:
                tmp.append(str1list[i])
            else:
                tmp.append(int(str1list[i]))
        records.append(tmp)
#print(records)
functions = []
while True:
    str2 = input()
    if str2 == "FUNCTIONSTOP":
        break
    else:
        str2list = str2.split()
        functions.append(str2list)
#print(functions)

for func in functions:
    if func[0] == '1':
        s = func[1].split(',')
        n = int(func[2])
        print(chop(player_avg(seasons=s, records=records, player_number=n)))
    elif func[0] == '2':
        s = func[1].split(',')
        t = func[2]
        print(chop(team_avg(seasons=s, records=records, team_name=t)))
    elif func[0] == '3':
        s = func[1].split(',')
        print_list_onebyone(best_player(seasons=s, records=records))
    elif func[0] == '4':
        s = func[1].split(',')
        print_list_onebyone(best_team(seasons=s, records=records))