# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-01-04 13:15
"""
import base64

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# 1、创建加密器
# MODE_ECB ->不需要IV
# MODE_CBC ->需要IV
aes = AES.new(key=b'abcdefghijklmnop', mode=AES.MODE_CBC, IV=b'0123456789123456')

# 2、加密一段数据试试
s = "我发给杨老师了，请杨老师下课发给我"  # str
print('s的类型', type(s), s)
bs = s.encode('utf-8')  # bytes
print('bs的类型', type(bs), bs)
bs = pad(bs, 16)  # 填充，aes大多数是16bit
print('bs的类型', type(bs), bs)
result = aes.encrypt(bs)
print('加密后', type(result), result)

# 需要对字节进行b64的处理
ss = base64.b64encode(result).decode()

print('最后的结果', type(ss), ss)

# 解密：
s = 'wQ5IxEL11fDbK/rqoHDagWWjWkv+T67pvLnkf/utGbSwEmshjcpNtFWjgxPdzH57hWUkXQasKXObL0y2hXzq9A=='
aes = AES.new(key=b'abcdefghijklmnop', mode=AES.MODE_CBC, IV=b'0123456789123456')
result = aes.decrypt(base64.b64decode(s))
r = unpad(result, 16)
print(r.decode('utf-8'))
