# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-01-06 12:56
"""
import logging

logger = logging.getLogger(__name__)


def do_something():
    print(f"model1 :{logger}")
    logger.debug(f'module1:{logger.level}')
    logger.info('This is a message from module1')
