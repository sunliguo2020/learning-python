import datetime
import json

def get_working_age(hiredate):
    """
    计算工龄
    :param hiredate: datetime类型数据
    :return:
    """
    # 计算时间间隔，结果为天数
    days = (datetime.date.today() - hiredate).days
    # 计算为工龄，结果为年数
    working_age = days // 365
    return working_age

def get_uncheck_users(users):
    data = []
    for user in users:
        # 入职时间转化为字符串
        user.hiredate_str = user.hiredate
        # 计算工龄工资
        user.working_age = get_working_age(user.hiredate)
        # 判断用户是否修改
        if user.log:
            content_json = user.log[-1].update_content
            content_dict = json.loads(content_json)
            for key, value in content_dict.items():
                old, new = value.split(',')
                if old != new :
                    # 入职时间需要单独处理
                    if key == "hiredate":
                        user.hiredate_str = f'{old}->{new}'
                    else:
                        exec(f'user.{key} = "{old}->{new}"')
        # 追加到列表
        data.append(user)
    return data

def get_check_users(users):
    data = []
    for user in users:
        # 入职时间转化为字符串
        user.hiredate_str = user.hiredate
        # 计算工龄工资
        user.working_age = get_working_age(user.hiredate)
        # 追加到列表
        data.append(user)
    return data