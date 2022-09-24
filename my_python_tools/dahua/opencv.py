# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/4/28 15:36
"""
import cv2

# 参数
# -------------------------------------- 这是一条分割线 --------------------------------------
# -------------------------------------- 摄像机的：用户名 密码 IP --------------------------------------

# path = 0 # 0表示计算机自带的摄像头，这样可以实验余下程序是否正确
#path = "rtsp://摄像机用户名:摄像机密码@摄像机IP地址:554/h264/ch1/main/av_stream"  # 把摄像机相应信息修改好

path = "rtsp://admin:admin123@192.168.1.247:554/cam/realmonitor?channel=2&subtype=1"

# 例如：path = "rtsp://admin:admin@192.168.0.66:554/h264/ch1/main/av_stream"
# -------------------------------------- 这是一条分割线 --------------------------------------



def main():
    camera = cv2.VideoCapture(path)

    while True:
        grabbed, frame = camera.read()
        cv2.putText(frame,
                    'Tips: Please click "Esc" to close the window.',
                    (0, 25),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    (0, 255, 255), 2)
        cv2.imshow("surveillance", frame)

        if cv2.waitKey(1) & 0xff == 27:
            break
    camera.release()
if __name__ == "__main__":
    main()