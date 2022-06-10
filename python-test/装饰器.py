account = {

    "is_login": False,
    "user_name": "sunliguo",
    "password": '12345'
}


def login(func):
    def inner(*args, **kwargs):
        if not account.get('is_login'):

            name = input("请输入用户名：")
            pw = input("请输入密码：")
            if name == account.get('user_name') and pw == account.get('password'):
                print("登陆成功！")
                account['is_login'] = True
                print("*args, **kwargs", args, args)
                res = func(*args, **kwargs)

        else:
            print("已经登陆")
            res = func(*args, **kwargs)
        return res

    return inner


@login
def home(s):
    print("首页", s)

    return s


# home = login(home)
res = home("ssdaf")
print(res)
