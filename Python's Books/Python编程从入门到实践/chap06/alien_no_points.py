# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/11/28 11:02
"""
alien_0 = {'color':'green',
           'speed':'slow',
           }
# print(alien_0['points'])
point_value = alien_0.get('points',"No point value assigned.")
print(point_value)