# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-05-24 13:14
"""
import logging

# 创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# handler 写入日志文件
logfile = './log.txt'
fh = logging.FileHandler(logfile, mode='a')
fh.setLevel(logging.DEBUG)

# 输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)

# 定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d]-%(levelname)s:%(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

logger.debug('这是 logger debug message')
logger.info('这是 logger info message')
logger.warning('这是 logger warning message')
logger.error('这是 logger error message')
logger.critical('这是 logger critical message')
