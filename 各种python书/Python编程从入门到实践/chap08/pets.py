# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/1/16 8:25
"""


def describe_pet(pet_name, animal_type='dog'):
    """
    显示宠物的信息。
    :param animal_type:
    :param pet_name:
    :return:
    """
    print(f'\nI have a {animal_type}.')
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet('hamster', 'harry''sdfs')
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet('harryy', 'chick')
