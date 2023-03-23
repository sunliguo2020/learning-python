import cv2
import time
import random
inx=input('按回车开始掷骰子!!').strip()
for i in range(10):
    cv2.waitKey(1)
    time.sleep(0.1)
    j=random.randint(1,6)
    imgj=str(j)+'a.png'
    img=cv2.imread(imgj)
    cv2.imshow("img",img)
if inx!='':
    if ord(inx) in range(49,55):
        imgj=inx+'a.png'
        img=cv2.imread(imgj)
        cv2.imshow("img",img)
