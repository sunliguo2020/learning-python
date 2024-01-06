# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-09-17 13:57
"""


def count_vowels(fp):
    """
    统计某个文件中元音字母（aeiou)的数量
    """
    VOWELS_LETTERS = {'a', 'e', 'i', 'o', 'u'}

    count = 0
    for line in fp:
        for char in line:
            if char.lower() in VOWELS_LETTERS:
                count += 1
    return count


if __name__ == '__main__':
    from io import  StringIO

    print(count_vowels(StringIO('hello,world!')))
