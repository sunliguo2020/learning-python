# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/1/16 13:08
"""


def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中。
    :param unprinted_designs:
    :param completed_models:
    :return:
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Printing model:{current_design}')
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """
    显示打印好的所有模型
    :param completed_models:
    :return:
    """
    print('\nThe following models have been printed')
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
