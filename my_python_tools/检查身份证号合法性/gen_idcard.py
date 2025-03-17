# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2025/3/14 17:09
"""


def calculate_check_code(id_number):
    """
        计算身份证号校验码
    """
    # 加权因子
    weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    # 校验码对应表
    check_codes = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']

    # 计算加权和
    weighted_sum = sum(int(id_number[i]) * weights[i] for i in range(17))
    # 计算余数
    remainder = weighted_sum % 11
    # 返回校验码
    return check_codes[remainder]


def generate_valid_ids(prefix):
    """
        生成指定前缀的身份证号
        :param prefix: 身份证号前14位
        :return: 有效身份证号列表
    """
    valid_ids = []
    # 遍历顺序码（001 到 999）
    for seq in range(1, 1000):
        # 生成顺序码部分（3位，不足补零）
        seq_str = f"{seq:03}"
        # 拼接前17位
        id_17 = prefix + seq_str
        # 计算校验码
        check_code = calculate_check_code(id_17)
        # 拼接完整身份证号
        full_id = id_17 + check_code
        valid_ids.append(full_id)
    return valid_ids


if __name__ == '__main__':

    # 前14位
    prefix = "37078319850201"
    # 生成所有有效身份证号
    valid_ids = generate_valid_ids(prefix)

    # 打印结果

    with open("valid_ids.txt", "w") as file:
        for id_number in valid_ids:
            print(id_number)
            file.write(id_number + "\n")
