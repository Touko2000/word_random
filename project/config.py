'''
Descripttion: 
FilePath: /word_random/project/config.py
Author: lwk
Date: 2022-06-05 14:35:51
LastEditors: lwk
LastEditTime: 2022-07-04 23:26:19
'''
cibiao = "/Users/touko/Desktop/pycode/word_random/static/data/要你命3000词表.xlsx"

sheets = [29,30,31] # 第几个list
sheets = [f"List{n}" for n in sheets]
list_name = "_".join(sheets)
