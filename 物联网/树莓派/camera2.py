# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-05-11 13:31
"""
# 该程序打开摄像头，显示视频，按q拍摄一张照片并储存下来

import cv2

cap = cv2.VideoCapture(0)

while (1):
    # 获得图片
    ret, frame = cap.read()
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    # 展示图片
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # 存储图片
        cv2.imwrite("camera.jpg", frame)
        break

cap.release()
cv2.destroyAllWindows()
