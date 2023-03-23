sdate = [20, 19, 21, 20, 21, 22, 23, 23, 23, 24, 23, 22]  # 星座判断列表
conts = ['摩羯座', '水瓶座', '双鱼座', '白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座',
         '射手座', '摩羯座']
signs = ['♑', '♒', '♓', '♈', '♉', '♊', '♋', '♌', '♍', '♎', '♏', '♐', '♑']

# 输入生日,输出星座
birth = input('请输入你的出生年月日,格式为:2001-02-21\n').strip(' ')
cbir = birth.split('-')  # 分割年月日到列表
cmonth = str(cbir[1])  # 提取月数据
cdate = str(cbir[2])  # 提取日数据


def sign(cmonth, cdate):  # 判断星座函数
    if int(cdate) < sdate[int(cmonth) - 1]:  # 如果日数据早于对应月列表中对应的日期
        print(conts[int(cmonth) - 1])  # 直接输出星座列表对应月对应的星座
        print(signs[int(cmonth) - 1])  # 直接输出星座列表对应月对应的星座
    else:
        print(conts[int(cmonth)])  # 否则输出星座列表下一月对应的星座
        print(signs[int(cmonth)])  # 否则输出星座列表下一月对应的星座


sign(cmonth, cdate)  # 调用星座判断程序
