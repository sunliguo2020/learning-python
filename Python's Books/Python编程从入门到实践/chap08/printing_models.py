# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/1/16 13:03
"""
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_designs = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f'Printing model:{current_design}')
    completed_designs.append(current_design)

print("\nThe following models have been printed:")
for completed_model in completed_designs:
    print(completed_model)
