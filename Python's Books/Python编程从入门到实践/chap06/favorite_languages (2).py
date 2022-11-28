# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/11/28 10:58
"""
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',

}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

for name,language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")