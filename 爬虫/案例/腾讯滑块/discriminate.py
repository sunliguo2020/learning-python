# -*- coding: utf-8 -*-
"""
 @Time : 2024/3/17 14:41
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""

"""
pip3 install opencv-python
"""

import cv2 as cv


def get_pos(image):
    """
    缺口轮廓检测
    对付腾讯滑块够用
    该方法识别率 95% 左右
    """
    # 使用高斯模糊对图像进行平滑处理，以减少图像中的噪声和细节，使边缘检测更准确
    # def GaussianBlur(src,ksize,sigmaX,dst=None,SigmaY=None,borderType=None)
    # src 需要处理的图片
    # ksize 高斯内核大小(x,y)
    #
    blurred = cv.GaussianBlur(image, (5, 5), 0)
    # 使用Canny边缘检测算法从模糊后的图像中提取边缘信息。
    canny = cv.Canny(blurred, 200, 400)

    # 在边缘检测后的图像上查找轮廓。这里只查找最外层的轮廓（cv.RETR_EXTERNAL），
    # 并且轮廓近似方法采用cv.CHAIN_APPROX_SIMPLE。
    contours, hierarchy = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for i, contour in enumerate(contours):
        m = cv.moments(contour)
        if m['m00'] == 0:
            cx = cy = 0
        else:
            cx, cy = m['m10'] / m['m00'], m['m01'] / m['m00']

        """
        * **筛选条件**:  
        + 轮廓面积在6000到8000之间。  
        + 轮廓的周长在370到390之间。  
        + 轮廓的中心x坐标小于400的则跳过。  
        * **绘制并显示轮廓的外接矩形**:  
        """
        if 6000 < cv.contourArea(contour) < 8000 and 370 < cv.arcLength(contour, True) < 390:
            if cx < 400:
                continue
            x, y, w, h = cv.boundingRect(contour)  # 外接矩形

            cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv.imshow('image', image)
            return x
    return 0


if __name__ == '__main__':
    """
    这里是滑块缺口识别
    识别到后
    1。可以通过自动化工具取拖动滑块
    2。可以通过参数解析的形式生成参数提交通过验证
    """
    img0 = cv.imread('bg.jpg')
    get_pos(img0)

    cv.waitKey(0)
    cv.destroyAllWindows()
