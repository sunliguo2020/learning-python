import logging

# 引用主程序中的日志记录器
logger = logging.getLogger(__name__)

def do_something_else():
        logger.info('This is a message from module2')