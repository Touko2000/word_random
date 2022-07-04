'''
Descripttion: 
FilePath: /word_random/project/config.py
Author: lwk
Date: 2022-06-05 14:35:51
LastEditors: lwk
LastEditTime: 2022-07-04 23:39:04
'''
# 词表路径
cibiao = "/Users/touko/Desktop/pycode/word_random/static/data/要你命3000词表.xlsx"

# 哪几个list
sheets = [29,30,31] 
sheets = [f"List{n}" for n in sheets]
list_name = "_".join(sheets)
