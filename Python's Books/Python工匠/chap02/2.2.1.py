# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022-11-25 17:20
"""
from enum import Enum


def add_daily_points(user):
    """
    用户每天完成第一次登录后，为其增加记分
    @param user:
    @return:
    """
    if user.type == 13:
        return
    if user.type == 3:
        user.points += 120
        return
    user.points += 100
    return


# 用户每天奖励记分数量
DAILY_POINTS_REWARDS = 100
# VIP 用户每天额外奖励记分数量
VIP_EXTRA_POINTS = 20


class UserType(int, Enum):
    # VIP用户
    VIP = 3
    # 小黑屋用户
    BANNED = 13


def add_daily_points(user):
    if user.type == UserType.BANNED:
        return
    if user.type == UserType.VIP:
        user.points += DAILY_POINTS_REWARDS + VIP_EXTRA_POINTS
        return
    user.points += DAILY_POINTS_REWARDS
