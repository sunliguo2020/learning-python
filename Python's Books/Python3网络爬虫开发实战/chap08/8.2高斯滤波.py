# -*- coding: utf-8 -*-
"""
 @Time : 2024/3/17 16:42
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import cv2 as cv

img0 = cv.imread('img.png')

if img0 is None:
    print("Error: Could not read image.")
    exit()

blurred = cv.GaussianBlur(img0, (5, 5), 0)
print(type(blurred))

# 边缘检测
canny = cv.Canny(blurred, 200, 450)

# 轮廓提取
contours, hierarchy = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# imshow('标题','')
# cv.imshow('Original Image', img0)
# cv.waitKey(0)
# cv.destroyAllWindows()

cv.imshow('canny', canny)
cv.waitKey(0)
cv.destroyAllWindows()
