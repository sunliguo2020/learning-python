# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-03-21 19:07
"""

import subprocess
from functools import partial  # 用来固定某个参数的固定值

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs


def get_x96(tt, tu):
    """

    @param tt:
    @param tu:
    @return:
    """

    with open('demo5.js', encoding='utf-8') as fp:
        js_content = fp.read()

    jj = execjs.compile(js_content)

    return jj.call('x96', tt, tu)


if __name__ == '__main__':
    tt = '/api/v4/search/preset_words'
    tu = 'ADDSD-j4lRePTsK721fRFrWpxQLGjfijbjo=|1697981461'
    print(get_x96(tt, tu))
