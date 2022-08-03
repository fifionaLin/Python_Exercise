#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 02:33:37 2020

@author: fiona
"""

#寫檔（如果檔案不存在，會建立新檔）
with open(file="Lab8_FilesIO_test.txt", mode="w", encoding="utf-8") as f:
    f.write("Hello World!")
    f.write("\n\n")
    f.write("My name is Fiona.")
    f.write("\n")
    f.write("Nice to meet you.")

#讀檔
#read(): read entire file
with open(file="Lab8_FilesIO_test.txt", mode="r", encoding="utf-8") as f:
    print(f.read())

print()
#readline(): read file line by line    
with open(file="Lab8_FilesIO_test.txt", mode="r", encoding="utf-8") as f:
    line = f.readline()
    print(line.strip())

print()
#Read file through every line
with open(file="Lab8_FilesIO_test.txt", mode="r", encoding="utf-8") as f:
    line_cnt = 1
    for line in f:
        print(str(line_cnt) + ": " + line.strip())
        line_cnt += 1

print()
#readlines(): return a list of lines
with open(file="Lab8_FilesIO_test.txt", mode="r", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)