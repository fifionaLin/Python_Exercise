#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 20:32:21 2020

@author: fiona
"""

# 實作 class 與 instance method

from datetime import datetime

class Family:
    
    def __init__(self, birthday): # 強迫初始化 instance method
        self.birthday = datetime.strptime(birthday, '%Y-%m-%d')

    def is_of_age(self): # 判斷是否成年 instance method
        today = datetime.today()
        if (today - self.birthday).days > 365*18:
            return True
        else:
            return False

Dad = Family('1978-08-07') # Dad 是 Family 的 instance
Son = Family('2008-07-13') # Son 是 Family 的 instance
print(Dad.is_of_age()) # True
print(Son.is_of_age()) # False