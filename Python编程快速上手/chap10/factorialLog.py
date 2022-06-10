# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/12/6 8:45
"""
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message) s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program')


def factorial(n):
    logging.debug('Start of factorial(%s%%)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ',total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % (n))
    return total


print(factorial(5))
logging.debug('End of program')
