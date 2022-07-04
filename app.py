'''
Descripttion: 
FilePath: /word_random/app.py
Author: lwk
Date: 2022-06-04 22:35:01
LastEditors: lwk
LastEditTime: 2022-07-04 23:26:01
'''
import sys
import os
sys.path.append(os.path.dirname(__file__))
import project.words as words
from flask import Flask, render_template, request
import random

app = Flask(__name__)
RW = words.RW()


@app.route('/')
@app.route("/index", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = RW.get_rand_word()
        return {'words': data}
    return render_template("index.html")


@app.route("/prior_word", methods=['GET', 'POST'])
def prior_word():
    if request.method == 'POST':
        data = RW.prior_word()
        return {'words': data}
    return render_template("index.html")


@app.route("/next_word", methods=['GET', 'POST'])
def next_word():
    if request.method == 'POST':
        data = RW.next_word()
        return {'words': data}
    return render_template("index.html")



@app.route("/random", methods=['GET', 'POST'])
def randomnum():
    if request.method == 'POST':
        data = random.randint(1, 10)
        return {'words': data}
    return render_template("index.html")


@app.route("/check", methods=['GET', 'POST'])
def check():
    if request.method == 'POST':
        data = request.values.get("status")
        # print(type(data))
        if data == "1":
            print("right")
            RW.update_right()
        elif data == "0":
            print("error")
            RW.update_error()
        elif data == "2":
            if RW.right_num > 0:
                RW.delright()
            else:
                RW.right_num = 0
        elif data == "3":
            if RW.error_num > 0:
                RW.delerror()
            else:
                RW.error_num = 0
        elif data == "4":
            RW.update_unfamiliar()
            print("unfamiliarwords")
        elif data == "5":
            if RW.unfamiliar_num > 0:
                RW.delunfamiliar()
            else:
                RW.unfamiliar_num = 0
        return {
            'error_words': RW.get_list("error"),
            'unfamiliar_words': RW.get_list("unfamiliar"),
            "right": RW.right_num,
            "error": RW.error_num,
            "unfamiliar": RW.unfamiliar_num
        }  # familiar words
    return render_template("index.html")


@app.route("/mean", methods=['GET', 'POST'])
def getmean():
    if request.method == 'POST':
        data = RW.get_cur_mean()
        return {'means': data}
    return render_template("index.html")


@app.route("/clearerror", methods=['GET', 'POST'])
def clearerror():
    if request.method == 'POST':
        RW.error = set()
        data = RW.get_cur_mean()
        return {'means': data}
    return render_template("index.html")


@app.route("/acc", methods=['GET', 'POST'])
def acc():
    if request.method == 'POST':
        accuracy = 0
        print(RW.right_num, RW.error_num, RW.unfamiliar_num, RW.right_num + RW.error_num + RW.unfamiliar_num)
        if RW.right_num == 0 and RW.error_num == 0 and RW.unfamiliar_num == 0:
            accuracy = 0
        else:
            accuracy = RW.right_num / (RW.right_num + RW.error_num + RW.unfamiliar_num)
        print("acc: ", accuracy)
        return {"acc": accuracy}
    return render_template("index.html")


@app.route("/reset", methods=['GET', 'POST'])
def reset():
    if request.method == 'POST':
        RW.reset()
        return {'status': 1}
    return render_template("index.html")


if __name__ == '__main__':
    # app.debug = True
    app.run(host="127.0.0.1", port=9999, debug=True)
