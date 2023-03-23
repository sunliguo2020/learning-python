# -*- coding: utf-8 -*-
# 文件名称   ：videoTest.PY
# 开发工具   ：PyCharm
'''
  Python控制摄像头拍照
'''
import cv2 # 导入cv2模块
cap = cv2.VideoCapture(0) # 创建视频对象
while(1):
    ret, frame = cap.read() # 显示视频
    cv2.imshow("Capture", frame) # 显示视频窗口
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("test.jpeg", frame) # 保存图片
        break
cap.release() # 释放占用资源
cv2.destroyAllWindows() # 关闭窗体