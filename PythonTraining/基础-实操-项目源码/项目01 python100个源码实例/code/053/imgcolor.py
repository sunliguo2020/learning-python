import cv2  # 导入OpenCV-Python模块
import os   # 导入文件与系统模块
import numpy as np  # 导入数值计算库

'''
 * 功能：为图片应用灰度滤镜，并且保存图片到指定路径
 * filein：要应用滤镜的图片的路径
 * picture_name：要应用滤镜的图片的文件名
'''
def filter(filein,picture_name):
    imgI_filename = os.path.join(filein,picture_name) # 源文件路径
    imgO_filename = os.path.join(r'out', picture_name)  # 目标文件路径
    img_rgb = cv2.imread(imgI_filename)  # 读取源图片
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY) # 转换为灰度
    # 调整亮度和对比度
    res = np.uint8(np.clip((1.2 * img_gray + 0), 0, 255))
    cv2.imwrite(imgO_filename, res)    # 保存转换后的图片
    ## cv2.imshow('GrayImage',img_cartoon)  # 加预览

if __name__ == '__main__':
    imagelist = [] # 创建空列表
    #循环读取指定路径下的文件名
    for filename in os.listdir(r'in/'):
        imagelist.append(filename)  #将文件名添加到imagelist
        print(filename)
        filter(r'in',filename)  # 为图片应用灰度滤镜

'''
#########################################################################
 import cv2
import numpy as np

original_image1 = cv2.imread('in/20140927_071425.jpg').astype(np.float32)/255

# 设置调整颜色参数，小于1时，数值越小，越具有美白效果。反之，大于1时数值越大，可对美白照片还原原色
gamma1 = 0.6
whitening = np.power(original_image1, gamma1)

# 去除噪点
denoise = cv2.medianBlur(whitening, 5)

cv2.imshow('original_image', original_image1)
cv2.imshow('whitening', whitening)
cv2.imshow('denoise', denoise)

'''

##
### 对图片进行二值化======================================================
##import cv2
##import numpy as np
##img1 = cv2.imread('003.jpg')
##img2 = cv2.imread('temppic.jpg')
##rows, cols, channels = img1.shape
##roi = img2[0:rows, 0:cols]
##img2gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
##ret, Mask = cv2.threshold(img2gray, 170, 255, cv2.THRESH_BINARY)
##Mask_inv = cv2.bitwise_not(Mask)
##img1_bg = cv2.bitwise_and(roi, roi, mask=Mask)
##img1_fg = cv2.bitwise_and(img1, img1, mask=Mask_inv)
##dst = cv2.add(img1_bg, img1_fg)
##img2[0:rows, 0:cols] = dst
##cv2.imshow('res', Mask)
##cv2.imshow('das', img2)
##cv2.waitKey(0)
##cv2.destroyAllWindows()


# 实时调整图片透明度
##import cv2
##import numpy as np
##
##def callback(object):
##    pass
##
##cv2.namedWindow('image')
##img1 = cv2.imread('temppic.jpg')
##[x, y, z] = img1.shape
### 创建一个相同规格的图像，可以自己读取一张图用切片工具
### 选出相同大小的矩阵
##img2 = np.zeros([x, y, z], img1.dtype)
##B, G, R = 10, 88, 21  # 自己调色
##img2[:, :, 0] = np.uint8(B)
##img2[:, :, 1] = np.uint8(G)
##img2[:, :, 2] = np.uint8(R)
##cv2.createTrackbar('alpha', 'image', 0, 100, callback)
##
##while True:
##    Alpha = cv2.getTrackbarPos('alpha', 'image')/100
##    img3 = cv2.addWeighted(img1, Alpha, img2, 1-Alpha, 0)
##    cv2.imshow('image', img3)
##    if cv2.waitKey(10) & 0xFF == ord('q'):
##        break
##cv2.destroyAllWindows()
