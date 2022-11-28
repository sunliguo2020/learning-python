# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022-11-08 13:02
"""


def incr_by_one(value):
    """
    对输入整数加1，或者可以转成整形的字符串
    @param value: 整型，或者可以转成整型的字符串
    @return: 整型结果
    """

    if isinstance(value, int):
        return value + 1

    elif isinstance(value, str) and value.isdigit():
        return (int(value)) + 1
    else:
        print(f'unable to perform incr for value:"{value}"')


def incr_by_one2(value):
    """

    @param value:
    @return:
    """

    try:
        return int(value) + 1
    except (TypeError, ValueError) as e:
        print(f"Unable to perform incr for value:'{value}',error:{e}")


if __name__ == '__main__':
    print(incr_by_one2('7s'))
