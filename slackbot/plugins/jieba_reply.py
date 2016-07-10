#coding: UTF-8

import sys
sys.path.append('../')

import jieba
jieba.load_userdict("slackbot/plugins/extra_dict/custom_dict.txt")
jieba.load_userdict("slackbot/plugins/extra_dict/dict.txt")
import jieba.analyse

import re
from slackbot.bot import respond_to
from slackbot.bot import listen_to

ANSWER_LIST = []

@respond_to(u'jieba')
def jieba_message(message):
    seg_list = jieba.cut("我超級喜歡吃茄子", cut_all=False)
    message.reply(u"Default Mode: " + "/ ".join(seg_list))


@listen_to(u'jieba')
def jieba_l_message(message):
    seg_list = jieba.cut("我超級喜歡吃茄子", cut_all=False)
    message.reply(u"Default Mode: " + "/ ".join(seg_list))

## 取得 quizmaster 丟出的題目字串，解析出問題及選項
@respond_to(unicode("題目", 'utf-8') + ' (.*)', re.DOTALL)
def receive_question(message, question):
    # if message._client.users[message._get_user_id()][u'name'] == "quizmaster":
    print isinstance(message.body['text'], unicode)
    m = re.match(u"(.*) \[(\d+)\] (.*)     ### (.*) \[END\]", message.body['text'])
    quiz_no = m.group(2)
    question = m.group(3)
    options = {}
    for item in m.group(4).split(','):
        index, value = item.split(':')
        options[index] = value
    seg_list = jieba.cut(question, cut_all=False)
    message.reply(u"text seg: " + "/ ".join(seg_list))
    # word2vec

@listen_to(unicode("題目", 'utf-8') + ' (.*)', re.DOTALL)
def receive_question(message, question):
    # if message._client.users[message._get_user_id()][u'name'] == "quizmaster":
    print isinstance(message.body['text'], unicode)
    m = re.match(u"(.*) \[(\d+)\] (.*)     ### (.*) \[END\]", message.body['text'])
    quiz_no = m.group(2)
    question = m.group(3)
    options = {}
    for item in m.group(4).split(','):
        index, value = item.split(':')
        options[index] = value
    seg_list = jieba.cut(question, cut_all=False)
    message.reply(u"text seg: " + "/ ".join(seg_list))
    # word2vec

## 當 quizmaster 丟出 "機器人小朋友請搶答"，請儘速把答案丟到 channel
@listen_to(unicode("機器人小朋友請搶答", 'utf-8') +'$')
def hello_send(message):
    # if message._client.users[message._get_user_id()][u'name'] == "quizmaster":
    reply_ans = ""
    for idx, ans in enumerate(ANSWER_LIST):
        reply_ans += str(idx + 1) + " : " + ans + ", "
    message.send("<@%s>: %s %s" % (PIX_INSPECTOR, unicode("請給分 ", 'utf-8'), reply_ans[:-2]))
    ANSWER_LIST[:] = []

# 幫按讚
@listen_to(unicode("題號", 'utf-8') + ' (.*)')
def hey(message, ans_string):
    message.react('+1')

# 回覆訊息範例
@respond_to('hello$', re.IGNORECASE)
def hello_reply(message):
    message.reply('hello sender!')