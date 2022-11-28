# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/11/28 11:16
"""
alien_0 = {'color':'green',
           'points':5}
alien_1 = {'color':'yellow',
           'points':10}
alien_2 = {'color':'red',
           'points':16}
aliens = [alien_0,alien_1,alien_2]

for alien in aliens:
    print(alien)

aliens = []

for alien_number in range(30):
    new_alien = {'color':'green',
                 'points':5,
                 'speed':'slow',
                 }
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print("...")
print(f"Total number os aliens:{len(aliens)}")
