import os,time


def get_screen_shot_img(img_type='png', img_path='/sdcard/douyin/', image_name='default'):
   """
   截屏
   """
   img_path = ''
   img_type = ''
   img_name=time.strftime("%Y%m%d%H%M%S", time.localtime())
   os.system('adb shell /system/bin/screencap -p /sdcard/xxx.jpg')


for i in range(1000000):
   strtime=time.strftime("%Y%m%d%H%M%S", time.localtime())
   os.system(r"C:\Users\sunliguo\Desktop\platform-tools\adb.exe shell input swipe 0 800 0 500")
   os.system(r"C:\Users\sunliguo\Desktop\platform-tools\adb.exe shell screencap /sdcard/douyin/" +strtime+".png")
   print(strtime+".png")
   time.sleep(1)
