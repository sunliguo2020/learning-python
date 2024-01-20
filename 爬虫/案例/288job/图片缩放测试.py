# -*- coding: utf-8 -*-
"""
 @Time : 2024/1/20 21:40
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 @File : 图片缩放测试.py
 @Project : learning-python
"""
import io

import requests
from PIL import Image

image_url = 'https://turing.captcha.qcloud.com/cap_union_new_getcapbysig?img_index=1&image=0279050000682d0100000009dcd20a723b7e&sess=s0oAKqemVIF3CXV3wFfUICSmCypd5ZxNJf4I7ZCIcmLZc0-zk7Dt67-K5JM7kvp5S3NCGaA0KPZTYu4F-kMO_AmS3WzaYgfINjnzhF9UwqhHSX1_Et9Jkeo9ygboMOQu_a89ByumPzURFc8xY5dAhTyvxzjBwLbBhgvRJrUlzvnyb39w2Wy0wfTqsoLeaBlnpZ4yieP-YdH8gGvkYHiuVDP5xzvvbv3EplN7pInHSDjK4GrtwK5PTJu-nfDceFRy_0n1g2C9YSHJJiW08wxsd0-apahfmsVua1ZHH9U-Crx7My9wrpwSwHDXD5sZgD2IS38qgreBpr9HfLOZCqurt0oKBFHaHwYnPbVPVmI_lMqJWfU5Qb6VOw3pYatK8kTq0OUnZc49_1v1tXTvcusx_QmecRkSohw5-zAlPYoN4CVQbbq4_5IySuzeZ4ylgl51j1NFTHi94wgjEbtqdjYZ73X86FtPGAQ-1UHR-I7q8QMVY*'
image_content = requests.get(image_url).content
image = Image.open(io.BytesIO(image_content))
# 调整图像大小为宽度为 500 像素，高度按比例缩放
resized_image = image.resize((340, 243))
print(type(resized_image))

# 保存调整大小后的图像
resized_image.save("resized_example.jpg")

resized_image_bytes = io.BytesIO()

resized_image.save(resized_image_bytes, 'png')
print(resized_image_bytes)
