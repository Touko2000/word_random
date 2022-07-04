'''
Descripttion: 
FilePath: /word_random/project/words.py
Author: lwk
Date: 2022-04-30 09:37:28
LastEditors: lwk
LastEditTime: 2022-07-04 23:26:13
'''
import random
import time
import pandas as pd
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import project.config as config
from project.logger import logger
today = time.strftime("%Y-%m-%d", time.localtime())

class RW:
    def __init__(self, path=config.cibiao):
        self.path = path
        self.visit = {}
        self.error = []
        self.right = []
        self.unfamiliar = []
        self.history = []
        self.pointer = 0
        
        self.error_num = 0
        self.right_num = 0
        self.unfamiliar_num = 0
        
        self.load(sheets=config.sheets)
        print(config.sheets)
        self.all_num = 0
        pass
    
    def load(self, sheets):
        word_dict = {}
        for sheet in sheets:
            words_sheet = pd.read_excel(self.path, sheet_name=sheet, header=None)
            print(sheet)
            for index, row in words_sheet.iterrows():
                if index >= 200:
                    break
                word_dict[row[1]] = {
                    "mean": row[2],
                    "explain": row[3],
                    "list": sheet,
                    "line": index
                }
        self.word_dict = word_dict
        self.word_list = list(word_dict.keys())
        
    def get_rand_word(self):
        rand_word = random.choice(self.word_list)
        while self.visit.get(rand_word) and rand_word not in self.error and random.random() >= 0.2:
            rand_word = random.choice(self.word_list)
        self.cur_rand_word = rand_word
        self.history.append(self.cur_rand_word)
        self.pointer = len(self.history) - 1
        logger.info(f"随机生成单词 {self.cur_rand_word}, list: {self.word_dict[self.cur_rand_word]['list']}, line: {self.word_dict[self.cur_rand_word]['line']}")
        return self.cur_rand_word
    
    def prior_word(self):
        print(self.history)
        if self.pointer == 0:
            logger.info(f"查找到第一个单词 {self.cur_rand_word}")
        else:
            self.pointer -= 1
            logger.info(f"查找到上一个单词 {self.cur_rand_word}")
        self.cur_rand_word = self.history[self.pointer]
        return self.history[self.pointer]
    
    def next_word(self):
        print(self.history)
        if self.pointer == len(self.history) - 1:
            logger.info(f"查找到最后一个单词 {self.cur_rand_word}")
        else:
            self.pointer += 1
            logger.info(f"查找到下一个单词 {self.cur_rand_word}")
        self.cur_rand_word = self.history[self.pointer]
        return self.history[self.pointer]
    
    def get_cur_mean(self):
        cur_word = self.history[self.pointer]
        return self.word_dict.get(cur_word)

    def update_right(self):
        if self.cur_rand_word in self.right:
            pass
        else:
            self.right.append(self.cur_rand_word)
            self.right_num = len(self.right)
            if random.random() >= 0.33:
                self.visit[self.cur_rand_word] = 1
                self.all_num = len(self.visit)
        print(self.right)

    def update_error(self):
        if self.cur_rand_word in self.error:
            pass
        else:
            self.error.append(self.cur_rand_word)
            self.visit[self.cur_rand_word] = 1
            self.all_num = len(self.visit)
            
            if self.cur_rand_word in self.right:
                if random.random() >= 0.8:
                    del self.right[self.right.index(self.cur_rand_word)]
                    self.right_num = len(self.right)
        with open(f"./error_unfamiliar/error_{config.list_name}_{today}.txt", 'w', encoding='utf8') as f:
            for word in self.error:
                f.write(word + ", " + self.word_dict[word]["mean"] + "\n")
        self.error_num = len(self.error)
    
    def update_unfamiliar(self):
        if self.cur_rand_word in self.unfamiliar:
            pass
        else:
            self.unfamiliar.append(self.cur_rand_word)
            self.visit[self.cur_rand_word] = 1
            self.all_num = len(self.visit)
            
            if self.cur_rand_word in self.right:
                if random.random() >= 0.8:
                    del self.right[self.right.index(self.cur_rand_word)]
                    self.right_num = len(self.right)
        with open(f"./error_unfamiliar/unfamiliar_{config.list_name}_{today}.txt", 'w', encoding='utf8') as f:
            for word in self.unfamiliar:
                f.write(word + ", " + self.word_dict[word]["mean"] + "\n")
        self.unfamiliar_num = len(self.unfamiliar)
    
    def get_list(self, identity):
        """_summary_

        Args:
            identity (_type_): _description_

        Returns:
            _type_: _description_
        """
        string = ''
        assert identity in ["error", "unfamiliar", "right"]
        if identity == "error":
            for idx, w in enumerate(self.error):
                if idx != 0:
                    string += ", "
                string += w
        elif identity == "unfamiliar":
            for idx, w in enumerate(self.unfamiliar):
                if idx != 0:
                    string += ", "
                string += w
        else:
            for idx, w in enumerate(self.right):
                if idx != 0:
                    string += ", "
                string += w
        return string
    
    def delerror(self):
        if len(self.error) <= 1:
            self.error = []
        else:
            if not self.cur_rand_word in self.error:
                pass
            else:
                if self.visit.get(self.error[-1]):
                    del self.visit[self.error[-1]]
                    self.all_num = len(self.visit)
                self.error = self.error[:-1]
        self.error_num = len(self.error)
            
    def delright(self):
        if len(self.right) <= 1:
            self.right = []
        else:
            print(self.right)
            print(self.cur_rand_word)
            if not self.cur_rand_word in self.right:
                pass
            else:
                if self.visit.get(self.right[-1]):
                    del self.visit[self.right[-1]]
                    self.all_num = len(self.visit)
                self.right = self.right[:-1]
        self.right_num = len(self.right)
    
    def delunfamiliar(self):
        if len(self.unfamiliar) <= 1:
            self.unfamiliar = []
        else:
            if not self.cur_rand_word in self.unfamiliar:
                pass
            else:
                if self.visit.get(self.unfamiliar[-1]):
                    del self.visit[self.unfamiliar[-1]]
                    self.all_num = len(self.visit)
                self.unfamiliar = self.unfamiliar[:-1]
        self.unfamiliar_num = len(self.unfamiliar)
 
    def reset(self):
        self.error = []
        self.visit = {}
        self.right= []
        self.unfamiliar = []
        
        self.error_num = 0
        self.right_num = 0
        self.unfamiliar_num = 0   

if __name__ == '__main__':
    rw = RW()
    print(len(rw.word_list))
    