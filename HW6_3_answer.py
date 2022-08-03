#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 19:38:14 2020

@author: fiona
"""

# HW6_3 股票消息面分析
# 接收輸入
company = input().split(',')
keyword = input().split(',')
news_title = []
while True:
    title = input()
    title = title.replace(" ", "")  # 去除空格
    if title == "INPUT_END":
        break
    news_title.append(title)

keyword.sort(key = lambda i:len(i), reverse=True) # 關鍵字根據長度排序

# 斷詞
company_ans = []
token_ans = []

for title in news_title:
    # company
    # 排序公司順序，出現次數多的放前面
    had_company = []
    count_company = []
    for c in company:
        check_c = title.find(c)
        count_c = title.count(c)
        if check_c != -1:
            had_company.append(c)
            count_company.append(count_c)
    # 把找出的company依照出現次數排序（多的在前面）        
    sort_had_company = []
    for i in range(len(had_company)):
        index = count_company.index(max(count_company))
        count_company[index] = 0
        sort_had_company.append(had_company[index])

    ########## 解答方法
    # token
    token_index_list = []
    # token_list = []
    for key in keyword:
        idx = title.find(key)
        title_tmp = title
        while idx != -1:
            token_index_list.append([idx, len(key)])
            title_tmp = title_tmp.replace(key, " "*len(key), 1)
            idx = title_tmp.find(key)
    # 排序token_index_list，因為關鍵字不一定照新聞標題順序出現
    token_index_list.sort()

    # 移除重疊的關鍵字
    token_index_list_new = []
    for i in range(len(token_index_list)):
        if i == 0:
            token_index_list_new.append(token_index_list[i])
        else:
            last = token_index_list_new[-1]

            index0 = last[0]
            len0 = last[1]

            index1 = token_index_list[i][0]
            len1 = token_index_list[i][1]

            if index0 + len0 > index1 and len0 < len1:  # 不合條件就取代
                # print(token_index_list)
                # print(token_index_list[i])
                token_index_list_new[-1] = token_index_list[i]

            elif index0 + len0 > index1 and len0 >= len1:  # 符合條件就跳過
                # print(token_index_list[i])
                continue
            else:   # 沒有重複一律就加進去
                token_index_list_new.append(token_index_list[i])

    token_string = ''
    for i in range(len(token_index_list_new)):
        if i == 0:
            index0 = 0  # 非關鍵字起點index
        else:
            # 非關鍵字起點index，就是上個關鍵字的起始index+它的長度
            index0 = sum(token_index_list_new[i-1])

        # key1_pos
        # 非關鍵字終點index、關鍵字起點index
        index1 = token_index_list_new[i][0]
        # 關鍵字終點index
        index2 = token_index_list_new[i][0] + token_index_list_new[i][1]
        if i == 0:
            if title[index0:index1] == "":
                token_string += title[index1:index2]
            else:
                token_string += title[index0:index1] + '/' \
                                + title[index1:index2]
        else:
            if title[index1:index2] == "":
                token_string += '/' + title[index0:index1]
            else:
                token_string += '/' + title[index0:index1] + '/' \
                                + title[index1:index2]

    # 剩下最後一段
    # 沒有任何可以斷的關鍵字，就回傳原始標題
    if token_string == "":
        token_string = title
    elif title[index2-1] != title[-1]:
        token_string += '/' + title[index2:]

    # 移除可能的//，因為關鍵字可能相連
    token_string = token_string.replace("//", "/")
    ##########
    
    # 輸出結果
    if len(sort_had_company) == 0:
        print("NO_MATCH")
    else:
        print('{0};{1}'.format(','.join(sort_had_company), token_string))


# 合併公司名稱與斷詞，輸出結果
"""
for i in range(len(company_ans)):
    if company_ans[i] == "NO_MATCH":
        print(company_ans[i])
    else:
        print(company_ans[i] + ';' + token_ans[i])
        """
