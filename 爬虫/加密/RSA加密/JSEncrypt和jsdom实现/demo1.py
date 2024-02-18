# -*- coding: utf-8 -*-
"""
 @Time : 2024/2/16 0:01
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import base64

import rsa


def RsaEncrypt(publickey, data):
    pubkey = rsa.PublicKey.load_pkcs1_openssl_pem(publickey.encode())
    msg = data.encode(encoding='utf-8')
    cryptedMessage = rsa.encrypt(msg, pubkey)
    info = str(base64.b64encode(cryptedMessage), encoding='utf-8')
    return info


PublicKey = '''-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDlXTJX5BgW2/oJRf3kTo7XZ3q7
aOnqN832+hkKe/xjKLKHnMTv+td/0Zsw1VkczWvodtLKsjJnrjiIx+dRIjLz2qYC
WagGNroXGeh0AQm+GarLqkpsxQpgu7p9HIgukF1lkUKkGlKLHk7WdOYMDEsvWpF/
BprA0vZPz1SeTjmllQIDAQAB
-----END PUBLIC KEY-----'''


def r_hashtoken(data):
    return RsaEncrypt(PublicKey, data)


if __name__ == '__main__':
    value = RsaEncrypt(PublicKey, '1708012726424')
    print(value)
