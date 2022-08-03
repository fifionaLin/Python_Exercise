#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 04:16:07 2020

@author: fiona
"""
# HW7_3 分析新聞並算出買個公司股票幾張（HW6_3的延續）
# /Users/fiona/Python_exercise/news_title.txt
# /Users/fiona/Python_exercise/news_dict.txt
# /Users/fiona/Python_exercise/company_category.txt

# 接收輸入的檔案路徑
news_title_rute = input()
news_dict_rute = input()
company_category_rute = input()

news_title = [] # 把檔案中的新聞資料一行一行存進
with open(file=news_title_rute, mode='r', encoding='utf-8') as f:
    for line in f:
        line = line.strip().replace(" ", "")  # 去除空格
        news_title.append(line)

keyword_dict = dict() # 關鍵字對應到其權重的dict
keyword = [] # 所有關鍵字
with open(file=news_dict_rute, mode='r', encoding='utf-8') as f:
    for line in f:
        this_list = line.split(' ')
        keyword.append(this_list[0])
        keyword_dict[this_list[0]] = int(this_list[1])

category_dict = dict() # 產業類別對應到公司的dict
company = [] # 所有公司
with open(file=company_category_rute, mode='r', encoding='utf-8') as f:
    for line in f:
        this_list = line.strip().split(' ')
        company.append(this_list[0])
        if this_list[1] not in category_dict:
            category_dict[this_list[1]] = []
        category_dict[this_list[1]].append(this_list[0])


# 函式用途：計算新聞分數
def count_tokenNews_score(news):
    score = 0 # 初始總分為零
    for key in keyword:
        check = news.find(key) # 找關鍵字位置
        count = news.count(key) # 關鍵字出現次數
        for i in range(count): # 關鍵字有幾個就要算幾次  
            if check != -1:
                # 關鍵字在字串尾巴
                if check+len(key) == len(news) and news[check-1:check] == '/':
                    score += keyword_dict.get(key)
                # 關鍵字在字串首
                if check == 0 and news[check+len(key):check+len(key)+1] == '/':
                    score += keyword_dict.get(key)
                # 關鍵字在字串中央
                if news[check-1:check] == '/' and news[check+len(key):check+len(key)+1] == '/':
                    score += keyword_dict.get(key)
            front = news[0:check]
            back = news[check+len(key):]
            news = front + ('*'*len(key)) + back # 把判斷過的關鍵字用＊代替
            check = news.find(key) # 再找一次關鍵字位置  
    return score            


keyword.sort(key = lambda i:len(i), reverse=True) # 關鍵字根據長度排序

company_score_dict = dict() # 各公司的總分

for title in news_title:
    # company
    # 找出有的company及出現次數
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
          
    ##########
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
                token_index_list_new[-1] = token_index_list[i]

            elif index0 + len0 > index1 and len0 >= len1:  # 符合條件就跳過
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
    
    
    this_score = count_tokenNews_score(token_string) # 本則新聞分數    
    # 把分數加到有對應的公司
    if len(sort_had_company) != 0: # 確定有對應的公司
        for c in sort_had_company:
            if c not in company_score_dict:
                company_score_dict[c] = this_score
            else:
                company_score_dict[c] += this_score


# 接收輸入
data = input().split(',')
want_category = data[0]
stock_amount = int(data[1])
distribute_amount = data[2].split(':')

companies = category_dict.get(want_category) # 找出所要產業類別的公司

if companies == None: # 沒有該產業類別的公司
    print("NO_MATCH")
else:
    companies.sort(key=lambda x: company_score_dict.get(x), reverse=True) # 用公司總分排序
    times = min(len(companies), len(distribute_amount)) # 最終要列出幾間公司
    final_stock_amount = [0 for i in range(times)] # 給定初始值為零
    # 分配股票數量
    while stock_amount > 0:
        for i in range(times):
            get_amount = int(distribute_amount[i]) # 這次的分配量
            if stock_amount > get_amount:
                final_stock_amount[i] += get_amount
                stock_amount -= get_amount
            else:
                final_stock_amount[i] += stock_amount
                stock_amount = 0
            if stock_amount == 0:
                break
    # 輸出結果
    for i in range(times):
        if final_stock_amount[i] != 0:
            print('{0}購買{1}張'.format(companies[i], final_stock_amount[i]))
