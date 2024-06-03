# -*- coding: utf-8 -*-
"""
 @Time : 2024/5/22 22:47
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
data = {
    # 子弹
    0: {
        'PATH': '../pic/other/peabullet.png',
        'IMAGE_INDEX_MAX': 0,
        'IMAGE_INDEX_CD': 0,
        'POSITION_CD': 0.008,
        'SIZE': (44, 44),
        'SPEED': (4, 0),
        'SUMMON_CD': -1,
        'CAN_LOOT': False,
        'PRICE': 0,
        'HP': 1,
        'ATT': 1,
    },
    # 僵尸
    1: {
        'PATH': '../pic/zombie/0/%d.png',
        'IMAGE_INDEX_MAX': 15,
        'IMAGE_INDEX_CD': 0.2,
        'POSITION_CD': 0.2,
        "SIZE": (100, 100),
        'SPEED': (-2.5, 0),
        'SUMMON_CD': -1,
        'CAN_LOOT': False,
        'PRICE': 0,
        'HP': 5,
        'ATT': 1,
    },
    # 阳光
    2: {
        'PATH': '../pic/other/sunlight/%d.png',
        'IMAGE_INDEX_MAX': 30,
        'IMAGE_INDEX_CD': 0.06,
        'POSITION_CD': 0.06,
        "SIZE": (80, 80),
        'SPEED': (0, 2),
        'SUMMON_CD': -1,
        'CAN_LOOT': True,
        'PRICE': 5,
        'HP': 1000,
        'ATT': 0,
    },
    # 向日葵
    3: {
        'PATH': '../pic/plant/sunflower/%d.png',
        'IMAGE_INDEX_MAX': 19,
        'IMAGE_INDEX_CD': 0.06,
        'POSITION_CD': 100000,
        "SIZE": (76, 100),
        'SPEED': (0, 2),
        'SUMMON_CD': 8,
        'CAN_LOOT': False,
        'PRICE': 20,
        'HP': 5,
        'ATT': 1,
    },
    # 豌豆射手
    4: {
        'PATH': '../pic/plant/peashooter/%d.png',
        'IMAGE_INDEX_MAX': 15,
        'IMAGE_INDEX_CD': 0.15,
        'POSITION_CD': 0.05,
        "SIZE": (76, 100),
        'SPEED': (0, 0),
        'SUMMON_CD': 3,
        'CAN_LOOT': False,
        'PRICE': 30,
        'HP': 5,
        'ATT': 1,
    },
}
