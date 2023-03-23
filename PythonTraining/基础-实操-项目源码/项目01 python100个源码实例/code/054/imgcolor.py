import cv2  # 导入OpenCV-Python模块
import os   # 导入文件与系统模块
import numpy as np  # 导入数值计算库


'''
 * 功能：为图片应用写生素描滤镜，并且保存图片到指定路径
 * filein：要应用滤镜的图片的路径
 * picture_name：要应用滤镜的图片的文件名
'''
def filter(filein,picture_name):
    imgI_filename = os.path.join(filein,picture_name) # 源文件路径
    imgO_filename = os.path.join(r'out', picture_name)  # 目标文件路径
    img_rgb = cv2.imread(imgI_filename)  # 读取源图片

    num_down = 2   # 缩减像素采样的数目
    num_bilateral = 9 # 定义双边滤波的数目
    # 用高斯金字塔降低取样
    img_color = img_rgb
    for _ in range(num_down):
        img_color = cv2.pyrDown(img_color)
    # 重复使用小的双边滤波代替一个大的滤波
    for _ in range(num_bilateral):
        img_color = cv2.bilateralFilter(img_color,d=4,sigmaColor=8,sigmaSpace=4)
    # 升采样图片到原始大小
    for _ in range(num_down):
        img_color = cv2.pyrUp(img_color)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)  # 转换为灰度
    img_blur = cv2.medianBlur(img_gray, 19)  # 增加模糊效果。值越大越模糊（取奇数）
    # 检测到边缘并且增强其效果
    img_edge = cv2.adaptiveThreshold(img_blur,256,
                                     cv2.ADAPTIVE_THRESH_MEAN_C,
                                     cv2.THRESH_BINARY,
                                     blockSize=9,
                                     C=2)
    img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB) # 彩色图像转为灰度图像
    cv2.imwrite(imgO_filename, img_edge) # 保存图片
    
if __name__ == '__main__':
    imagelist = [] # 创建空列表
    #循环读取指定路径下的文件名
    for filename in os.listdir(r'in/'):
        imagelist.append(filename)  #将文件名添加到imagelist
        print(filename)
        filter(r'in',filename)  # 为图片应用写生素描滤镜
