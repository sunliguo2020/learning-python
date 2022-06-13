# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/1/16 8:02
"""
def make_pizza(size,*toppings):
    """
    概述要制作的pizza
    :param size:
    :param toppings:
    :return:
    """
    print(f'\nMaking a {size}-inch pizza with the follwing toppings:')
    for topping in toppings:
        print(f'-{topping}')

make_pizza('pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')