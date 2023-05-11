# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-05-11 13:01
"""
import cv2 as cv

# 读取设备
cap = cv.VideoCapture('/dev/video0', cv.CAP_V4L)
# 读取摄像头FPS
fps = cap.get(cv.CAP_PROP_FPS)

# set dimensions 设置分辨率
cap.set(cv.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 400)

video = cv.VideoWriter('video.avi', cv.VideoWriter_fourcc('I', '4', '2', '0'), fps, (800, 400)) # 初始化文件写入 文件名 编码解码器 帧率 文件大小

# 录制10帧
for i in range(10):
    # take frame 读取帧
    ret, frame = cap.read()
    if ret:
        # write frame to file
        cv.imwrite('image-{}.jpg'.format(i), frame) # 截图
        video.write(frame) # 录制视频

# release camera 必须要释放摄像头
cap.release()