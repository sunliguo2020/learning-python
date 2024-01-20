# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-01-20 13:00
"""
from PIL import Image

img = Image.open("slice.png")
print(img.size)
cropped = img.crop((160, 490, 240, 588))  # (left, upper, right, lower)
print(type(cropped))
cropped.save("slice2.png")