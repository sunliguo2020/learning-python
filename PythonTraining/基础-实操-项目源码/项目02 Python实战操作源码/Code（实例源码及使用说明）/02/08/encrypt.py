# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称   ：encrypt.PY
# 开发工具   ：PyCharm
'''
 对用户密码进行MD5或者SHA加密
'''
import hashlib
str = input('请输入要加密的字符串：')
#MD5加密（返回32位16进制表示字符串）
md5=hashlib.md5()
md5.update(str.encode('utf-8'))
print('MD5加密:',md5.hexdigest())

#SHA1加密（返回40位16进制表示字符串）
sha1=hashlib.sha1()
sha1.update(str.encode('utf-8'))
print('SHA1加密:',sha1.hexdigest())

#SHA256加密（返回64位16进制表示字符串）
sha256=hashlib.sha256()
sha256.update(str.encode('utf-8'))
print('SHA256加密:',sha256.hexdigest())

# 采用哈希算法计算后的MD5加密
import hmac
pwd=str.encode('utf-8')
key='id'.encode('utf-8')
h=hmac.new(key,pwd,digestmod='MD5')
print('更安全的MD5加密:',h.hexdigest())