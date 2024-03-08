# -*- coding: utf-8 -*-
"""
 @Time : 2024/2/15 23:07
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend
import datetime
import base64


def r_hashtoken():
    # 公钥字符串
    public_key_pem = """-----BEGIN PUBLIC KEY-----  
    MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDlXTJX5BgW2/oJRf3kTo7XZ3q7  
    aOnqN832+hkKe/xjKLKHnMTv+td/0Zsw1VkczWvodtLKsjJnrjiIx+dRIjLz2qYC  
    WagGNroXGeh0AQm+GarLqkpsxQpgu7p9HIgukF1lkUKkGlKLHk7WdOYMDEsvWpF/  
    BprA0vZPz1SeTjmllQIDAQAB  
    -----END PUBLIC KEY-----"""

    # 加载公钥
    public_key = serialization.load_pem_public_key(
        public_key_pem.encode('utf-8'),
        backend=default_backend()
    )

    # 获取当前时间戳并转换为字节
    timestamp = datetime.datetime.now().timestamp() * 1000
    # print(timestamp)
    timestamp_bytes = str(int(timestamp)).encode('utf-8')
    # print(timestamp_bytes)
    # 加密时间戳
    encrypted = public_key.encrypt(
        timestamp_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # 将加密后的数据转换为Base64编码的字符串以便显示或传输
    encrypted_b64 = base64.b64encode(encrypted).decode('utf-8')
    # print(f"Encrypted timestamp (Base64): {encrypted_b64}")

    return encrypted_b64


if __name__ == '__main__':
    print(r_hashtoken())
