import logging

# 创建一个全局的日志记录器
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
print(f"我是main.py的logger: {logger},我的级别是{logger.level}")

import module1
import module2


def main():
    logger.info('This is a message from the main program')

    module1.do_something()
    module2.do_something_else()


if __name__ == "__main__":
    main()
