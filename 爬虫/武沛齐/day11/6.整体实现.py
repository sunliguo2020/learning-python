# @课程    : 爬虫逆向实战课
# @讲师    : 武沛齐
# @课件获取 : wupeiqi666

import execjs
import requests
import ddddocr
from bs4 import BeautifulSoup

cookie_dict = {}
# 1.首页请求
res = requests.get(url="https://xuexi.chinabett.com/")
cookie_dict.update(res.cookies.get_dict())
print(f"cookie 1:{cookie_dict}")
# 2.获取验证码地址
soup = BeautifulSoup(res.text, features="html.parser")
image_tag = soup.find(name="img", attrs={"id": "imgVerifity"})
code_src = image_tag.attrs['src']
print(code_src)

# 3.读取验证码并实现
res = requests.get(url=f"https://xuexi.chinabett.com{code_src}", cookies=cookie_dict)
cookie_dict.update(res.cookies.get_dict())

print(f"cookie 2 :{cookie_dict}")

ocr = ddddocr.DdddOcr(show_ad=False)
code = ocr.classification(res.content)

# 4.处理用户名&密码

js_string = """
function base64encode(str) {
    var base64EncodeChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    var base64DecodeChars = new Array(
    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 62, -1, -1, -1, 63,
    52, 53, 54, 55, 56, 57, 58, 59, 60, 61, -1, -1, -1, -1, -1, -1,
    -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
    15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -1, -1, -1, -1, -1,
    -1, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, -1, -1, -1, -1, -1);
    var out, i, len;
    var c1, c2, c3;
    len = str.length;
    i = 0;
    out = "";
    while (i < len) {
        c1 = str.charCodeAt(i++) & 0xff;
        if (i == len) {
            out += base64EncodeChars.charAt(c1 >> 2);
            out += base64EncodeChars.charAt((c1 & 0x3) << 4);
            out += "==";
            break;
        }
        c2 = str.charCodeAt(i++);
        if (i == len) {
            out += base64EncodeChars.charAt(c1 >> 2);
            out += base64EncodeChars.charAt(((c1 & 0x3) << 4) | ((c2 & 0xF0) >> 4));
            out += base64EncodeChars.charAt((c2 & 0xF) << 2);
            out += "=";
            break;
        }
        c3 = str.charCodeAt(i++);
        out += base64EncodeChars.charAt(c1 >> 2);
        out += base64EncodeChars.charAt(((c1 & 0x3) << 4) | ((c2 & 0xF0) >> 4));
        out += base64EncodeChars.charAt(((c2 & 0xF) << 2) | ((c3 & 0xC0) >> 6));
        out += base64EncodeChars.charAt(c3 & 0x3F);
    }
    return out;
};

function s1() {
    var data = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];
    var r = Math.floor(Math.random() * 62);
    return data[r];
}

function encryptPwd(password){
    //base64编码的密码每隔1位插入一个随机数 最后一位后面不插入
    var newPwd = [];
    var pwdlength = password.length;
    for (i = 0; i < pwdlength; i++) {
        newPwd.push(password[i]);
        if (i < pwdlength - 1)
            newPwd.push(s1());

    }
    var res = newPwd.join('');
    return res;
}
"""
JS = execjs.compile(js_string)

# 用户名
username = JS.call("base64encode", "18630087660")
# 密码
temp = JS.call("base64encode", "123")
password = JS.call("encryptPwd", temp)

# 5.登录
res = requests.post(
    url="https://xuexi.chinabett.com/Login/Entry",
    data={
        "userAccount": username,
        "password": password,
        "returnUrl": "/PersonalCenter",
        "proVing": code,
    },
    cookies=cookie_dict
)
print(res.text)
