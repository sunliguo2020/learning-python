# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-01-06 12:56
"""
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

from module1 import do_something
from module2 import do_something_else


def main():
    print(f"main:{logger.level}")
    logger.warning('Starting the program')

if __name__ == '__main__':
    main()
    do_something()
    do_something_else()
