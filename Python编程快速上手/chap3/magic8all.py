# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/11/28 21:22
"""

import random


def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It is certain"
    if answerNumber == 2:
        return 'It is decidely so'
    if answerNumber == 3:
        return 'yes'
    if answerNumber == 4:
        return "reply hazy try again"
    if answerNumber == 5:
        return "Ask again later"
    if answerNumber == 6:
        return 'Concentrate and ask again'
    if answerNumber == 7:
        return "My reply is no "
    if answerNumber == 8:
        return "Ooutlook not so good"
    if answerNumber == 9:
        return "very doubtful"


r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
