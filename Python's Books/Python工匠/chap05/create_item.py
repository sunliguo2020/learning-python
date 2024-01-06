# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-09-17 8:56
"""
MAX_LENGTH_OF_NAME = 5
MAX_ITEMS_QUOTA = 5


def get_current_items():
    return 'sdfdf'


class CreateItemError(Exception):
    """创建Item失败"""


def create_item(name):
    """
     创建一个新的item
    ：raises :当无法创建时抛出CreateItemError
    @param name:
    @return:
    """
    if len(name) > MAX_LENGTH_OF_NAME:
        raise CreateItemError("name of item is too long")
    if len(get_current_items()) > MAX_ITEMS_QUOTA:
        raise CreateItemError("items is full")
    return Item(name=name), ''


def create_from_input():
    name = input('请输入：')
    try:
        item = create_item(name)
    except CreateItemError as e:
        print(f"create item failed:{e}")
    else:
        print(f"item<{name}>created")


if __name__ == '__main__':
    create_from_input()
