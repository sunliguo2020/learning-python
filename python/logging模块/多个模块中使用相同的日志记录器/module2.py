import logging

# 引用主程序中的日志记录器
logger = logging.getLogger(__name__)
print(f"我是{__name__}模块，logger是{logger},我的级别是{logger.level}")


def do_something_else():
    logger.info('This is a message from module2')
