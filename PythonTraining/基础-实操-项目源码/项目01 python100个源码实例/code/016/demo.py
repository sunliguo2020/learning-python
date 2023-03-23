print("||||||||||||||||||||||")
print("    摄氏温度转换器")
print("||||||||||||||||||||||")
she = input('请输入摄氏温度：').strip('')


def is_number(s):  # 判断数字是否为浮点数
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


if is_number(she):
    she = float(she)  # 摄氏温度
    hua = she * 1.8 + 32  # 华氏温度
    kai = she + 273.15  # 开氏温度
    lie = she * 0.8  # 列氏温度
    lan = (she + 273.15) * 1.8  # 兰金温度

    print("摄氏温度：{:.2f}".format(she))
    print("华氏温度：{:.2f}".format(hua))
    print("开氏温度：{:.2f}".format(kai))
    print("列氏温度：{:.2f}".format(lie))
    print("兰金温度：{:.2f}".format(lan))
else:
    print("输入温度错误！")
