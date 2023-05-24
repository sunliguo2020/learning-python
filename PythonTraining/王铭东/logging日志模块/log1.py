# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-05-24 13:07
"""

import logging

logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d]-%(levelname)s:%(message)s')

logging.debug('这是logging debug message')
logging.info('这是logging info message')
logging.warning('这是logging warning message')
logging.error('这是logging error message')
logging.critical('这是logging critical message')
