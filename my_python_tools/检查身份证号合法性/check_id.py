# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2021/4/20 18:41
检查身份证号是否合法
2022-02-11：检查最后一位是否为X

"""
import sys


def check_id_length(n):
    """
    检测身份证号长度是否为18位
    :param n:
    :return:
    """
    if len(str(n)) != 18:
        # print("只支持18位身份证号查询")
        return False
    else:
        return True


def check_id_data(n):
    """
    检查身份证号是否合法
    :param n:
    :return:
    """

    # print(n)
    # 加权数字列表
    var = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    # 标准 校验列表
    var_id = ['1', '0', 'x', '9', '8', '7', '6', '5', '4', '3', '2']
    n = str(n)
    # 判断是否是数字或者最后一位是X
    n2 = str(n[:17])
    # print("n2=",n2)
    is_digit = (not (n2.isdigit())) or (not (n[17].isdigit()) and (n[17]).lower() != "x")
    if is_digit:
        # print("对不起，您这是火星身份证，暂不受理")
        return

    id_sum = 0
    for i in range(0, 17):
        id_sum += int(n[i]) * var[i]
    id_sum %= 11
    if (var_id[id_sum]) == str(n[17]):
        # print("身份证号规则核验通过，校验码是：",var_id[sum])
        # print("出生于：",n[6:10],"年",n[10:12],"月",n[12:14],"日","性别：",gender,"\n当地同性别同生日排名：",same)
        return n
    else:
        # print("出生于：",n[6:10],"年",n[10:12],"月",n[12:14],"日","性别：",gender,"\n当地同性别同生日排名：",same)
        # print("但身份证号规则核验失败，校验码应为",var_id[sum],"，当前校验码是：",n[17])
        return


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("参数少于1个,缺少要检查的身份证文本文件!")
        sys.exit(-1)
    file_name = sys.argv[1]
    with open(file_name, encoding='utf-8') as f:
        for i in f:
            i = i.replace('\n', '')
            if check_id_length(i):
                idcardno = check_id_data(i)
                if idcardno:
                    print(idcardno)
