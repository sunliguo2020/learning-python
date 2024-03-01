# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-01-26 17:28
"""
import tesserocr
from PIL import Image

image = Image.open('captcha.png')
result = tesserocr.image_to_text(image)
print(result)