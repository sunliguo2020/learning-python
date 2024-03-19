# -*- coding: utf-8 -*-
"""
 @Time : 2024/3/17 16:57
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import cv2

GAUSSIAN_BLUR_KERNEL_SIZE = (5, 5)
GAUSSIAN_BLUR_SIGMA_X = 0
CANNY_THRESHOLD1 = 200
CANNY_THRESHOLD2 = 450

TARGET_HEIGHT = 90
TARGET_WIDTH = 90


def get_gaussian_blur_image(image):
    """

    @param image:
    @return: 高斯滤波处理后的图片
    """
    return cv2.GaussianBlur(image, GAUSSIAN_BLUR_KERNEL_SIZE, GAUSSIAN_BLUR_SIGMA_X)


def get_canny_image(image):
    """

    @param image:
    @return: 边缘检测处理后
    """
    return cv2.Canny(image, CANNY_THRESHOLD1, CANNY_THRESHOLD2)


def get_contours(image):
    """

    @param image:
    @return: 轮廓信息
    """
    contours, _ = cv2.findContours(image, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    return contours


def get_contour_area_threshold(image_width, image_height):
    """
        返回图片最大和最小面积
    @param image_width:
    @param image_height:
    @return:
    """
    # contour_area_min = (image_width * 0.15) * (image_height * 0.25) * 0.8
    # contour_area_max = (image_width * 0.15) * (image_height * 0.25) * 1.2

    contour_area_min = TARGET_WIDTH * TARGET_HEIGHT * 0.8
    contour_area_max = TARGET_WIDTH * TARGET_HEIGHT * 1.2

    return contour_area_min, contour_area_max


def get_arc_length_threshold(image_width, image_height):
    """
    返回目标轮廓周长下限和上限
    @param image_width:
    @param image_height:
    @return:
    """
    # arc_length_min = ((image_width * 0.15) + (image_height * 0.25)) * 2 * 0.8
    # arc_length_max = ((image_width * 0.15) + (image_height * 0.25)) * 2 * 1.2

    arc_length_min = (TARGET_WIDTH + TARGET_HEIGHT) * 2 * 0.8
    arc_length_max = (TARGET_WIDTH + TARGET_HEIGHT) * 2 * 1.2

    return arc_length_min, arc_length_max


def get_offset_threshold(image_width):
    """
    缺口位置偏移量下限和上限
    @param image_width:
    @return:
    """
    offset_min = 0.2 * image_width
    offset_max = 0.85 * image_width

    return offset_min, offset_max


if __name__ == '__main__':
    image_raw = cv2.imread('img.png')
    image_height, image_width, _ = image_raw.shape
    print(f"背景图片大小：{image_width}*{image_height}")
    image_gaussian_blur = get_gaussian_blur_image(image_raw)
    image_canny = get_canny_image(image_gaussian_blur)
    contours = get_contours(image_canny)

    contour_area_min, contour_area_max = get_contour_area_threshold(image_width, image_height)
    arc_length_min, arc_length_max = get_arc_length_threshold(image_width, image_height)
    offset_min, offset_max = get_offset_threshold(image_width)

    offset = None

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)

        print(x, y, w, h)
        if contour_area_min < cv2.contourArea(contour) < contour_area_max and \
                arc_length_min < cv2.arcLength(contour, True) < arc_length_max and \
                offset_min < x < offset_max:
            cv2.rectangle(image_raw, (x, y), (x + w, y + h), (0, 0, 255), 2)
            offset = x

    cv2.imwrite('image_label.png', image_raw)
    print('offset', offset)

    cv2.imshow('canny', image_raw)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
